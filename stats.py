import sys, os

#check user privileges
if not os.geteuid() == 0:
    sys.exit("You need to be root in order to save your progress !")

#read the log data
def check_directory():
    pwd = os.getcwd()
    print("Checking log files...")
    try:
        if "n-back" in pwd:
            os.mkdir("__log__")
            print("Wrote log folder in current working directory. Do not remove the log files in the folder, for which they will be used to make a graph out of your n-back performances.")
        else:
            sys.exit("Please cd in the cloned github repository.")
    except FileExistsError:
        print("__log__ folder already exists.")

        
#connect to the database to retrieve data (date, levels increased, average games per day and game type)


#use retrieved data to make a graph on tkinter with matplotlib for the graph


if __name__ == "__main__":
  check_directory()
