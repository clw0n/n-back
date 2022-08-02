import os, sys


if not os.geteuid() == 0:
    sys.exit("You need to be root in order to save your progress !")


def check_directory():
    pwd = os.getcwd()
    #assuming we are in the cloned repository
    if "__log__" in pwd:
        if "n-back" in pwd:
            os.mkdir("__log__")
            print("Wrote log folder in current working directory. Do not remove the log files in the folder, for which they will be used to make a graph out of your n-back performances.")
        else:
            sys.exit("Please change dir to cloned directory.")
    else:
        sys.exit("__log__ folder already exists.")

check_directory()

