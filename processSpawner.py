#!/bin/python

import os

## first arg is command, 2nd argument is a list of commands.
## The first in this list is the name of the process the n number of variables just like a standard shell.
os.execvp("ping", ["processName","-c 5", "127.0.0.1"])
