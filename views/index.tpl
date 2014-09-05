<!doctype html>
<title>Welcome to the Build Assistant {{ version }}</title>
<link rel="shortcut icon" href="/static/build.png">
<body bgcolor="black">
<font color="grey">
<img src="/static/build.png" align="left" height="64" width="64">
<img src="/static/build.png" align="right" height="64" width="64">
<center><strong>Welcome to the Build Assistant {{ version }}</center></strong><br><br>
<table align=center width=50%>
<form method="POST">
  <tr>
    <td align=center><strong>IP Address: </strong><input type="text" name="ip_addr"></td>
    <td align=center><strong>Rack Pass: </strong><input type="password" name="ssh_pass"></td>
  </tr>
  <tr>
    <td align=center><input type="checkbox" name="lamp" value="lamp">LAMP</td>
    <td align=center><input type="checkbox" name="varnishd" value="varnishd">varnish</td>
  </tr>
  </tr>
    <td align=center><input type="checkbox" name="memcached" value="memcached">memcached</td>
    <td align=center><input type="checkbox" name="lsyncd" value="lsyncd">lsyncd</td>
  </tr>
  <tr>
    <td><br /></td>
  </tr>
  <tr>
    <td colspan='2' align=center>
      <input type="submit" value="Install the things!">
     <input type="reset" value="Clear Form"></form>
    </td>
  </tr>
  <tr>
    <td><br /></td>
  </tr>
  <tr>
    <td colspan='2' align=center><button onClick="window.location.href='/status'">Status</button></td>
  </tr>
</table>
<span style="position: absolute; bottom: 5pt; left: 5pt;"><a href="https://github.com/zully/build" target="_blank">Build Assistant</a></span>
<span style="position: absolute; bottom: 5pt; right: 5pt;"><a href="mailto:christopher.hidalgo@rackspace.com">Feedback?</a></span>
