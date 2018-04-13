from org.slf4j import LoggerFactory

from dk.atomit.Builders import JSONBuilder #Use this for Java objects
from PyJettyHandler import PyJettyHandler, Template

from javax.servlet.http import HttpServletResponse
from java.lang import Object as JavaObject

from jinja2 import Template as JinjaTemplate

import json
import os

BASE_DIR = os.path.dirname(os.path.join(os.getcwd(), __path__))

ErrorTemplate = JinjaTemplate("""
<!DOCTYPE html>
<html>
<head></head>
<body>{{ errormessage }}</body>
</html>                   
""")

InfoTemplate = JinjaTemplate("""
<!DOCTYPE html>
<html>
<head></head>
<body>
Path: {{ path }}<br />
Parameters:<br/>
<pre><code>
{{ parameters }}
</code></pre>
</body>
</html> 
""")

handler = PyJettyHandler()
__bird__.setHandler(handler)

class PythonCode(JavaObject):
    pass

log = LoggerFactory.getLogger(PythonCode)

@handler.path("/name/(?P<name>\\w+)")
@Template(os.path.join(BASE_DIR, "templates", "base.template"), cache=False)
def handle_name_page(pyRequest):

    name = pyRequest.getStrGroup("name", "Admin")

    pyRequest.out.println(
        pyRequest.template.render({
                
                "name": name
                
        }))

@handler.path("/socketio")
@Template(os.path.join(BASE_DIR, "templates", "socketio.template"), cache=False)
def handle_socketIO_front(pyRequest):
    plugins = __bird__.getActiveMockingBirdREPL().getSubHandlers()
    if not plugins.containsKey("socketio"):
        pyRequest.out.println(
                ErrorTemplate.render({ "errormessage":
                                           ("The SocketIO plugin should be enabled for this to work<br/>"
                                            "To enable the plugin use the command 'start socketio 0.0.0.0 9092'")
                                     }))
        return

    pyRequest.out.println(
        pyRequest.template.render({


        }))

@handler.path(".*")
def handle_all_other_pages(pyRequest):

    params = json.loads(JSONBuilder.objectToJSON(pyRequest.params))
    params = json.dumps(params, indent=4)
    
    pyRequest.out.println(
        InfoTemplate.render({
            "parameters": params,
            "path": pyRequest.path
            }))
    
