package dk.itminds.kg.MockingBird.Helpers;

import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * Created by Kristian on 4/13/2018.
 */
public class DefaultJettyHandler extends AbstractHandler{
    @Override
    public void handle(String s, Request request, HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse) throws IOException, ServletException {
        httpServletResponse.setContentType("text/html; charset=utf-8");
        httpServletResponse.setStatus(HttpServletResponse.SC_OK);

        PrintWriter out = httpServletResponse.getWriter();
        out.println("<!DOCTYPE html><html><head></head><body><h1>Welcome to MockingBird</h1></body></html>");

        request.setHandled(true);
    }
}
