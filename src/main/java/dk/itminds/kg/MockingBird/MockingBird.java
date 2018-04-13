package dk.itminds.kg.MockingBird;

import dk.itminds.kg.MockingBird.Helpers.DefaultJettyHandler;
import org.eclipse.jetty.server.Handler;
import org.eclipse.jetty.server.Server;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * @author Kristian Gausel
 */
public class MockingBird {

    private JythonManager jythonManager;

    private Server server;

    private int port;
    private Logger log;

    private MockingBirdREPL activeREPL;

    public MockingBird(){
        this(8080);
    }

    public MockingBird(int port){
        this.port = port;
        this.log = LoggerFactory.getLogger(MockingBird.class);
        this.jythonManager = new JythonManager(this);
    }

    public void start(){
        server = new Server(port);
        log.info("Started HTTP server on port " + port);
        server.setHandler(new DefaultJettyHandler());
        log.info("Set handler to default handler");

        try {
            server.start();
        } catch (Exception e){
            log.error("Exception while starting server", e);
        }
    }

    public void stop(){
        try {
            server.stop();
        } catch (Exception e){
            log.error("Exception while stopping server", e);
        }
    }

    public void setHandler(Handler handler){
        try {
            server.stop();
            server.setHandler(handler);
            server.start();
        } catch (Exception e){
            log.error("Exception while setting handler", e);
        }
    }

    public JythonManager getJythonManager(){
        return this.jythonManager;
    }

    public void startREPL(){
        MockingBirdREPL repl = new MockingBirdREPL(this);
        repl.begin();
    }

    public int getPort(){
        return port;
    }

    public MockingBirdREPL getActiveMockingBirdREPL(){
        return activeREPL;
    }

    public void setActiveMockingBirdREPL(MockingBirdREPL repl){
        this.activeREPL = repl;
    }


    public static void main(String[] args) {

        MockingBird bird = new MockingBird(9000);

        bird.start();
        //bird.getJythonManager().openPythonREPL();
        bird.startREPL();
        bird.stop();

    }



}
