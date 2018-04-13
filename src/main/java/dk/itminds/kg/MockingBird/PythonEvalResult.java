package dk.itminds.kg.MockingBird;

import org.python.core.PyObject;
import org.python.util.PythonInterpreter;

/**
 * @author Kristian Gausel
 */
public  class PythonEvalResult {
    private PyObject evalResult;
    private PythonInterpreter interpreter;
    private Throwable exception;

    public PythonEvalResult(PyObject evalResult, PythonInterpreter interpreter){
        this(evalResult, interpreter, null);
    }

    public PythonEvalResult(PyObject evalResult, PythonInterpreter interpreter, Throwable exception){
        this.evalResult = evalResult;
        this.interpreter = interpreter;
        this.exception = exception;
    }

    /**
     * @return the result of evaluating the code as a PyObject
     */
    public PyObject getEvalResult(){
        return evalResult;
    }

    /**
     * @return The python interpreter used to evaluate the PyObject
     */
    public PythonInterpreter getInterpreter(){
        return interpreter;
    }

    /**
     * @return any exception that happened during execution
     */
    public Throwable getException(){
        return exception;
    }
}