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
    epilog="None ya bizz..."
)

parser.add_argument('folder', help='Relative path to folder of cpp files to compile and run')
parser.add_argument('input_path', help="Path of the input files (in the form Input***.txt): ")
parser.add_argument('compiler_type', help="Indicate the compiler you would like to use (1 = CygWin and gcc, 2 = VisualStudio and cl)")

args = parser.parse_args()
folder = args.folder
input_path = args.input_path
compiler_type = args.input_path


source = Path(folder)
files = [x.name for x in source.iterdir() if x.is_file()]

for i, file in enumerate(files):
    folder_file = f"{folder}/{file}"
    print(f"student file location= {folder_file}")
    exec_loc = "a.out"
    if compiler_type == 1:
        subprocess.call(["g++", folder_file])
    elif compiler_type == 2:
        subprocess.call(["cl", folder_file])
    else:
        raise Exeption("You Messed Up :( invalid compiler type.")
    output = subprocess.run(f"./{exec_loc}", capture_output=True, shell=True)
    print(f"stdout_{i} : {output.stdout.decode()}")
    print(f"stderr: {output.stderr.decode()}")
