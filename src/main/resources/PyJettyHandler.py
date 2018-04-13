from org.eclipse.jetty.server.handler import AbstractHandler
from javax.servlet.http import HttpServletResponse

import re
import base64

try: from jinja2 import Template as JTemplate
except: pass

def Transaction(db):
    """Decorator to wrap a whole handler. This will attempt to set a transaction property on the first argument"""
    def wrapper(f):
        def transaction_wrapper(*args, **kwargs):
            tx = db.beginTx()
            
            try: args[0].transaction = tx
            except: pass
        
            result = f(*args, **kwargs)
            tx.success()
            tx.close()
            return result
        return transaction_wrapper
    return wrapper

def Template(path, cache=True):
    if cache:
        with open(path, "r") as templatefile:
            template = JTemplate(templatefile.read())
    def wrapper(f):
        def template_wrapper(*args, **kwargs):
            
            if not cache: #Reload file
                with open(path, "r") as templatefile:
                    templ = JTemplate(templatefile.read())
            else:
                templ = template
                    
            try: args[0].template = templ
            except: pass
            return f(*args, **kwargs)
        return template_wrapper
    return wrapper

class PyJettyHandler(AbstractHandler):

    def __init__(self):
        self.handlers = []

    def handle(self, path, baseRequest, request, response):
        for regex, handler in self.handlers:
            match = regex.match(path)
            if match:
                response.setContentType("text/html; charset=utf-8")
                response.setStatus(HttpServletResponse.SC_OK)
                baseRequest.setHandled(True)
                handler(PyRequest(self, match, path, baseRequest, request, response))
                if baseRequest.isHandled():
                    return
        
        response.setContentType("text/html; charset=utf-8")
        response.setStatus(HttpServletResponse.SC_NOT_FOUND)
        response.getWriter().println("<!DOCTYPE html><html><body><h1>404 Not Found</h1></body></html>")
        baseRequest.setHandled(True)

    def register_handler(self, regex, handler):
        """Register a handler to handle the path matched by regex. If multiple matches are possible,
        the handler registered first will get the request"""
        regex = re.compile("^" + regex + "$")
        self.handlers.append((regex, handler))

    def path(self, path):
        """Decorator for register_handler
        example usage:
            handler = PyJettyHandler()
            @handler.path("/test/\\d+")
            def handle_test_number(pyRequest):
                pyRequest.out.println("hello world!")
        """
        def f(handler):
            self.register_handler(path, handler)
            return handler
        return f

class PyRequest(object):
    """
    Pretty complete example of a handler:
    
    @handler.path("/scan/(?P<scanid>\\d+)")
    @Transaction(db) #The order here matters
    def handle_scan_page(pyRequest):
        pyRequest.response.setContentType("application/json; charset=utf-8")
        
        # Can be called as /scan/229?limit=10 to get scan info from scan with id 229 and limit it to 10 results
        
        #pyRequest.out.println(JSONBuilder.objectToJSON(pyRequest.params))
        #pyRequest.out.println("")
        
        #tx = db.beginTx() #Not needed because of the Transaction decorator
        result = db.execute("WITH $sid as scanid "
                            "MATCH (scan:Scan {scanid: scanid})<-[:STATS_FROM]-(ws:WebStats) "
                            "RETURN neon.list.tolist(scan, $limit) as scans, neon.list.tolist(ws, $limit) as stats",
                            {"sid": pyRequest.getIntGroup("scanid"),
                             "limit": pyRequest.getIntParam("limit", 10)})
        output = JSONBuilder.objectToJSON(result)
        
        #tx.success() #Not needed because of the Transaction decorator
        #tx.close()
        
        pyRequest.out.println(output)
    """
    
    def __init__(self, handler, match, path, baseRequest, request, response):
        self.handler = handler
        self.match = match
        self.path = path
        self.baseRequest = baseRequest
        self.request = request
        self.response = response
        
        #Will be set by the wrapper if needed
        self.transaction = None
        self.template = None
        
    def getRequestContent(self):
        """Read the request content (from ex. POST requests)"""
        return "\n".join(self.request.getReader().lines().toArray())
    
    def getBasicAuthorization(self):
        """Returns a tuple of (username, password) from a basic authorization,
        or None if no Basic Authorization is present in the headers"""
        header = self.request.getHeader("Authorization")
        if header:
            try:
                if header.lower().startswith("basic "):
                    authstr = base64.b64decode(header[6:]).split(":")
                    if len(authstr) == 1:
                        return None
                    return authstr[0], ":".join(authstr[1:])
            except:
                return None
        return None
    
    @property
    def out(self):
        return self.response.getWriter()
    
    @property
    def params(self):
        return self.request.getParameterMap()
    
    def getIntParam(self, paramkey, default=None):
        """Get a path parameter and cast it to an integer, if the parameter is
        not present, or the value can not be cast to an integer, return default"""
        value = self.request.getParameter(paramkey)
        if value is None: return default
        try: return int(value)
        except: return default
        
    def getStrParam(self, paramkey, default=None):
        """Get a path parameter, or if the parameter is not a present, return default"""
        value = self.request.getParameter(paramkey)
        if value is None: return default
        return value
    
    def getIntGroup(self, groupname, default=None):
        """Get a regexp group from the path, and convert it to an integer, 
        if the group does not exist or if the value can't be cast to an integer, 
        return default"""
        try: return int(self.match.group(groupname))
        except: return default
        
    def getStrGroup(self, groupname, default=None):
        """Get a regexp group from the path, and convert it to an integer, 
        if the group does not exist return default"""
        
        try:
            value = self.match.group(groupname)
            if value is None: return default
            return value
        except: return default
        
    def loadStaticContent(self, path, bytemode=False):
        """Loads a file and returns its contents"""
        with open(path, "r" + ("b" if bytemode else "")) as f:
            content = f.read()
        return content
