package dk.itminds.kg.MockingBird;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.Console;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Kristian Gausel
 */
public class MockingBirdREPL {

    private MockingBird bird;
    private Console console;
    private Logger log;

    public MockingBirdREPL(MockingBird bird){
        this.bird = bird;
        this.log = LoggerFactory.getLogger(MockingBirdREPL.class);
    }

    public void begin(){
        console = System.console();
        String input = console.readLine(">> ");
        while(!input.equals("stop")){

            String[] args = input.split("\\s");
            if(args.length < 1 || input.equals("")) {
                input = console.readLine(">> ");
                continue;
            }

            switch (args[0]){
                case "help": CMD_help(); break;
                case "jython": CMD_jythonREPL(); break;
                case "sethandler": CMD_setHandler(args); break;
                case "run": CMD_jythonRun(args); break;

                default: console.writer().println("Unknown command '" + args[0] +
                        "' (Arguments: [\"" + String.join("\", \"", new ArrayView(args).setWindow(1, args.length)) + "\"])");
            }

            input = console.readLine(">> ");

        }
    }

    private void CMD_help(){
        console.writer().println("help: TODO");
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

    private void CMD_replaceHandler(){

    }

}
