import sys
import random

def get_random(file_num):
   with open('group' + str(file_num) + '.txt', 'r') as groupfile:
      lines = list(groupfile.readlines())
      random.shuffle(lines)
      for line in lines:
         if (sys.version.startswith("3")):
            input(line)
         else:
            raw_input(line)
         

def main(argv):
   if len(argv) < 1:
      print("Not enough arguments")
   else:
      file_num = int(argv[0])
      get_random(file_num)

if __name__ == "__main__":
   main(sys.argv[1:])