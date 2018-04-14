package dk.itminds.kg.MockingBird;

import dk.itminds.kg.MockingBird.Helpers.ArrayView;
import dk.itminds.kg.MockingBird.Helpers.CommandHandler;
import dk.itminds.kg.MockingBird.Helpers.PythonEvalResult;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.Console;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Kristian Gausel
 */
public class MockingBirdREPL {

    private MockingBird bird;
    private Console console;
    private Logger log;

    private Map<String, CommandHandler> subHandlers = new HashMap<>();
    private Map<Long, Thread> threads = new HashMap<>();

    private static final String REPL_PREFIX = ">> ";

    public MockingBirdREPL(){
        this(null);
    }

    public MockingBirdREPL(MockingBird bird){
        this.bird = bird;
        this.log = LoggerFactory.getLogger(MockingBirdREPL.class);
    }

    public void begin(){
        console = System.console();
        CMD_help();
        String input = console.readLine(REPL_PREFIX);
        while(!input.equals("stop")){

            String[] args = input.split("\\s");
            if(args.length < 1 || input.equals("")) {
                input = console.readLine(REPL_PREFIX);
                continue;
            }

            if(bird == null){
                if(args[0].equals("start")){
                    int port = 9000;
                    try {port = Integer.parseInt(args[1]);} catch (Exception e){}
                    bird = new MockingBird(port);
                    bird.setActiveMockingBirdREPL(this);
                    bird.start();
                } else if(args[0].equals("help")){
                  CMD_help();
                } else {
                    console.writer().println("MockingBird not started, to start use the command `start [port]`");
                }
                input = console.readLine(REPL_PREFIX);
                continue;
            }

            switch (args[0]){
                case "help": CMD_help(); break;
                case "start": CMD_start(args); break;
                case "jython": CMD_jythonREPL(); break;
                case "sethandler": CMD_setHandler(args); break;
                case "run": CMD_jythonRun(args); break;
                case "runasync": CMD_jythonRunAsync(args); break;

                default: if(subHandlers.containsKey(args[0])){
                            String[] subargs;
                            if(args.length < 2){
                               subargs = new String[]{"help"};
                            } else {
                                subargs = Arrays.copyOfRange(args, 1, args.length);
                            }
                            subHandlers.get(args[0]).handleCommand(subargs);
                         } else {
                            console.writer().println(
                                      "Unknown command '" + args[0] + "' (Arguments: [\"" +
                                      String.join("\", \"", new ArrayView(args).setWindow(1, args.length)) + "\"])");
                         }
            }

            input = console.readLine(REPL_PREFIX);

        }

        if(input.equals("stop")){
            subHandlers.values().forEach(CommandHandler::shutdown);
        }
        subHandlers.clear();
    }

    private void CMD_help(){
        console.writer().println("Available commands: ");
        console.writer().println("\t `start <service> [args]`: Starts a service");
        console.writer().println("\t `jython`: Opens a Jython REPL with __bird__ set to the MockingBird instance");
        console.writer().println("\t `run <path>`: Runs the Python script at location <path>");
        console.writer().println("\t `runasync <path>`: Runs the Python script at location <path> in a separate thread");
        //console.writer().println("\t `threads`: Lists all running thread ids");
        //console.writer().println("\t `interupt <id>`: Interrupts thread with id <id>");
        console.writer().println("\t Plugins:");
        for(String plugin : subHandlers.keySet()){
            console.writer().println("\t\t`"  + plugin + "`");
        }
        console.writer().println("\t `stop`: Stops the server");
    }

    private void CMD_jythonREPL(){
        bird.getJythonManager().openPythonREPL();
    }

    private void CMD_setHandler(String[] args){
        console.writer().println("NOT IMPLEMENTED");
    }

    private void CMD_jythonRun(String[] args){
        String path = String.join(" ", new ArrayView(args).setWindow(1, args.length));

        Map<String, Object> env = new HashMap<>();
        env.put("__path__", path);

        PythonEvalResult result = bird.getJythonManager().execfile(path, bird.getJythonManager().getNewInterpreter(env));
        if(result.getException() != null){
            log.warn("Exception when executing script '" + path + "'", result.getException());
        }
    }

    private void CMD_jythonRunAsync(String[] args){
        String path = String.join(" ", new ArrayView(args).setWindow(1, args.length));

        Map<String, Object> env = new HashMap<>();
        env.put("__path__", path);

        Thread t = bird.getJythonManager().execfileAsync(path, bird.getJythonManager().getNewInterpreter(env)); //Currently this should stop by itself
        threads.put(t.getId(), t);
    }

    private void CMD_start(String[] args){
        if(args.length < 2){
            console.writer().println("MockingBird already running on port " + bird.getPort());
            CMD_start_supplementtext();
            return;
        }

        switch (args[1]){
            case "socketio": CMD_start_socketio(args); break;

            default: console.writer().println("Unknown service: '" + args[1] + "'"); CMD_start_supplementtext();
        }


    }

    private void CMD_start_supplementtext(){
        console.writer().println("You can start the following other services by using the command:");
        console.writer().println("`start <service> [args]`");
        console.writer().println("\t`start socketio [interface] [port]`: Starts a SocketIO server on interface [interface] (default: 0.0.0.0) and  port [port] (default: 9092)");
    }

    private void CMD_start_socketio(String[] args){
        if(subHandlers.containsKey("socketio")){
            console.writer().println("SocketIO already running");
            return;
        }
        int port = 9092;
        String hostname = "0.0.0.0";
        try {hostname = args[2];} catch (Exception e){}
        try {port = Integer.parseInt(args[3]);} catch (Exception e){}
        console.writer().println("Starting SocketIO on interface " + hostname + ":" + port);
        try {
            subHandlers.put("socketio", new SocketIOManager(bird, console,hostname, port));
        } catch (Exception e){
            log.warn("Exception when trying to start SocketIO", e);
        }
    }

    private void CMD_replaceHandler(){

    }

    public Map<String, CommandHandler> getPlugins(){
        return subHandlers;
    }
    public Map<Long, Thread> getThreads(){ return threads; }

    public static void main(String[] args) {

        MockingBirdREPL repl = new MockingBirdREPL(null);
        repl.begin();

        if(!(repl.bird == null)){
            repl.bird.stop();
        }

    }

}
