#!/usr/bin/env python3
"""List all files in a given directory"""

# directory of files to be listed
dir_data = './data/'

# list all files
filenames_all = os.listdir(dir_data)

# list all *.png files in the given directory and split suffix from filename
filenames_glob_nosuffix = [os.path.splitext(f)[0] for f in os.listdir(dir_data) if f.endswith('.png')]
