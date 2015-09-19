# Script for placing all patents on a single line
# Callable from linux shell

import sys as sys
from re import sub

if __name__ == "__main__":
    one_patent_per_line = ''
    
    # stdin is a file object, "standard input"
    for line in sys.stdin.readlines():
        line = sub('\n', ' ', line)
        line = sub('\</us-patent-grant\>', '\n', line)
        one_patent_per_line += line
        
sys.stdout.write(one_patent_per_line)