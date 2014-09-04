#!/usr/bin/env python

#pip install ansible pyyaml jinja2 paramiko bottle
import urllib, json, helper, db
from bottle import Bottle, request, template, TEMPLATE_PATH
from tasks import install_stuff

from bottle import debug

app = Bottle(__name__)
debug(True)

TEMPLATE_PATH.insert(0,'/var/www/vhosts/build/views/')
VERSION='v0.23 beta'

@app.route('/status')
def status():
    # Return template of status
    data = db.read()
    return template('status', version=VERSION, data=data)

@app.route('/')
def index():
    # Return index template on GET or HEAD requests
    return template('index', version=VERSION)

@app.route('/', method=['POST'])
def do_cool_things():
    plays = []
    
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
        plays.append('{ role: IUS-repos, tags: ius-repos }')
        plays.append('apache2')
        plays.append('php5')
        plays.append('{ role: mysql, tags: mysql }')
        plays.append('{ role: phpmyadmin, tags: phpmyadmin }')
        plays.append('{ role: holland, tags: holland }')

    if lsyncd != 'None':
        plays.append(lsyncd)

    if memcached != 'None':
        plays.append(memcached)

    if varnishd != 'None':
        plays.append(varnishd)

    
    # write the playbook, then pass off to celery to run
    playbook = helper.write_playbook(plays)

    task = install_stuff.delay(ip_addr, sshpass, playbook)
    return template('answer', status='Job request received...', answer='Your Job ID: ' + str(task), version=VERSION)

if __name__ == '__main__':
    app.run()
