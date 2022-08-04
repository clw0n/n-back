import os, sys, random, sqlite3
from time import sleep
from django.db import OperationalError

#make user select game mode
def select():
    start_date = os.system("date")
    print("""Please select a mode :
            1)Single-N-Back
            2)Dual-N-Back
            3)Tri-N-Back
            4)Quad-N-Back
            5)Penta-N-Back\n""")
    game_mode = int(input("> "))
    if game_mode == 1:
        start_single()
    elif game_mode == 2:
        sys.exit("Game mode not available for now !")
    elif game_mode == 3:
        sys.exit("Game mode not available for now !")
    elif game_mode == 4:
        sys.exit("Game mode not available for now !")
    elif game_mode == 5:
        sys.exit("Game mode not available for now !")
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
    elif accuracy >= 80.0:
        print("N-Back level increased ! Good job !")
        n += 1
        multiple *= 2
    else:
        if len(fails) <3:
            fails.append(0)
            print(f"N-Back level below 50% ! Only {3 - len(fails)} tries left and N-Back level will be decreased !") #make accountant
        else:
            if not n == 1:
                n -= 1
                multiple /= 2
                print("N-Back level has been decreased.")
            else:
                print("N-Back level is staying at 1.")
     
    #transfering statistics into the log folder of the current session
    try:
        conn = sqlite3.connect(f"{date}.db")
       
    
    except OperationalError:
        #transfer the game data (start_time, accuracy, level increase
        pass
    
    #veryfing the log folder for the session already exists
    

def clear_screen():
    os.system("clear -x")

if __name__ == "__main__":
    select()
