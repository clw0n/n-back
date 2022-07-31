import os, sys
from time import sleep

#make user select game mode
print("""Please select a mode :
            1)Single-N-Back
            2)Dual-N-Back
            3)Tri-N-Back
            4)Quad-N-Back
            5)Penta-N-Back"""\n)

game_mode = raw_input("> ")

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
def start_single(n = int):
    y = 0
    #clear the screen first
    os.system("clear")
    grid = [[0 for i in range(3)] for i in range(3)]
    while not y == 20:
        clear_screen()
        rand_num = random.randint(0,2)
        grid[random_number()][random_number()] = "X"
        compare.list_append(random_num)
        print_grid()
        ask = raw_input("> ")
        if ask == "Y" or "y":
            return compare_list[-1] == compare_list[len(compare_list) - n)

def list_compare():
    compare_list = []
    rand_num = random.randint(0,2)
    compare_list.append(random_num)
    return rand_num

def clear_screen():
    os.system("clear")

def print_grid():
    for elem in grid:
        print(elem)
