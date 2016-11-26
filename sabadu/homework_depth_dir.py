# Homework - add the file depth to the print statement
import os

my_dir = os.getcwd()


def describe_path(path, depth=0):
    # does it exist
    if os.path.exists(path):
        # is the path a valid directory
        if os.path.isdir(path):
            # find the things that are in the directory
            print'|',  path, "is a directory"
            for sub_path in os.listdir(path):
                # recurse
                describe_path(os.path.join(path, sub_path))
        else:
            # it must me a file, print it
            depth = path.count(os.sep)
            print '|_____', path, depth

describe_path(my_dir)
