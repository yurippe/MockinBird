package dk.itminds.kg.MockingBird.Helpers;

/**
 * @author Kristian Gausel
 */
public interface CommandHandler {

    void handleCommand(String[] args);

    void shutdown();

}
