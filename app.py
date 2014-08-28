#!/usr/bin/env python

#pip install ansible pyyaml jinja2 paramiko bottle

import urllib, json, os, jinja2, re
from bottle import Bottle, request, template, TEMPLATE_PATH
from bottle import debug
from ansible.playbook import PlayBook
from ansible import callbacks
from ansible import utils

app = Bottle(__name__)
debug(True)

TEMPLATE_PATH.insert(0,'/var/www/vhosts/build/views/')
ANS_PATH='/var/www/vhosts/build/ansible/'

def install_stuff(user, ip_list, sshpass, pb_name): 
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    stats = callbacks.AggregateStats()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    pb = PlayBook(remote_user=user,
        remote_pass=sshpass,
        playbook=pb_name,
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        stats=stats,
        host_list=ip_list,
    )

    results = pb.run()
    return results

def input_validation(username, sshpass, ip_addr):
    # Check to make sure no fields were left blank
    if (sshpass == '' or username == '' or ip_addr == ''):
        return template('answer', answer='Please fill out all fields!', status='Error!')

    #Input validation
    pattern = r'[^\.0-9,]'
    if re.search(pattern, ip_addr):
        return template('answer', answer='Invalid IP!', status='Error!')

@app.route('/')
def index():
    # Return index template on GET or HEAD requests
    return template('index')

@app.route('/', method=['POST'])
def do_cool_things():
    # Collect all the information to make the server from the form fields
    sshpass = str(request.forms.get('ssh_pass'))
    username = str(request.forms.get('username'))
    ip_addr = str(request.forms.get('ip_addr'))
    lsyncd = str(request.forms.get('lsyncd'))
    memcached = str(request.forms.get('memcached'))
    varnish = str(request.forms.get('varnish'))

    input_validation(username, sshpass, ip_addr)
    ip_addr += ','

    if lsyncd != '':
        play = ANS_PATH + lsyncd

    results = install_stuff(username, ip_addr, sshpass, play)

    return template('answer', answer=str(results), status="Success!")

if __name__ == '__main__':
    app.run()
