#!/usr/bin/python3
"""Creates a script that adds all arguments to a Python list, and then
save them to a file"""
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

if not os.path.isfile(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("[]")

if len(argv) > 1:
    file_data = load_from_json_file(filename)
    for i in range(1, len(argv)):
        file_data.append(sys.argv[i])

    save_to_json_file(file_data, filename)
