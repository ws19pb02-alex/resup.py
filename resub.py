"""
Normalize phone numbers.
"""

import sys
import re   #regular expressions

infilename = "phonenum.py"

try:
    infile = open(infilename)
except FileNotFoundError:
    print(f"Sorry, could not find input file \"{infilename}\".")
    sys.exit(1)
except PermissionError:
    print(f"Sorry, no permission to open input file \"{infilename}\".")
    sys.exit(1)

for line in infile:
    line = line.rstrip("\n")       #Remove the trailing newline.
    line = re.sub(r"\D", "", line) #Remove every non-digit.
    line = re.sub(r"^1", "", line) #Remove the number one from the begining of the area code
    line = re.sub("r(...)-(....)", r"(???) \1-\2 ", line)
    if not re.search("^\d{10}$", line): # if line is not ten digits give ten questions marks
        line = 10 * "?"
    #if re.search("^\d{7}$", line): # if the line has seven digits put 3 questions marks in front
        #line = 3 * "?" "\d\d\d"-"\d\d\d\d"
    line = re.sub("(...)(...)(....)", r"(\1) \2-\3", line)   #or "(.{3})(.{3})(.{4})"
    print(line)

infile.close()
sys.exit(0)
