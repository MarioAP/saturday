# create a variable containing a python dictionary
my_dict = {'Name': 'asu', 'age': 20}
# print that dictionary
print my_dict
# print true if they key 'asu' is in the dictionary
print "asu" in my_dict
# add a key->value 'asu': ' boot'  to that dictionary
my_dict["asu"] = 'boot'
# print that dictionary
print my_dict
# print true if they key 'asu' is in the dictionary
print "asu" in my_dict
# print the value of 'asu' in the dictionary
print my_dict['asu']
print my_dict.get('asu')
