import re
import sqlite3

html_code = '''
<form name="theForm" method="post" action="/save_job">    
<table border="1" width="98%" cellspacing="0" align="center" style="border-collapse: collapse" bordercolor="#CCCCCC">
	 <tbody><tr>
	  <td bgcolor="#45818e" align="center" height="20" width="49%"><font color="#FFFFFF" face="Verdana"><b>Moving From</b></font></td>
	  <td bgcolor="#45818e" align="center" height="20" width="49%"><font color="#FFFFFF" face="Verdana"><b>Moving To</b></font></td>
	</tr>
	 <tr>
	  <td valign="top" width="49%">
	  <table border="0" align="center" width="339" style="border-collapse: collapse;line-height:23px;" bordercolor="#111111">
	   <tbody><tr>
		<td width="79" height="19"><font size="2" face="Arial" color="#0000FF">Customer:<font color="#FF0000">*</font></font></td>
		<td width="256" colspan="3" height="19">
        <input id="txtSNAME" type="text" autocomplete="off" name="SNAME" size="30" style="background-color: #FFFFCC; font-size:9pt" value="" tabindex="1"></td>
	  </tr>	  
	   <tr>
		<td width="79" height="21"><font size="2" face="Arial">Address:</font></td>
		<td width="256" colspan="3" height="21"><input type="text" name="SADD1" size="30" style="font-size: 9pt" value="" tabindex="2"></td>
	  </tr>
	   <tr>
		<td width="79" height="19">&nbsp;</td>
		<td width="256" colspan="3" height="19"><input type="text" name="SADD2" size="30" style="font-size: 9pt" value="" tabindex="3"></td>
	  </tr>
	   <tr>
		<td width="79" height="19"><font face="Arial" size="2">Location:</font></td>
		<td width="95" height="19">
		 <select size="1" name="SLEVEL" tabindex="4" style="font-size: 9pt">
		   <option selected="">                    </option>
		   <option>House</option>
           <option>Townhouse</option>
           <option>Apartment</option>
           <option>Condo</option>           
		   <option>Storage</option>
		   <option>Mobile Home</option>
		   <option>Garage</option>
		   <option>Warehouse</option>
		   <option>Office</option>
		   <option>Military Base</option>		   
		   <option value=""></option>
		  </select></td>
		<td width="42" height="19"><font face="Arial" size="2">Level:</font></td>
		<td width="115" height="19">
	    <select size="1" name="SSUBLEVEL" tabindex="5" style="font-size: 9pt">
		   <option selected=""></option>
		   <option>Ground</option>
		   <option>Elevator</option>
		   <option>Stairs</option>
		   <option>Basement</option>
		   <option>Pod</option>		   		   
		   <option value=""></option>
		  </select>		
		</td>
	  </tr>
	   <tr>
		<td width="79" height="19"><font face="Arial" size="2">Floor:</font></td>
		<td width="95" height="19"><input type="text" autocomplete="off" name="SFLOOR" size="2" style="font-size: 9pt" value="" maxlength="3" tabindex="6"></td>
		<td width="42" height="19"><font face="Arial" size="1">APT. #</font></td>
		<td width="115" height="19"><input type="text" autocomplete="off" name="SAPT" size="2" style="font-size: 9pt" value="" tabindex="7"></td>
		</tr>
	   <tr>
		<td width="79" height="19"><font face="Arial" size="2">City:</font></td>
		<td width="95" height="19"><input type="text" name="SCITY" size="10" style="font-size: 9pt" value="" tabindex="8"></td>
		<td width="42" height="19"><font face="Arial" size="2">State:</font></td>
		<td width="115" height="19"><input type="text" name="SSTATE" size="2" style="font-size: 9pt" value="" tabindex="9"></td>
	  </tr>
	   <tr>
		<td height="19" width="79"><b><a href="javascript:openCityPopup()" ><font size="2" face="Arial" color="#0000FF">Zip Code:</font></a></b><font color="#FF0000">*</font></td>
		<td height="19" colspan="3" width="256">
     <!--   <input type="text" id="city-name" name="SZIP" style="width:50px;background-color:#FFFFCC;font-size:9pt" value="" tabindex="10" size="20"> -->
		<input type="text" id="zipPicker" name="zipcode" style="width:50px;background-color:#FFFFCC;font-size:9pt" value="" tabindex="10" size="20" >
		
		
		</td>
		
	  </tr>
   
	   
	   <tr>
		<td width="79" height="19"><font size="2" face="Arial" color="#0000FF">Phone:</font><font color="#FF0000">*</font></td>
		<td width="256" colspan="3" height="19">
        <input type="text" name="STELH" size="25" style="background-color: #FFFFCC; font-size:9pt" value="" tabindex="12"></td>
	  </tr>
	   <tr>		
		<td width="79" height="19"><font face="Arial" size="2">Phone:</font></td>
		<td width="256" colspan="3" height="19">
        <input type="text" name="STELO" size="25" value="" tabindex="13" style="font-size: 9pt"></td>
	  </tr>
	   <tr>
		<td width="79" height="19"><font size="2" face="Arial" color="#0000FF">Email:</font><font color="#FF0000">*</font></td>
		<td width="256" colspan="3" height="19"><input type="text" autocomplete="off" name="EMAIL" size="25" value="" tabindex="14" style="background-color: #FFFFCC; font-size:9pt"></td>
	  </tr>
	   <tr>
		<td width="79" height="19"><font size="2" face="Arial">Proxy:</font></td>
		<td width="256" colspan="3" height="19"><input type="text" autocomplete="off" name="SPROXY" size="30" style="font-size:9pt" value="" tabindex="15"></td>
	  </tr>	  
     </tbody></table>	  
	  </td>
	  <td valign="top" width="49%">
	 <table border="0" align="center" width="340" cellspacing="0" style="border-collapse: collapse;line-height:23px;">
	  <tbody><tr>
	   <td width="84" height="19"><font size="2" face="Arial" color="#000000">Customer:</font></td>
	   <td width="252" colspan="3" height="19"><input type="text" autocomplete="off" name="RNAME" size="30" value="" tabindex="16" style="font-size: 9pt"></td>
	 </tr>	 
	  <tr>
	   <td width="84" height="19"><font size="2" face="Arial" color="#000000">Address:</font></td>
	   <td width="252" colspan="3" height="19"><input type="text" name="RADD1" size="30" style="font-size: 9pt" value="" tabindex="17"></td>
	 </tr>
	  <tr>
	   <td width="84" height="19">&nbsp;</td>
	   <td width="252" colspan="3" height="19"><input type="text" name="RADD2" size="30" style="font-size: 9pt" value="" tabindex="18"></td>
	 </tr>
	  <tr>
	   <td width="84" height="19"><font face="Arial" size="2">Location:</font></td>
	   <td width="91" height="19">
       <select size="1" name="RLEVEL" tabindex="19" style="font-size: 9pt">
		<option selected="">                    </option>
		 <option>House</option>
         <option>Townhouse</option>
         <option>Apartment</option>
         <option>Condo</option>         
	     <option>Storage</option>
	     <option>Mobile Home</option>
	     <option>Garage</option>
		 <option>Warehouse</option>
		 <option>Office</option>
		 <option>Military Base</option>		 
	     <option value=""></option>
	   </select></td>
	   <td width="45" height="19"><font face="Arial" size="2">Level:</font></td>
	   <td width="112" height="19">
	    <select size="1" name="RSUBLEVEL" tabindex="20" style="font-size: 9pt">
		   <option selected=""></option>
		   <option>Ground</option>
		   <option>Elevator</option>
		   <option>Stairs</option>
		   <option>Basement</option>
		   <option>Pod</option>		   		   
		   <option value=""></option>
		  </select>	   
	   </td>
	  </tr>
	   <tr>
		<td width="84" height="19"><font face="Arial" size="2">Floor:</font></td>
		<td width="91" height="19"><input type="text" autocomplete="off" name="RFLOOR" size="2" style="font-size: 9pt" value="" maxlength="3" tabindex="21"></td>
		<td width="45" height="19"><font face="Arial" size="1">APT. #</font></td>
		<td width="112" height="19"><input type="text" autocomplete="off" name="RAPT" size="2" style="font-size: 9pt" value="" tabindex="22"></td>
		</tr>
      <tr>
		<td width="84" height="19"><font face="Arial" size="2">City:</font></td>
		<td width="91" height="19"><input type="text" name="RCITY" size="10" style="font-size: 9pt" value="" tabindex="23"></td>
		<td width="45" height="19"><font face="Arial" size="2">State:</font></td>
		<td width="112" height="19"><input type="text" name="RSTATE" size="2" style="font-size: 9pt" value="" tabindex="24"></td>
	  </tr>
	   <tr>
		<td height="19" width="84"><b><a href="javascript:FindZip(&#39;RZIP&#39;)"><font size="2" face="Arial" color="#0000FF">Zip Code:</font></a></b><font color="#FF0000">*</font></td>
		<td height="19" colspan="3" width="252">
        <input type="text" name="RZIP" style="width:50px;background-color:#FFFFCC;font-size:9pt" value="" tabindex="25" size="20"></td>
	  </tr>
   
	   	   
	   <tr>
		<td width="84" height="19"><font size="2" face="Arial" color="#0000FF">Cell Phone:</font></td>
		<td width="252" colspan="3" height="19"><input type="text" name="RTELH" size="25" style="font-size: 9pt" value="" tabindex="27"></td>
	  </tr>
	   <tr>
		<td width="84" height="19"><font face="Arial" size="2">Phone:</font></td>
		<td width="252" colspan="3" height="19"><input type="text" name="RTELO" size="25" style="font-size: 9pt" value="" tabindex="28"></td>
	  </tr>
	  

	   <tr>
		<td width="84" height="19"><font face="Arial" size="2">Fax:</font></td>
		<td width="252" colspan="3" height="19"><input type="text" name="SFAX" size="25" style="font-size: 9pt" value="" tabindex="29"></td>
	  </tr>
	  

	   <tr>
		<td width="79" height="19"><font size="2" face="Arial">Proxy:</font></td>
		<td width="256" colspan="3" height="19"><input type="text" autocomplete="off" name="RPROXY" size="30" style="font-size:9pt" value="" tabindex="30"></td>
	  </tr>	  
     </tbody></table>	  
	  </td>
	</tr>
</tbody></table>
 <br>
<table border="1" width="98%" cellspacing="0" align="center" style="border-collapse: collapse" bordercolor="#CCCCCC">
  <tbody><tr>
	<td valign="top" width="67%">
<table border="0" width="100%" align="center" cellspacing="0" style="border-collapse: collapse;line-height:30px;" bordercolor="#111111" cellpadding="0">
 
 
  <tbody><tr>
	<td width="38%"><font face="Arial" size="2" color="#0000FF">Expected Move Date</font><font color="#FF0000">:*</font></td>
	<td width="30%">
	


<input type="text" id="datepicker" name="date" size="13" style="background-color:#FFFFCC;text-align:center;font-weight:bold;" tabindex="33">


    </td>
	<td width="27%"><font face="Arial" size="2">Time:
	<input type="text" name="LBOOKTME" size="10" value="" style="cursor:pointer; font-size:9pt" onclick="window.open(&#39;/wc.dll?mputil~timetablewc~theForm~LBOOKTME&#39;,&#39;EANITHING&#39;,&#39;toolbar=no,location=no,directories=no,status=no,menubar=no,resizable=no,copyhistory=no,scrollbars=yes,width=650,height=600&#39;)" tabindex="34" maxlength="20"></font></td>
 </tr>

 
  <tr>
    <td width="38%"><font face="Arial" size="2" color="#0000FF">How did you hear about us?</font><font color="#FF0000">*</font></td>
    <td width="62%" colspan="2">
	<select size="1" name="REF" style="background-color: #FFFFCC;" tabindex="35">
	  <option>                                        </option>
	   

	  <option>FACEBOOK                                </option>
		

	  <option>GOOGLE                                  </option>
		

	  <option>USED PREVIOUSLY                         </option>
		

	  <option>WEBSITE                                 </option>
		

		</select>    
    </td>
 </tr>

 

 
     <tr>
	  <td width="38%"><font face="Arial" size="2" color="#0000FF">Move Size:</font></td>
	  <td width="62%" colspan="2">     
		<select size="1" name="ROOMID" tabindex="36" style="font-size:9pt;">
		  <option selected="">&lt; Select Move Size &gt;</option>		  
	   	  

	      <option value="102405">Few Items</option>
		  

	      <option value="102406">Studio</option>
		  

	      <option value="102407">One Bedroom</option>
		  

	      <option value="102408">Two Bedrooms</option>
		  

	      <option value="102409">Three Bedrooms</option>
		  

	      <option value="102410">Four Bedrooms</option>
		  

	      <option value="102411">Five Bedrooms</option>
		  

	      <option value="102412">Six Bedrooms</option>
		  

	      <option value="102413">20 ft. Container</option>
		  

	      <option value="102414">40 ft. Container</option>
		  

	      <option value="102415">Office Move</option>
		  

	    </select>
	  </td>
	  </tr>


  </tbody></table>	  
	  </td>
	  <td valign="top" width="32%">
  <table border="0" width="100%" cellspacing="1" style="border-collapse: collapse;line-height:20px;font-family:Arial;font-size:10pt;" bordercolor="#111111" cellpadding="2">
   

  
  
   <tbody><tr>
	<td><b>Type of Move: <font color="red">Residential</font><br>
    &nbsp;<input type="radio" name="RC" value="R" checked="" tabindex="37">Residential<br>	
	&nbsp;<input type="radio" name="RC" value="C" tabindex="38">Commercial
  
<br>&nbsp;<input type="radio" name="RC" value="M" tabindex="39">Military
</b></td>
  </tr>
</tbody></table>	  
	  </td>
	</tr>
</tbody></table>
 <br>
<table border="0" width="80%" align="center">
  <tbody><tr>
	<td width="100%"><b><font color="#FF0000"> </font></b></td>
 </tr>
</tbody></table>
'''

names_tags = re.findall(r'name="([^"]*)"', html_code)

for tag in names_tags:
    print(tag)


conn = sqlite3.connect('granot.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Generate the CREATE TABLE statement dynamically based on the elements in names_tags
create_table_query = "CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY AUTOINCREMENT, {})".format(', '.join('{} TEXT'.format(column) for column in set(names_tags[1:])))

# Execute the CREATE TABLE statement
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()
