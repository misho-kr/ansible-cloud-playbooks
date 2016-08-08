Base Cloud Playbook
===================

Use [cloud](../cloud.yml) playbook as template and example of how to build new Ansible playbooks. Make a copy of it and then add new playbook roles and tasks.

### Virtual Machine Tags

New virtual machines are created with a set of descriptive tags. They are used to distinguish one set of machines from another. This feature allows to execute playbooks without having to create and update inventory files, which with cloud-provisioned resources can be quite a headache.

The base playbook defines one single tag:

* __provisioner__ = "Ansible"

New playbook should extend the set of tags to make the new virtual machines easily identifiable.

### Inventory file

The playbook will create create or update inventory file (for example _cloud.aws_) when it is invoked to provision cloud resources. It is possible (but not mandatory) to use this inventory file to identify and target the cloud virtual machines in subsequent invocations of the playbook. It is a shortcut to avoid the query to the cloud provider to search for virtual machines by tags.

### Usage

This playbook can be used on virtual machines created with other playbooks, so long as the set of tags defined in the derived playbook is a superset of the tags in the base playbook. Another option is to use the generated inventory file.

* Test connectivity to virtual machines

```bash
$ ansible-playbook cloud.yml -i cloud.aws -t ping

```

* Reduce their number (all the way to zero)

```bash
$ ansible-playbook cloud.yml -e vm_count=1

```

### Playbook tags

Convenient to restict the execution to a subset of the playbook roles. Without tags the playbook run will execute all roles.

* __vm__ -- create or destroy virtual machines
* __min-install__ -- install Python2 (required ro run Ansible playbook) and small set of config files
* __ping__ -- test connectivity with Ansible (a bit more involved than simple _ping_)

### Playbook variables

* __cloud__ -- cloud provider to use, initially only _aws_ is supported
* __vm_count__ -- number of VMs to create
* AWS-specific variables -- look at [aws.yml](../roles/provision-cloud/vars/aws/yml)

### ToDo

* Expland the playbook to support more cloud providers