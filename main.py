from time import sleep

from world import World
from ant import Ant
import os


def print_swiat(w, ants):
    board_rows = []

    # prepare board
    for y, row in enumerate(w.world_matrix):
        board_cols = []
        for x, p in enumerate(row):
            board_cols.append("_")
        board_rows.append(board_cols)

    for y, row in enumerate(w.world_matrix):
        for x, p in enumerate(row):
            if p.visited > 1:
                board_rows[p.y][p.x] = "*"
            elif p.visited == 1:
                board_rows[p.y][p.x] = "."



    # for i, ant in enumerate(ants):
    #     for pos in ant.path:
    #         # print("Ant Pos: {},{} Visited: {}".format(pos.x, pos.y, pos.visited),end="")
    #         znak = '.'
    #         if pos.visited > 1:
    #             znak = '*'
    #         board_rows[pos.y][pos.x] = znak

    board_rows[w.food_pos.y][w.food_pos.x] = 'F'
    board_rows[w.ant_colony_pos.y][w.ant_colony_pos.x] = 'K'
    # display current state of world
    for y, rows in enumerate(board_rows):
        # print("{}: ".format(y), end="")
        for row in rows:
            print(row, end='')
        print("")


swiat = World()
ants = [Ant(swiat,k) for k in range(100)]
#ants = [Ant(swiat, "1")]
iteration_list=range(100)
for i in iteration_list:
    for a in ants:
        a.move()
    os.system('clear')
    print("Ant pos: ", end="")
    for p in a.path:
        print("{}, {} ".format(p.x, p.y), end="\n")
    print()
    print("Iteracja: {} z {} ".format(i+1,len(iteration_list)), end="")
    print(" Food: {},{}".format(swiat.food_pos.x, swiat.food_pos.y), end="")
    print(" Ant colony: {},{}".format(swiat.ant_colony_pos.x, swiat.ant_colony_pos.y))


    print_swiat(swiat, ants)
    sleep(0.1)

print("End")
