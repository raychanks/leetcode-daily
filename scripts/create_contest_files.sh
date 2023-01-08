#!/bin/bash

# Usage
# ./create_contest_files.sh <date>
# 
# e.g.
# ./create_contest_files.sh 8jan

mkdir contests/2023/$1
cd contests/2023/$1

touch a.py b.py c.py d.py
