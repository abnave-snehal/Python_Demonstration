# python CommandLine3.py 11 21 pune 89.00

import sys

def main():
  print("Command Line Arguments are : ")
  for i in range(len(sys.argv)):
     print(sys.argv[i])

if __name__ == "__main__":
    main()