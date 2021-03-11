Create cloud virtual machines with [Ansible](https://docs.ansible.com/playbooks.html)
============================================

Pure Ansible playbooks, no need for cloud provider-specific UIs or command-line tools:

1. Use one of the ready-to-use playbooks or create new one from template
1. Set the cloud provider and desired number of virtual machines (otional)
1. Run the playbook

Supported cloud providers: [aws](https://aws.amazon.com), [gce](https://cloud.google.com) (work in progress).

There are other cloud provisioning solutions, like [Teraform](https://www.terraform.io). This is my experiment with [Ansible cloud modules](http://docs.ansible.com/ansible/list_of_cloud_modules.html).

## Ansible playbooks

* [Cloud](cloud.yml) / [docs](docs/cloud.md) -- showcase of how to create virtual machines in the cloud
* [Dev Machine](dev-machine.yml) / [docs](docs/dev-machine.md) -- software development environment (c++, ruby, etc.)
* [Serf](serf.yml) / [docs](docs/serf.md) -- cluster of [Serf agents](https://www.serf.io/docs/index.html)

#### Configuration

Parameters that can be defined in the __vars__ section of the playbook, or passed as command line arguments:

* __cloud__ -- cloud provider to use, initially only _aws_ is supported
* __vm_count__ -- number of VMs to create, default to 1

```bash
$ ansible-playbook cloud.yml -e vm_count=3 -e cloud=gce
```

### Playbook actions

* Queries the selected cloud provider to get current list of VMs
* Creates VMs (or destroys) as necessary and updates the inventory under the __cloud__ group
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

Can not create VMs on multiple could providers in the same playbook execution. Instead run the playbook multiple times, each time with different __cloud__ parameter.
