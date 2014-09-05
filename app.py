#!/usr/bin/env python

#pip install ansible pyyaml jinja2 paramiko bottle
import urllib, json, helper, db
from bottle import Bottle, request, template, TEMPLATE_PATH
from tasks import install_stuff

from bottle import debug

app = Bottle(__name__)
debug(True)

TEMPLATE_PATH.insert(0,'/var/www/vhosts/build/views/')
VERSION='v0.0.31 beta'

@app.route('/status')
def status():
    # Return template of status
    data = db.read_completed()
    prog = db.read_in_progress()
    return template('status', version=VERSION, data=data, prog=prog)

@app.route('/')
def index():
    # Return index template on GET or HEAD requests
    return template('index', version=VERSION)

@app.route('/', method=['POST'])
def do_cool_things():
    plays = []
    req_list = []    
    # Collect all the information to make the server from the form fields
    sshpass = str(request.forms.get('ssh_pass'))
    ip_addr = str(request.forms.get('ip_addr'))
    lsyncd = str(request.forms.get('lsyncd'))
    memcached = str(request.forms.get('memcached'))
    varnishd = str(request.forms.get('varnishd'))
    lamp = str(request.forms.get('lamp'))

    test_results = helper.input_validation(sshpass, ip_addr)
    if test_results != 'success':
        return template('answer', answer=test_results, status='Error!', version=VERSION)
    ip_addr += ','

    # Test which plays were selected
    if lamp != 'None':
        req_list.append('LAMP')
    if lsyncd != 'None':
        req_list.append('lsyncd')
    if memcached != 'None':
        req_list.append('memcached')
    if varnishd != 'None':
        req_list.append('varnishd')
    
    # Pass off to celery to run
    task = install_stuff.delay(ip_addr, sshpass, req_list)

    return template('answer', status='Job request received...', answer='Your Job ID: ' + str(task), version=VERSION)

if __name__ == '__main__':
    app.run()
