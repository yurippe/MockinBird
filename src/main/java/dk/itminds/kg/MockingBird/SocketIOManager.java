package dk.itminds.kg.MockingBird;

import com.corundumstudio.socketio.Configuration;
import com.corundumstudio.socketio.SocketIOServer;
import dk.itminds.kg.MockingBird.Helpers.ArrayView;
import dk.itminds.kg.MockingBird.Helpers.CommandHandler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.Console;

/**
 * @author Kristian Gausel
 */
public class SocketIOManager implements CommandHandler {

    private MockingBird bird;
    private SocketIOServer sioServer;
    private Console console;

    private Logger log;

    private String hostname;
    private int port;

    public SocketIOManager(MockingBird bird, Console console, String hostname, int port){
        this.bird = bird;
        this.console = console;
        this.log = LoggerFactory.getLogger(SocketIOManager.class);

        this.hostname = hostname;
        this.port = port;

        Configuration configuration = new Configuration();
        configuration.setHostname(hostname);
        configuration.setPort(port);

        this.sioServer = new SocketIOServer(configuration);
        sioServer.start();
    }

    @Override
    public void handleCommand(String[] args) {
        switch (args[0]){
            case "stop": CMD_stop_and_remove(); break;
            case "event": CMD_broadcast(args); break;

            default: console.writer().println("'" + args[0] + "' is not a valid SocketIO command"); CMD_help();
        }
    }

    private void CMD_help(){

    }

    private void CMD_stop_and_remove(){
        shutdown();
        bird.getActiveMockingBirdREPL().getPlugins().remove("socketio");
    }

    private void CMD_broadcast(String[] args){
        if(args.length < 3){
            console.writer().println("Too few arguments, Usage: event <name> <data>");
            return;
        }
        String eventName = args[1];
        String eventData = String.join(" ", new ArrayView<>(args).setWindow(2, args.length));
        broadcastEvent(eventName, eventData);
    }

    public void broadcastEvent(String name, Object data){
        sioServer.getBroadcastOperations().sendEvent(name, data);
        log.info("Broadcast event '" + name + "' with data: " + data);
    }

    @Override
    public void shutdown() {
       sioServer.stop();
    }

    public int getPort(){
        return port;
    }

    public String getHostname(){
        return hostname;
    }
}
