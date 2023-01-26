#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path

print("Inside Python script")

parser = argparse.ArgumentParser(
    prog="Compiler",
    description="""Compile and run a c++ program""",
    epilog="None ya buisness...",
)

parser.add_argument(
    "folder", help="Relative path to folder of cpp files to compile and run"
)
parser.add_argument(
    "input_path", help="Path of the input files (in the form Input***.txt): "
)
parser.add_argument(
    "compiler_type",
    help="Indicate the compiler you would like to use (1 = CygWin and gcc, 2 = VisualStudio and cl)",
)

args = parser.parse_args()
folder = args.folder
input_path = args.input_path
compiler_type = args.compiler_type


source = Path(folder)
files = [x.name for x in source.iterdir() if x.is_file()]

for i, file in enumerate(files):
    folder_file = f"{folder}/{file}"
    print(f"folder_file = {folder_file}")
    exec_loc = "a.out"
    print(f"exec_loc = {exec_loc}")
    subprocess.call(["g++", folder_file])
    output = subprocess.run([f"{exec_loc}", "1"], capture_output=True, shell=True)
    print(output.stdout.decode())
