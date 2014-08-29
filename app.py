#!/usr/bin/env python

#pip install ansible pyyaml jinja2 paramiko bottle

import urllib, json, os, jinja2, re, uuid
from bottle import Bottle, request, template, TEMPLATE_PATH
from bottle import debug
from ansible.playbook import PlayBook
from ansible import callbacks
from ansible import utils

app = Bottle(__name__)
debug(True)

TEMPLATE_PATH.insert(0,'/var/www/vhosts/build/views/')
ANS_PATH='/var/www/vhosts/build/ansible/'

## programatically call the ansible playbook
def install_stuff(ip_list, sshpass, pb_name): 
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    stats = callbacks.AggregateStats()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    pb = PlayBook(remote_user='rack',
        remote_pass=sshpass,
        playbook=pb_name,
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        stats=stats,
        host_list=ip_list,
    )

    results = pb.run()
    return results

## Check various types of input for correctness
def input_validation(sshpass, ip_addr):
    # Check to make sure no fields were left blank
    if (sshpass == '' or ip_addr == ''):
        return template('answer', answer='Please fill out all fields!', status='Error!')

    #Input validation
    pattern = r'[^\.0-9,]'
    if re.search(pattern, ip_addr):
        return template('answer', answer='Invalid IP!', status='Error!')
    return

## Write the plays that were taken from user input to a file
def write_playbook(plays):
    filename = ANS_PATH + str(uuid.uuid1())
    f = open(filename, 'w')
    f.write('---\n')
    f.write('- hosts: all\n')
    f.write('  user: rack\n')
    f.write('  sudo: yes\n')
    f.write('  roles:\n')
    for play in plays:
        f.write('    - ' + play + '\n')
    f.close()
    
    return filename

@app.route('/')
def index():
    # Return index template on GET or HEAD requests
    return template('index')

@app.route('/', method=['POST'])
def do_cool_things():
    plays = []
    
    # Collect all the information to make the server from the form fields
    sshpass = str(request.forms.get('ssh_pass'))
    ip_addr = str(request.forms.get('ip_addr'))
    lsyncd = str(request.forms.get('lsyncd'))
    memcached = str(request.forms.get('memcached'))
    varnishd = str(request.forms.get('varnishd'))

    input_validation(sshpass, ip_addr)
    ip_addr += ','

    # Test which plays were selected
    if lsyncd != 'None':
        plays.append(lsyncd)

    if memcached != 'None':
        plays.append(memcached)

    if varnishd != 'None':
        plays.append(varnishd)
    
    # call the playbook on a server, then delete it
    playbook = write_playbook(plays)
    results = install_stuff(ip_addr, sshpass, playbook)
    os.remove(playbook)

    return template('answer', answer=results, status="Success!")

if __name__ == '__main__':
    app.run()
