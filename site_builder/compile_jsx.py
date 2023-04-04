import os, subprocess

def convert_file(file):
    print(f'Converting {file}')
    subprocess.Popen([
        "npx", "babel", "--config-file",
        "./.babelrc", file, "-d", os.path.split(file)[0]]).wait()
    os.remove(file)

def traverse_files(path):
    for p_ in os.listdir(path):
        p = os.path.join(path, p_)
        
        if os.path.isdir(p):
            traverse_files(p)
        else:
            if os.path.splitext(p)[1] == ".jsx":
                convert_file(p)

traverse_files("./output")