#!/usr/bin/env python3

import subprocess
import argparse
import os
import sys
from pathlib import Path

print("Inside Python script")

parser = argparse.ArgumentParser(
    prog='Compiler',
    description='''Compile and run a c++ program''',
    epilog="None ya buisness..."
)

parser.add_argument('folder', help='Relative path to folder of cpp files to compile and run')
args = parser.parse_args()
folder = args.folder

source = Path(folder)
files = [x.name for x in source.iterdir() if x.is_file()]

for file in files: 
    print(type(file))
    print(file)
    

