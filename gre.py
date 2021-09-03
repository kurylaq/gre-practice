import sys
import random

def get_random(file_num):
   with open('group' + str(file_num) + '.txt', 'r') as groupfile:
      lines = groupfile.readlines()
      return lines[random.randint(0, len(lines) - 1)]

def main(argv):
   if len(argv) < 1:
      print("Not enough arguments")
   else:
      file_num = int(argv[0])
      print(get_random(file_num))

if __name__ == "__main__":
   main(sys.argv[1:])