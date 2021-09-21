#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module for create file with content

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: Path to create file.
        required: true
        type: str
    content:
        description: Content to created file
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Andrey Pirozhkov (@tabwizard)
'''

EXAMPLES = r'''
# Create empty file
- name: Create file
  my_namespace.my_collection.my_own_module:
    path: "/tmp/hello.txt"

# Create file with content
- name: Create file
  my_namespace.my_collection.my_own_module:
    path: "/tmp/hello.txt"
    content: "Hello World"

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_own_module:
    path: "/tmp/hello.txt"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
res_path:
    description: Path to create file.
    type: str
    returned: always
    sample: '/tmp/hello.txt'
res_content:
    description: Content to created file.
    type: str
    returned: always
    sample: 'Hello World'
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    exist = False
    equally = False
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='')
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        res_path='',
        res_content=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    if not os.path.exists(module.params['path']):
        os.mknod(module.params['path'])
        exist = True
    FW = open(module.params['path'], 'r')
    fc = FW.read()
    if fc != module.params['content']:
        FW = open(module.params['path'], 'w')
        FW.write(module.params['content'])
        equally = True
    FW.close()
    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['res_path'] = module.params['path']
    result['res_content'] = module.params['content']

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if exist or equally:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['path'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
