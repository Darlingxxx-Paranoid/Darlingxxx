import os

def get_all_files(filedir):
    l = []
    dir1 = filedir
    for dir2 in os.listdir(dir1):
        for dir3 in os.listdir(os.path.join(dir1, dir2)):
            for dir4 in os.listdir(os.path.join(dir1, dir2, dir3)):
                l.append(os.path.join(dir1, dir2, dir3, dir4))
    return l