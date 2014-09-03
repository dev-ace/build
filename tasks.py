from celery import Celery
import urllib, json, os, jinja2
from ansible.playbook import PlayBook
from ansible import callbacks
from ansible import utils

app = Celery('tasks', backend='amqp://guest@localhost//', broker='amqp://guest@localhost//')

@app.task
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
    os.remove(pb_name)

    return results
