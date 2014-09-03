import re, uuid

ANS_PATH='/var/www/vhosts/build/ansible/'

## Check various types of input for correctness
def input_validation(sshpass, ip_addr):
    # Check to make sure no fields were left blank
    if (sshpass == '' or ip_addr == ''):
        return 'Please fill out all fields!'

    #Input validation
    pattern = r'[^\.0-9,]'
    if re.search(pattern, ip_addr):
        return 'Invalid IP!'
    return 'success'

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
