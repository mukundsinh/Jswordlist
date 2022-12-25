#!/usr/bin/python

# by R00T D3STR0Y3R -https://github.com/mukundsinh 
# Twitter (@r00td3str0y3r)

import sys
from jsbeautifier import beautify
import re
import string

blacklisted = [
# list of words omitted for brevity
]

# Read the contents of the input file from stdin
contents = sys.stdin.read()

# Use the jsbeautifier module to prettify the JavaScript code
beautified = beautify(contents)

# Split the beautified code into a list of words
words = re.split(r'\W+', beautified)

# Iterate through the list of words and print any that are not in the blacklisted list
for word in words:
    if word.lower() not in blacklisted:
        print(word)
