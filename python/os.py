import os
from pathlib import Path

## Get environmental variables
print(os.environ["HOME"])
print(os.environ["SHELL"])

## Join path
print(os.path.join("usr", "bin", "env"))
print(os.path.join("usr/", "bin/", "env"))

## Walk
root_dir = os.path.join(os.environ["HOME"], "git/code-note")
for i in os.walk(root_dir):
    print(i)
