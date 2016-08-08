Software Development Environment
================================

### Purpose

Use [dev-machine](../dev-machine.yml) playbook to create virtual machine with preinstalled packages for sofwtare development.

### Virtual Machine Tags

All virtual machines created by this playbok will have these tags:

| tag name | value |
| -------- | ----- |
| name | Development machine |
| purpose | Work on home assignments |
| provisioner | Ansible |

### Inventory file

The playbook will create create or update inventory file (for example _dev.aws_) for later use. See [cloud](loud.md) for explanation.

### Usage

* Create (or update) virtual machine for C++ development

```bash
$ ansible-playbook dev-machine.yml -e install=cpp

```

* Install SublimeText on that virtual machine

```bash
$ ansible-playbook -i dev.aws dev-machine.yml -e install=sublime

```

### Playbook tags

Convenient to restict the execution to a subset of the playbook roles. Without tags the playbook run will execute all roles.

* __vm__ -- create or destroy virtual machines
* __min-install__ -- install Python2 (required ro run Ansible playbook) and small set of config files
* __install__ -- install one of several supported environments

#### Dev environments

See the __install__ variable (see the example above) to one of the below values to direct the playbook to set up a specific environment:

* __sublime__ -- download and install [SublimeText 2](https://www.sublimetext.com)
* __cpp-dev__ -- install g++ compiler
* __ruby-dev__ -- install [Ruby On Rails](http://rubyonrails.org)

### Playbook variables

* __cloud__ -- cloud provider to use, initially only _aws_ is supported
* __vm_count__ -- number of VMs to create