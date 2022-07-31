import os, sys
from time import sleep

try:
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
                list_compare = []
                stats = []
                global grid
                grid = [[0 for i in range(3)] for i in range(3)]
                while not y == 20:
                    clear_screen()
                    rand_num = random.randint(0,2)
                    grid[rand_numb][rand_numb] = "X"
                    compare_list.append(rand_numb)
                    print_grid()
                    ask = raw_input("> ")
                    if list_compare != None and compare_list[-1] == compare_list[len(compare_list - 1) - n) and ask == "a" "A":
                        print("Correct !")
                        stats.append(1)
                    else:
                        print("False !")
                        stats.append(0)
                    y += 1

            def clear_screen():
                os.system("clear")

            def print_grid():
                for elem in grid:
                    print(elem)
                                                    
            def stats():
                for i, j in range(len(stats)):
                                                                                 
                                                                
except KeyboardInterrupt:
    sys.exit("Shutting down. Goodbye !")
