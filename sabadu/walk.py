import os
lista = '.'
def ano(top):
    try:
        names = os.listdir(top)
    except error, err:
        return
    dirs, nondirs = [], []
    for name in names:
        if os.path.isdir(os.path.join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)
    yield top, dirs, nondirs
    for name in dirs:
        new_path = os.path.join(top, name)
        for x in ano(new_path):
            yield x

for subdir, dirs, files in ano(lista):
    for file in files:
         print os.path.join(subdir, file)
