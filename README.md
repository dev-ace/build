## Build Assistant

### DESCRIPTION:

Front-end User Interface is written in Python/Bottle.  Backend is a programatically driven agentless orchestration function written in Python that leverages the Ansbile API library and executes the chosen Ansible plays on a user specified server.  Ansible plays are executed asynchronously via rabbitmq/celery worker, and a mysql database of "In Progress" and "Complete" tasks with a status of either "Sucessful" or "Failed" is maintained.  User can query this database of task conditions via a status page.

### REQUIREMENTS:

- Python 2.7+
- Ansible 1.6
- UWSGI
- Celery
- MySQL 5.5
- RabbitMQ
- Nginx

### USAGE:

This app will be used to speed up the installation of various services during a Cloud "build-out"

### TO DO:

* - [x] UI
  * - [x] Basic Functionality
  * - [x] Status Page of Tasks
  * - [ ] Make it pretty
  * - [ ] Testing
* - [x] General Functionality
  * - [x] Use rack user
  * - [x] Error Checking
    * - [x] Some error checking in place, much more needed
  * - [x] Unique playbook name writen in realtime
  * - [x] Threading for scalability
    * - [x] begun passing work to celery
  * - [ ] Testing
* - [x] Playbooks & Plays
  * - [x] lsyncd
    * - [x] Testing - Basic (More thorough testing needed)
  * - [x] varnishd
    * - [x] Testing - Basic (More thorough testing needed)
  * - [x] memcached
    * - [x] Testing - Basic (More thorough testing needed)
  * - [x] LAMP
    * - [x] Testing - This is the most vetted play (forked from other repo)

A more comprehensive list will be added as warranted.

### LICENSE:

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
