Virtual Machines in the cloud
=============================

[Ansible playbooks](https://docs.ansible.com/playbooks.html) to automate the creation of virtual machines on public clouds.

No need for vendor-specific UIs or multiple command-line tools. Define the cloud provider, set desired virtual machines, and run the playbook. Plenty of customization options.

Supported cloud providers: [aws](https://aws.amazon.com), [gce](https://cloud.google.com) (work in progress)

There are other solutions to do that, like [Teraform](https://www.terraform.io). This is my experiment, implemented with [Ansible cloud modules](http://docs.ansible.com/ansible/list_of_cloud_modules.html).

## Ansible playbooks

* [Cloud](cloud.yml) / [docs](docs/cloud.md) -- showcase of how to create virtual machines in the cloud
* [Dev Machine](dev-machine.yml) / [docs](docs/dev-machine.md) -- software development environment (c++, ruby, etc.)
* [Serf](serf.yml) / [docs](docs/serf.md) -- cluster of [Serf agents](https://www.serf.io/docs/index.html)

### Playbook execution

```bash
$ ansible-playbook cloud.yml -e vm_count=1

PLAY [localhost] ***************************************************************

TASK [provision-cloud : include_vars] ******************************************
ok: [localhost]

...

TASK [ping] ********************************************************************
ok: [10.179.131.227]

PLAY RECAP *********************************************************************
10.179.131.227             : ok=4    changed=0    unreachable=0    failed=0
localhost                  : ok=10   changed=1    unreachable=0    failed=0
```

Optional arguments -- defined in the __vars__ section of the playbook, or passed to the playbook on the command line:

* __cloud__ -- cloud provider to use, initially only _aws_ is supported
* __vm_count__ -- number of VMs to create

### Playbook actions

* Queries the selected cloud provider to get current list of VMs
* Creates VMs as necessary (or destroys) and adds them to the inventory under the __cloud__ group
* Genereates static inventory file
* Checks connectivity to each VM

### Preparation for execution

1. Inventory file not needed (but will be created for convenience)
1. Specify the cloud provider and desired number of VMs (see _Playbook execution_)
, or on the command line
1. Optionally, expand the playbook with your provisioning and configuration steps

Provisioning cloud infrastructure requires credentials to be passed to the playbook. Here is how to do that:

* For AWS, set these environment variables
 * AWS_ACCESS_KEY_ID
 * AWS_SECRET_ACCESS_KEY
 * AWS_SECURITY_TOKEN (only if required for the account to which the above pair of keys belongs)

### Limitation

You can not create VMs on multiple could providers in the same playbook execution. But you can run the playbook multiple times, each time with different __cloud__ parameter.