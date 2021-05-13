from pyfakefs.fake_filesystem_unittest import Patcher
import sys
import traceback

def bash():
    while True:
        command = input("$ ").split(" ")
        if command[0] == "exit": break
        try:
            output = globals()[command[0]](*command[1:])
        except:
            print(traceback.format_exc())
        else:
            if output != None:
                print(output)

def debug():
    import pdb; pdb.set_trace()




with Patcher() as patcher:
    os = patcher.fake_modules["os"]

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


    patcher.fs.create_file('/foo/bar', contents='test')



    bash()
