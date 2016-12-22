import os 

for path, subdirs, files in os.walk(".."):
    for file_name in files:
        file_path = os.path.join(path, file_name)
        print(file_path)