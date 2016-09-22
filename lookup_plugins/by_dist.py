# (c) 2016, Misho Krastev <misho(dot)kr(at)gmail.com>
#
# #####################################################################
#   Custom Lookup plugin for Ansible to define platform-dependant vars
# #####################################################################

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup         import LookupBase
from ansible.parsing.yaml.objects   import AnsibleMapping

class LookupModule(LookupBase):
    """Resolve variable setting based on distribution and version

    Usage:

        var: "{{ lookup('by_dist', 'varname') }}

    Supported formats of varname_<by-os>:

    varname_by_os:
        <os-distribution-name>  :    value
        <os-distribution-name2> :    value2

    varname_by_os:
        <os-distribution-name> :
            <os-distribution-version>:      value
            <os-distribution-version2>:     value2

    varname_by_os:
        <os-distribution-name> :
            <os-distribution-version>:      value
            default:                        value2
        default:                            value3
    """

    def run(self, terms, variables, **kwargs):

        ansible_distribution         = variables.get('ansible_distribution')
        ansible_distribution_version = variables.get('ansible_distribution_version')

        var_name = terms[0] + "_by_os"

        try:
            var = variables.get(var_name)

            if ansible_distribution in var:
                var = var.get(ansible_distribution)
            else:
                var = var.get('default')

            if type(var) is AnsibleMapping:
                if ansible_distribution_version in var:
                    var = var.get(ansible_distribution_version)
                else:
                    var = var.get('default')

        except KeyError:
            return([])

        return([var])
