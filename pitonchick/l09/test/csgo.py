import os 
#print(os.getcwd())
files = os.listdir(path=".")
for file in files:
    n = file.rfind(".")
    dst = file[:n] + ".lox"
    if file != os.path.basename(__file__):
        os.rename(file, dst)
