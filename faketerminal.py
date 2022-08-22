from pyfakefs.fake_filesystem_unittest import Patcher
import sys
import traceback
with Patcher() as patcher:
    import pdb; pdb.set_trace()
    os = patcher.fake_modules["os"]
    io = patcher.fake_modules["io"]
    patcher.fs.create_file("/home/root/test")

host_name = "localhost"

def bash(username="root"):
    prompt = f"\033[01;32m{username}@{host_name}\033[00m:\033[01;34m{os.getcwd()}\033[00m$ "
    while True:
        command = input(prompt).split(" ")
        if command[0] == "exit": break
        try:
            output = globals()[command[0]](*command[1:])
        except KeyError:
            if command[0] == "":
                continue
            else:
                print(f"{command[0]}: command not found")
        except:
            print(traceback.format_exc())
        else:
            if output != None:
                print(output)

def debug():
    import pdb; pdb.set_trace()

pwd = os.getcwd

def cd(path):
    try:
        os.chdir(path)
    except NotADirectoryError:
        print(f"cd: {path}: Not a directory")
    except FileNotFoundError:
        print(f"cd: {path}: No such file or directory")
        
cat = lambda filename : open(filename, "r").read()

ls = lambda path=None : "\n".join(os.listdir(path if path != None else "."))

def mount(path):
    patcher.fs.add_real_directory(path)

if __name__ == "__main__":
    bash()
