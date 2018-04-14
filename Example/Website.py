from org.slf4j import LoggerFactory

from dk.atomit.Builders import JSONBuilder #Use this for Java objects
from PyJettyHandler import PyJettyHandler, FileSystemLoader

from javax.servlet.http import HttpServletResponse
from java.lang import Object as JavaObject

from jinja2 import Template as JinjaTemplate

import json
import os

# Calculate the Base directory, this is calculated based on the path of the script joined with the current working dir
BASE_DIR = os.path.dirname(os.path.join(os.getcwd(), __path__))
# Make the @template decorator by supplying a template directory. This allows for template inheritance
template = FileSystemLoader([os.path.join(BASE_DIR, "templates")])

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

# Create a new Jetty Handler
handler = PyJettyHandler()
# Set the new handler as the default handler for Jetty
__bird__.setHandler(handler)

# Set the base path for static files
handler.setStaticContext(BASE_DIR)
# Add some static files to serve. These take priority over regex matches.
handler.static("/base.source", "templates/base.template", contentType="text/plain; charset=utf-8")
handler.static("/base.source.cache", "templates/base.template", contentType="text/plain; charset=utf-8", cache=True)

# Create a logger, (kind of hacky code)
class PythonCode(JavaObject):
    pass
log = LoggerFactory.getLogger(PythonCode)

@handler.path("/name/(?P<name>\\w+)")
@template("hello.template")
def handle_name_page(pyRequest):

    name = pyRequest.getStrGroup("name", "Admin")

    pyRequest.out.println(
        pyRequest.template.render({
                "name": name
        }))

@handler.path("/socketio")
@template("socketio.template")
def handle_socketIO_front(pyRequest):
    plugins = __bird__.getActiveMockingBirdREPL().getPlugins()
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