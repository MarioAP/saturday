my_list = [
    0,
    4,
    -8,
    [1, 2, 3],
    [],
    [True],
    [False],
    "True"
    "False",
    True,
    False,
    {},
    {True: False},
    3.5,
    0.0,
]

if my_list[1]:
    print "my_list 1 is truthy"
if my_list[0]:
    print "my_list 0 is truthy"
if my_list[0] and my_list[1]:
    print "my_list 0 and my_list 1 are truthy"
if my_list[0] or my_list[1]:
    print "my_list 0 or my_list 1 are truthy"

if (True and False) and (False or True):
    print "YES"
else:
    print "NO"



[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> bool("")
False
>>> bool("jgfjgf")
True
>>> bool([])
False
>>> bool([False])
True
>>> bool([] or "1")
True
>>> bool([] or "")
False
