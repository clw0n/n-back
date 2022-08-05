import os, sys, random, sqlite3, time
from django.db import OperationalError

#make user select game mode
def select():
    start_date = os.system("date")
    print("""1) PLAY
             2) SETTINGS
             3) MANUAL
             4) STATS
             5) QUIT\n""")

    choice = int(input("> "))
    if choice == 1:
        print("""1) SINGLE-N-BACK
                 2) DUAL-N-BACK
                 3) TRI-N-BACK
                 4) QUAD-N-BACK
                 5) PENTA-N-BACK
                 6) GO BACK\n""")
        game_mode = int(input("> "))
        if game_mode == 1:
            start_single()
        elif game_mode == 2:
            start_dual()
        elif game_mode == 3:
            start_tri()
        elif game_mode ==4:
            start_quad()
        elif game_mode == 5:
            start_penta()
        elif game_mode == 6:
            select()
    elif choice == 2:
        settings()
    elif game_mode == 3:
        manual_mode()
    elif game_mode == 4:
        sys.exit("In order to view statistics, close the program and run 'python3 stats.py' in the cloned n-back repository.")
    elif game_mode == 5:
        print("Writing changes to log files...")
        #write log changes, exit
        sys.exit("Shutting down... Goodbye !")
    else:
        sys.exit("Please choose a valid number.")
#single-n-back
def start_single():
    #declaring the variables first
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
    elif accuracy >= 80.0:
        print("N-Back level increased ! Good job !")
        n += 1
        multiple *= 2
        select()
    else:
        if len(fails) <3:
            fails.append(0)
            print(f"N-Back level below 50% ! Only {3 - len(fails)} tries left and N-Back level will be decreased !")
            select()
        else:
            if not n == 1:
                n -= 1
                multiple /= 2
                print("3 fails ! N-Back level has been decreased.")
                select()
            else:
                print("N-Back level already at the lowest, staying at 1.")
                select()
     
    #transfering statistics into the log folder of the current session
    #try:
        #conn = sqlite3.connect(f"{start_date}.db")
       
    
    #except OperationalError:
        #transfer the game data (start_time, accuracy, level increase
        #pass
    
    #veryfing the log folder for the session already exists


def start_dual():
    pass

def start_tri():
    pass

def start_quad():
    pass

def start_penta():
    pass

def settings(grid):
    pass

def manual_mode():
    pass

def clear_screen():
    os.system("clear -x")

def grid():
    grid = [[0 for i in range(3)] for i in range(3)]
    return grid()

if __name__ == "__main__":
    select()
mkultra79@mkult
