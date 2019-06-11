#!/usr/bin/python
import os
output = os.popen('starred --username amorist --sort > README.md', 'r')
print(output.read())
