my_list = [0, 1, 3, 4]

# Algorithms do work
for item in my_list:
    if item % 2 == 0:
        print "Algorithm: {} is even".format(item)

# Functions do work and can be called by name
def print_evens(my_list):
    for item in my_list:
        if item % 2 == 0:
            print "Function: {} is even".format(item)

print_evens(my_list)

# Methods are functions which are bound to Classes or Objects
class Lista(object):

    def __init__(self,):
        self.my_list = None

    def print_evens(self):
        for item in self.my_list:
            if item % 2 == 0:
                print "Method: {} is even".format(item)

my_object = Lista()
my_object.my_list = [0, 1, 3, 4]
my_object.print_evens()
