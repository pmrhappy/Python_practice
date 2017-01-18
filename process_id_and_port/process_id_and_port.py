import psutil, time, os

# In Windows cmd you can use "netstat -nao to get the pid and port
" 
file_name = os.path.basename(__file__)
print("file: ", file_name)
print("id: ", os.getpid())
for proc in psutil.process_iter():
    
    try:
        print(proc.connections()[0])
        print(proc, "\n")
    except:
        pass
    if proc.name() == file_name:
        print(file_name, " : ", proc)