File Create
=========

Роль создает файл по пути `file_create_path` с содержимым `file_create_content`.

Role Variables
--------------

|   Variable name   |   Default   |   Required   |   Description                                                      |
|-------------------|-------------|--------------|------------------------------------|
| file_create_path              | "/tmp/test_file_create_1"    | True   | Путь по которому будет создан файл |
| file_create_content           | "Some string content"     | False   | Содержимое создаваемого файла                     |


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- name: Create File
    hosts: servers
    roles:
    - role: file_create
        vars:
          file_create_path: "./my_test_file"
          file_create_content: "Some string content"
```

License
-------

MIT

Author Information
------------------

Andrey Pirozhkov tabwizard@gmail.com.
