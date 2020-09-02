#!/usr/bin/python
import os
import sys

blacklist = [
  "shutdown",
  "rm"
]

argv = sys.argv[1:]
command = argv[0]

if command in blacklist or any(blacklistedCommand in blacklist for blacklistedCommand in argv):
  print("No! This command is forbidden.")
  sys.exit(1)

os.system(" ".join(argv))