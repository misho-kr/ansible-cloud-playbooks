# -*- Mode: Python -*-

import string

from ansible import errors

def make_ec2_tag_filters(*vm_tags):
    """Transform dictionary of vm tags to filters-by-tag for EC2 instances"""

    all_tags = []
    for d in vm_tags:
        if not isinstance(d, dict):
            raise AnsibleFilterError("|make_ec2_tag_filters expects dictionaries, got" + repr(d))
        all_tags.extend(d.items())

    # return { x:x for x in range(10) }
    return { "tag:"+k:v for k,v in all_tags }

def string_2_list(s):
    """The ommission of 'strings.split' from the Jinja filters is baffling"""

    return([string.strip(s2) for s2 in string.split(str(s), ',')])

class FilterModule(object):
    '''Ansible helper jinja2 filters'''

    def filters(self):
        return {
            'vm_tags_2_aws_filters':    make_ec2_tag_filters,
            'str2list':                 string_2_list,
        }