#!/usr/bin/python
import os
starred_output = os.popen('starred --username amorist --sort > README.md', 'r')
print(starred_output.read())
git_output = os.popen('git add README.md && git commit -m "update" && git push -u origin master', 'r')
print(git_output.read())
