import os
def list_file(name = "."):
    if os.path.isdir(name):
        try:
            for i in os.listdir(name):
                list_file((name+"/"+i))
        except PermissionError:
            pass
    elif os.path.isfile(name):
        try:
            if(os.path.getsize(name) > 100000000):
                print(name)
        except PermissionError:
            pass
    else:
        pass

list_file("C:")