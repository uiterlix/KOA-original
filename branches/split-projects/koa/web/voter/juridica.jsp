<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<%@page import="ie.ucd.srg.koa.controller.client.ClientManager"%>
<%@page import="ie.ucd.srg.koa.constants.SystemState"%>
<%@page import="ie.ucd.srg.koa.constants.ComponentType"%>
<%@page session="false" %>
<%
	response.setHeader("Pragma", "no-cache"); //http1.0
	response.setHeader("Cache-Control", "no-cache"); //http1.1
%>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<META name="GENERATOR" content="IBM WebSphere Studio">
<META http-equiv="Pragma" content="no-cache"/>
<META http-equiv="Expires" content="-1"/>
<LINK href="KiezerWeb.css" rel="stylesheet" type="text/css">
<TITLE>European Parliament Elections 2004</TITLE>
</head>

<%
	String sCurrentState = ClientManager.getLocalState (ComponentType.WEB);
	String sElectionText = SystemState.getWebTextForState (sCurrentState);	
%>

<body>

        <table width="725" border="0" align="center" cellpadding="0" cellspacing="0">
            <tr>
                <td colspan="3">              <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td width="640" height="57" bgcolor="#6699CC">
<div align="center"><font color="#FFFFFF" size="4" face="Arial, Helvetica, sans-serif"><strong>European Parliament Elections 2004
                      </strong></font></div></td>
                </tr>
              </table></td>
            </tr>
            <tr valign="top">
                <td width="3%" align="left"><img src="images/blueline_3.gif" width="1" height="380"></td>
                <td width="94%" valign="top">
                <div align="center">&nbsp;
                <table width="100%" border="0" cellpadding="3">
                    <tr>
                        <td height="270">
                        <p align="left"><font size="2">It is illegal for on name of another one in the poll to take part (Article 128 Statute book of criminal law)</font></p>
                  <p><font size="2">Tevens is het strafbaar om in meer dan &eacute;&eacute;n lidstaat van de Europese Unie deel te nemen aan de stemming voor de verkiezing voor de leden van het Europees Parlement.
                    </font><br>
                        </p>
<%
	if (sElectionText != null) 
	{
%>
                        <p><b><%= sElectionText %></b></p>           
<%
    } else {
%>                        
                        <p><b>&nbsp;</b></p>           
<%
    } 
%>

                        <p>&nbsp;</p>
                        <p>&nbsp;</p>
                        <p>&nbsp;</p>
                        <p>&nbsp;</p>
                        </td>
                    </tr>
                </table>
                <table width="100%" border="0" cellpadding="3">
                    <tr>
                      <td width="173" height="38"><a href="uitleg.jsp"><img src="images/terug_2.gif" width="108" height="46" border="0" alt="press on this to return to the first page"></a></td>
                      <td>&nbsp;</td>
<%
	if (SystemState.OPEN.equals(sCurrentState)) 
	{
%>                
                        <td>
                        <div align="right"><a href="identification.jsp<%--Login--%>"><img src="images/start_2.gif" width="108" height="46" border="0" alt="click here if you want vote"></a></div>
                        </td>
<%
	}
%>                
                    </tr>
                </table>
                </div>
                </td>
                <td width="3%" align="right"><img src="images/blueline_3.gif" width="1" height="380"></td>
            </tr>
            <tr valign="top">
                <td height="1" colspan="3"><img src="images/horizontalline_2.gif" width="726" height="1"></td>
            </tr>
            <tr valign="top">
                <td colspan="3">
                <div align="center">
                <H2>The responsibility for this site rests at the Ministry of the Interior and Kingdom Relations</H2>
                </div>
                </td>
            </tr>
        </table>

</body>
<HEAD>
<META http-equiv="Pragma" content="no-cache"/>
<META http-equiv="Expires" content="-1"/>
</HEAD>
</html>
