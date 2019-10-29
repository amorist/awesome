#!/usr/bin/python
import os
starred_output = os.popen('starred --username amorist --sort > README.md', 'r')
print(starred_output.read())
