import os

my_dir = os.getcwd()


def describe_path(path, depth=0):
    # does it exist
    if os.path.exists(path):
        # is the path a valid directory
        if os.path.isdir(path):
            # find the things that are in the directory
            print path, "is a directory{}".format(depth)
            for sub_path in os.listdir(path):
                depth += len(path)
                # find the things that are in the directory
                print path, "is a directory{}".format(depth)
                # recurse
                describe_path(os.path.join(path, sub_path))
        else:
            depth += len(path)
            # find the things that are in the directory
            print path, "is a directory{}".format(depth)
            # it must me a file, print it
            print path, depth

describe_path(my_dir)
