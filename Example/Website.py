from org.slf4j import LoggerFactory

from PyJettyHandler import PyJettyHandler, Template

from javax.servlet.http import HttpServletResponse
from java.lang import Object as JavaObject

from jinja2 import Template as JinjaTemplate
import os

BASE_DIR = os.path.dirname(os.path.join(os.getcwd(), __path__))

ErrorTemplate = JinjaTemplate("""
<!DOCTYPE html>
<html>
<head></head>
<body>{{ errormessage }}</body>
</html>                   
""")

handler = PyJettyHandler()
__bird__.setHandler(handler)

class PythonCode(JavaObject):
    pass

log = LoggerFactory.getLogger(PythonCode)
print("--------")
print(dir())
print(os.path.dirname(os.path.realpath('__file__')))
print(__path__)
print(os.path.dirname(os.path.join(os.getcwd(), __path__)))
print("--------")

@handler.path("/name/(?P<name>\\w+)")
@Template(os.path.join(BASE_DIR, "templates", "base.template"), cache=False)
def handle_all_pages(pyRequest):

    name = pyRequest.getStrGroup("name", "Admin")

    pyRequest.out.println(
        pyRequest.template.render({
                
                "name": name
                
                }))
    

