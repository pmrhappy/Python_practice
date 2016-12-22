import re, os, sys, shutil
#import pkg.function_call
from importlib.machinery import SourceFileLoader

current_path = os.path.realpath(sys.argv[1])
sys.path.append(current_path)

py_pattern = re.compile(".py$")
for path, subdir, file_names in os.walk(current_path):
    for file_name in file_names:
        if py_pattern.search(file_name):
            file_path = os.path.join(path, file_name)
            try:
                foo = SourceFileLoader(file_name, file_path).load_module()
            except:
                pass

for path, subdir, file_names in os.walk(current_path):
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        pattern = re.compile("__pycache__")
        print(file_path)
        if pattern.search(file_path):
            print("Yes")
            file_name_pattern = re.compile("cpython-34.")
            exclusive_pattern = re.compile("__init__")
            if file_name_pattern.search(file_name) and not exclusive_pattern.search(file_name):
                new_file_name = file_path.split("cpython-34.")[0] + file_path.split("cpython-34.")[1]
                os.rename(file_path, new_file_name)
                move_path = os.path.join(os.path.dirname(new_file_name), "..")
                try:
                    shutil.move(new_file_name, move_path)
                except:
                    pass
                print(os.path.join(move_path, new_file_name.split("\\")[-1]))
                del_path = os.path.join(move_path, new_file_name.split("\\")[-1])
                del_path = del_path[:-1]
                print(del_path)
                os.remove(del_path)
            