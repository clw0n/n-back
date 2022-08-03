import os, sys, random, sqlite3
from time import sleep

#make user select game mode
def select():
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
        #printing the grid
        for elem in grid:
            print(elem)
        if len(compare_list) == multiple:
            clear_screen()
        else:
            answer = int(input("> "))
            if answer == 1:
                if compare_list[-1] and compare_list[-2] == compare_list[-2 - n] and compare_list[-3 - n]:
                    stats.append(1)
                else:
                    stats.append(0)
            elif answer == 0:
                if compare_list[-1] and compare_list[-2] != compare_list[-2 - n] and compare_list[-3 - n]:
                    stats.append(1)
                else:
                    stats.append(0)
        i += 1
    print(compare_list, stats)
    #returning statistics
    posi = []
    fails = []
    for elem in stats:
        if elem == 1:
            posi.append(elem)
    accuracy = len(posi) / len(stats) * 100
    print("Game stats :\n")
    print(f"Accuracy : {accuracy} %") 
    if 50.0 <= accuracy < 80.0:
        print("N-Back level is maintained. You need + 80% to increase your score.")
    elif accuracy >= 80.0:
        print("N-Back level increased ! Good job !")
        n += 1
        multiple *= 2
    else:
        if len(fails) <3:
            fails.append(0)
            print(f"N-Back level below 50% ! Only {3 - len(fails)} tries left and N-Back level will be decreased !")
        else:
            if not n == 1:
                n -= 1
                multiple /= 2
                print("N-Back level has been decreased.")
            else:
                print("N-Back level is staying at 1.")

def interface():
    #create well looking interfaces for the n-back and store the different variables inside a dictionnary
    pass

def log_data():
    #if the player doesn't play, no log will be created
    #note time at which user launched n-back
    date = os.popen("date") # + end game date (convert time = time activity)

    #gather all data from current activity 
    #put everything in a log file after session is interrupted
    #transfer data into a local database
    pass

def clear_screen():
    os.system("clear -x")

def settings():
    pass
    #change parameters : key bindings, erase all data, create a new user, change the interface

if __name__ == "__main__":
    select()
