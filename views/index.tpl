<!doctype html>
<title>Welcome to the {{ version }}</title>
<link rel="shortcut icon" href="/static/build.png">
<body bgcolor="black">
<font color="grey">
<img src="/static/build.png" align="left" height="64" width="64">
<img src="/static/build.png" align="right" height="64" width="64">
<center><strong>Welcome to the {{ version }}</center></strong><br><br>
<table style="width:500px" align="center">
<form method="POST">
  <tr>
    <td colspan='1.5'><strong>IP Address: </strong><input type="text" name="ip_addr"></td>
    <td colspan='1.5'><strong>Rack Pass: </strong><input type="text" name="ssh_pass"></td>
  </tr>
  <tr>
    <td><input type="checkbox" name="lsyncd" value="lsyncd">lsyncd</td>
    <td><input type="checkbox" name="varnishd" value="varnishd">varnish</td>
    <td><input type="checkbox" name="memcached" value="memcached">memcached</td>
  </tr>
      <tr>
        <td colspan='3'><center><input type="submit" value="Install the things!">&nbsp&nbsp
        <input type="reset" value="Clear Form"></center></td>
      </tr>
    </table>
</form>
<br><br><center><strong>Check the <a href="/status">Status</a> of a task</strong></center>
<span style="position: absolute; bottom: 5pt; left: 5pt;"><a href="https://github.com/zully/build" target="_blank">Build Tool</a></span>
<span style="position: absolute; bottom: 5pt; right: 5pt;"><a href="mailto:christopher.hidalgo@rackspace.com">Feedback?</a></span>
