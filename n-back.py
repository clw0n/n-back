import os, sys, random
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
    n = 1
    y = 0
    fails = []
    compare_list = []
    stats = []
    #clear the screen first
    os.system("clear")
    while not y == 20 + n:
        grid = [[0 for i in range(3)] for i in range(3)]
        clear_screen()
        rand_num = random.randint(0,2)
        rand_num2 = random.randint(0,2)
        grid[rand_num][rand_num2] = "X"
        compare_list.append(rand_num)
        compare_list.append(rand_num2)
        for elem in grid:
            print(elem)
        answer = input("> ")
        if answer == "A" or "a":
            try:
                if not compare_list == []:
                    if compare_list[-1] and compare_list[-2] == compare_list[-1 - n] and compare_list[-2 - n]:
                        stats.append(1)
                        start_single()
                        y += 1
                    else:
                        stats.append(0)
                        y += 1
            except IndexError:
                start_single()
                y += 1

    #returning statistics
    posi = []
    for elem in stats:
        if elem == 1:
            posi.append(elem)
    accuracy = len(posi) / len(stats) * 100
    print("Your score : " + accuracy)
    if 50.0 <= accuracy < 80.0:
        print("N-Back level is maintained. You need + 80% to increase your score.")
    elif accuracy >= 80.0:
        print("N-Back level increased ! Good job !")
        n += 1
    else:
        if len(fails) <3:
            fails.append(0)
            print("N-Back level below 50% ! Only " + 3 - len(list) + " tries and N-Back level will be decreased !")
        else:
            if not n == 1:
                n -= 1
                print("N-Back level has been decreased.")
            else:
                print("N-Back level is staying at 1.")


def clear_screen():
    os.system("clear")

def log():
    #note time at which user launched n-back
    #gather all data from current activity
    #put everything in a log file
    #use data to create graph statistics .py script
    pass

#create class / main.py

if __name__ == "__main__":
    select()
