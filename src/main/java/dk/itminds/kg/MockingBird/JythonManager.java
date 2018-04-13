package dk.itminds.kg.MockingBird;

import dk.itminds.kg.MockingBird.Helpers.PythonEvalResult;
import org.python.core.PyCode;
import org.python.core.PyException;
import org.python.core.PySyntaxError;
import org.python.core.PySystemState;
import org.python.util.PythonInterpreter;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Map;

/**
 * @author Kristian Gausel
 */
public class JythonManager {

    private MockingBird mockingBird;
    private Logger log;

    public JythonManager(MockingBird mockingBird){
        this.mockingBird = mockingBird;
        this.log = LoggerFactory.getLogger(JythonManager.class);
    }

    public PythonInterpreter getNewInterpreter(){
        // https://stackoverflow.com/a/40269239/2551905
        PythonInterpreter newInterpreter = new PythonInterpreter(null, new PySystemState());
        newInterpreter.set("__bird__", mockingBird);
        return newInterpreter;
    }

    public PythonInterpreter getNewInterpreter(Map<String, Object> bindings){
        PythonInterpreter interpreter = getNewInterpreter();
        for(Map.Entry<String, Object> binding : bindings.entrySet()){
            interpreter.set(binding.getKey(), binding.getValue());
        }
        return interpreter;
    }

    public void openPythonREPL(){
        PythonInterpreter interpreter = getNewInterpreter();
        String code =
                "from JythonConsole import console\n" +
                        "console.main(__bird__)";

        PyCode compiledCode = interpreter.compile(code);
        interpreter.eval(compiledCode);
        log.info("Python REPL opened");
    }

    public PythonEvalResult execfile(String path, PythonInterpreter interpreter){
        try {
            interpreter.execfile(path);
            return new PythonEvalResult(null, interpreter);
        } catch (PySyntaxError syntaxError){
            return new PythonEvalResult(null, interpreter, syntaxError);
        } catch (PyException pythonException){
            return new PythonEvalResult(null, interpreter, pythonException);
        } catch (Exception otherException){
            return new PythonEvalResult(null, interpreter, otherException);
        }
    }

}
