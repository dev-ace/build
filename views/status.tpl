<!doctype html>
<title>Welcome to the Build Assistant {{ version }}</title>
<link rel="shortcut icon" href="/static/build.png">
<body bgcolor="black">
<font color="grey">
<img src="/static/build.png" align="left" height="64" width="64">
<img src="/static/build.png" align="right" height="64" width="64">
<center><strong>Welcome to the Build Assistant {{ version }}</center></strong><br><br>

                <center><strong><font color='green'><h2>In Progress</h2></center></strong></font><hr>
                %if prog:
                  % for row in prog:
                  <table align=center width=80%>
                  <tr>
                    <td width="40%">ID: {{ row[0] }} </td>
                    <td width="20%">IP: {{ row[1] }} </td>
                    <td width="40%">Tasks: {{ row[2] }} </td>
                  </tr>
                  </table>
                  <hr>
                  %end
                %else:
                  <table align=center width=80%><tr><td><center><h3>No tasks to display</h3></center></td></tr></table><hr>
                %end
                <br /><br /><br />



                <center><strong><font color='green'><h2>Completed < 60 Min</h2></center></strong></font><hr>
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
                  <table align=center width=80%><tr><td><center><h3>No tasks to display</h3></center></td></tr></table><hr>
                %end

<center><button onClick="window.location.href='/'">Main Page</button></center>

<span style="position: absolute; bottom: 5pt; left: 5pt;"><a href="https://github.com/zully/build" target="_blank">Build Assistant</a></span>
<span style="position: absolute; bottom: 5pt; right: 5pt;"><a href="mailto:christopher.hidalgo@rackspace.com">Feedback?</a></span>
