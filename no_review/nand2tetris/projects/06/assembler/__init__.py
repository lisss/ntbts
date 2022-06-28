import sys
import os
from parser import Reader

if len(sys.argv) != 2:
    raise Exception('Must provide file name')

file = sys.argv[1]
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, file)
reader = Reader(filename)
lines = reader.read_file()
print(lines)
