/*
 * Created on 26-Oct-2004
 * Modified on 27-Jan-2009 by Dermot Cochran
 */

package ie.ucd.srg.logica.eplatform.servlet;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import ie.ucd.srg.logica.eplatform.ticket.*;

/**
 * @author Alan E. Morkan
 * @author Dermot Cochran
 */
public class UtilServlet extends HttpServlet {
    
    /**
     * is this necessary
     */
    private Ticket ticket;
    
    /**
     * 
     */
    public UtilServlet(){
    	//@ assert false;
    }
    
    /**
     * 
     */
    public void init(){
    	//@ assert false;
    }
    
    /**
     * 
     * @param request
     * @param response
     * @param s
     */
    //@ requires request != null;
    //@ requires response != null;
    //@ requires s != null;
    public void redirect(HttpServletRequest request, HttpServletResponse response, String s){
    	RequestDispatcher dispatcher = request.getRequestDispatcher(s);
    	try{
    		dispatcher.forward(request, response);
    	}catch(IOException ioe){
    		System.out.println(ioe);
    	}catch(ServletException se){
    		System.out.println(se);
    	}	
    }

    /**
     * @param request
     * @param response
     * @throws SerlvetException
     * @throws IOException
     */
    //@ requires request != null;
    //@ requires response != null;
    public void doGet(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException{
    	//@ assert false;
    }

    /**
     * @param s
     * @return
     */
    //@ requires s != null;
    //@ ensures \result != null;
    public String getProperty(String s){
    	//@ assert false;
    	return null;
    }

    /**
     * 
     * @param request
     * @return 
     */
    
    public Ticket getTicket(HttpServletRequest request){
    	//@ assert false;
    	return ticket;
    }
}
