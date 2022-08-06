import os, sys, random, sqlite3, time
from django.db import OperationalError


start_date = os.system("date| grep 2022 | cut -b 6-18")

if not "n-back" in os.listdir():
    sys.exit("Are you in the correct directory ?")

#check if the game log already exists
if not start_date in os.listdir("__log__"):
    conn = sqlite3.connect(f"/__log__/{start_date}.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE nback(
    dateID BLOB PRIMARY KEY,
    accuracy INTEGER,
    levels_increased INTEGER,
    game_mode INTEGER
    n INTEGER)""")
    cursor.execute("""INSERT INTO nback(dateID) VALUES(?)""",(start_date))
    conn.commit()
    conn.close()
    print("Log file created in the __log__ folder.")
else:
    print(f"Log file from this day detected. Writing changes in", dirfile, start_date, ".db")
    select()

#make user select game mode
def select():

    #check if the current log file exists
    #if yes wait for instructions
    #if no create the file with the start_date variable as a name and store it inside the file
    print("""
    1) PLAY
    2) SETTINGS
    3) MANUAL
    4) STATS
    5) QUIT\n""")


    choice = int(input("> "))

    first_actions = {1: start_playing, 2: settings, 3: manual_mode, 4: stats, 5: quit}
    first_action = first_actions.get(choice, error)
    first_action()

def start_playing():
    print_choices()

    game_mode = int(input("> "))

    actions = {1: start_single, 2: start_dual, 3: start_tri, 4: start_quad, 5: start_penta, 6:  select}
    action = actions.get(game_mode, error)
    action()

def quit():
    sys.exit("Shutting down... Goodbye !")

#single-n-back
def start_single(#n):  # n level wants to be checked from the previous log file, so its data needs to be gathered beforehand
    #declaring the variables first
    levels_increased = 0
    multiple = 2
    n = 1
    i = 0
    stats = []
    compare_list = []
    while i <= 20 + n:
        grid = [[0 for i in range(3)] for i in range(3)]
        clear_screen()
        randint_1 = random.randint(0,2)
        randint_2 = random.randint(0,2)
        grid[randint_1][randint_2] = "x"
        compare_list.append(randint_1)
        compare_list.append(randint_2)
        if not len(compare_list) == multiple:
            for elem in grid:
                print(elem)
            answer = int(input("> "))
            if answer == 1:
                if compare_list[-1] == compare_list[-1 - n - 1] and compare_list[-2] == compare_list[-2 - n - 1]:
                    stats.append(1)
                else:
                    stats.append(0)
            elif answer == 0:
                if compare_list[-1] != compare_list[-1 - n - 1] and compare_list[-2] != compare_list[-2 - n - 1]:
                    pass
        else:
            time.sleep(1)
            for elem in grid:
                print(elem)
            time.sleep(3)
        i += 1
    print(compare_list, stats)
    #returning statistics to the user
    posi = []
    fails = []
    for elem in stats:
        if elem == 1:
            posi.append(elem)
    accuracy = len(posi) / len(stats) * 100
    print("Game stats :\n")
    print(f"Visual accuracy : {accuracy} %") 
    if 50.0 <= accuracy < 80.0:
        print("N-Back level is maintained. You need + 80% to increase your score.")
        select()
        #transfer_game_data(start_date, accuracy, levels_increased, SINGLENBACK)
    elif accuracy >= 80.0:
        print("N-Back level increased ! Good job !")
        n += 1
        multiple *= 2
        levels_increased += 1
        #transfer_game_data(start_date, accuracy, levels_increased, SINGLENBACK)
        select()
    else:
        if len(fails) <3:
            fails.append(0)
            print(f"N-Back level below 50% ! Only {3 - len(fails)} tries left and N-Back level will be decreased !")
            #transfer_game_data(start_date, accuracy, levels_increased, SINGLENBACK)
            select()
        else:
            if not n == 1:
                n -= 1
                multiple /= 2
                print("3 fails ! N-Back level has been decreased.")
                levels_increased -= 1
                #transfer_game_data(start_date, accuracy, levels_increased, SINGLENBACK)
                select()
            else:
                print("N-Back level already at the lowest, staying at 1.")
                select()

                
def transfer_game_data(start_date, accuracy, levels_increased, game_mode):
    #transfering statistics into the log folder of the current session
    #try:
    #conn = sqlite3.connect(f"{start_date}.db")


    #except OperationalError:
    #transfer the game data (start_time, accuracy, level increase
    #pass

    #veryfing the log folder for the session already exists


def error():
    sys.exit("Please select a correct number.")

def print_choices():
            print("""
        1) SINGLE-N-BACK
        2) DUAL-N-BACK
        3) TRI-N-BACK
        4) QUAD-N-BACK
        5) PENTA-N-BACK
        6) GO BACK\n""")

    
def retrieve_data(game_mode): #retrieve log data from the existing latest file of the log folder
    conn = sqlite3.connect(f"/__log__/{start_date}.db") #
    cursor = conn.cursor()
    cursor.execute("""""") #retrieve the n level and 
    
def stats(): #create a graph from all the log data files
    pass

def start_dual(): #copy start_single, sound in the terminal
    # sound will be represented by dictionnary of variables
    # on a different sound panel folder ----> accuracy needs to contain all informations depending on the game mode to facilitate data transfer
    pass

def start_tri(): #copy start dual, but with colour, same process, colour displayed in terminal etc
    pass

def start_quad(): #copy start tri but with different figures
    pass

def start_penta():#copy start tri but with numbers (requires graphical user interface)
    pass

def settings(): #change settings (graphical user interface only)
    pass

def manual_mode(): #untracked manual mode, don't log the data in the folder
    pass

def clear_screen():
    os.system("clear -x")
    
if __name__ == "__main__":
    select()
