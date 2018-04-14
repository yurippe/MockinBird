import time
import random

repl = __bird__.getActiveMockingBirdREPL()
plugins = repl.getPlugins()

if plugins.containsKey("socketio"):
    sio = plugins.get("socketio")

    for i in range(1000):
        sio.broadcastEvent("myevent", "Loop %d" % (i))
        time.sleep(random.randint(0,5))
    
