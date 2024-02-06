#!/usr/bin/python3
"""
Script to add all arguments to a Python list
and save them to a file in JSON format.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Check if the file exists
filename = 'add_item.json'
if exists(filename):
    # Load existing items from file
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
