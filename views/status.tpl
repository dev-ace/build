<!doctype html>
<title>Welcome to the {{ version }}</title>
<link rel="shortcut icon" href="/static/build.png">
<body bgcolor="black">
<font color="grey">
<img src="/static/build.png" align="left" height="64" width="64">
<img src="/static/build.png" align="right" height="64" width="64">
<center><strong>Welcome to the {{ version }}</center></strong><br><br>

                %if data:
                  % for row in data:
                  <table align=center width=80%>
                    <tr>
                      <td width="30%">ID: {{ row[0] }}</td>
                      <td width="15%">Status: 
                    %if row[1] == 'SUCCESS':
                      <font color='green'>
                    %else:
                      <font color='red'>
                    %end
                      {{ row[1] }}</font></td>
                      <td width="20%">Date/Time: {{ row[2] }}</td>
                    %if len(row) >= 4:
                      <td width="20%">IP: {{ row[3] }}</td>
                    %end
                    %if len(row) >= 5:
                      <td width="15%">Failures: {{ row[4] }}</td>
                    %end
                    </tr>
                  </table>
                  <hr>
                  %end
                %end
                %if not data:
                  <h3><center>There are no processes to display</center></h3>
                %end

<center><FORM><INPUT Type="button" VALUE="Go Back" onClick="history.go(-1);return true;"></FORM></center>

<span style="position: absolute; bottom: 5pt; left: 5pt;"><a href="https://github.com/zully/build" target="_blank">Build Tool</a></span>
<span style="position: absolute; bottom: 5pt; right: 5pt;"><a href="mailto:christopher.hidalgo@rackspace.com">Feedback?</a></span>
