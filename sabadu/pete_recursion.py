import os


my_dir = os.getcwd()

def describe_path(path):
    # check does it exist
    if os.path.exists(path):
       # is the path a valid dirctory
       if os.path.isdir(path):
           # find the things that are in the directory
           for sub_path in os.listdir(path):
               # recursion
               describe_path(sub_path)
           else:
               # it must be a file, print it
               print path

describe_path(my_dir)
