Cluster of Serf Agents
======================

Note: Work in progress, at present only __systemd__ (Fedora) systems are supported.

### Purpose

Use [serf](../serf.yml) playbook to create a cluser of [serf agents](https://www.serf.io/docs/index.html) running on cloud virtual machines.

### Virtual Machine Tags

All virtual machines created by this playbok will have these tags:

| tag name | value |
| -------- | ----- |
| name | Serf cluster |
| purpose | Experiment with Serf |
| provisioner | Ansible |

### Inventory file

The playbook will create create or update inventory file (for example serf.aws_) for later use. See [cloud](cloud.md) for explanation.

### Usage

* Create 3 virtual machines with Serf agents

```bash
$ ansible-playbook serf.yml -e vm_count=3

```

* Reduce their number to 2

```bash
$ ansible-playbook -i serf.aws serf.yml -e vm_count=2

```

### Playbook tags

Convenient to restict the execution to a subset of the playbook roles. Without tags the playbook run will execute all roles.

* __vm__ -- create or destroy virtual machines
* __min-install__ -- install Python2 (required ro run Ansible playbook) and small set of config files
* __serf__ -- install Serf agent

### Playbook variables

* __cloud__ -- cloud provider to use, initially only _aws_ is supported
* __vm_count__ -- number of VMs to create

### ToDo

* Enable encryption of the communication channel between Serf agents
* Add support for __upstart__ (Ubuntu pre-15.x) and __init.d__ (RedHat) systems