import sys as sys
from re import sub

if __name__ == "__main__":
    original_format = ''
    
    # stdin is a file object, "standard input"
    for line in sys.stdin.readlines():
        line = sub('<endline>', '\n', line)
        original_format += line
        
sys.stdout.write(original_format)