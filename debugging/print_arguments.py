#!/usr/bin/python3
import sys

# Print all arguments passed to the script, excluding the script name
for i in range(1, len(sys.argv)):
    print(sys.argv[i])

