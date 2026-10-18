"""
This is the implementation of Herbert Kociemba's two-phase algorithm for solving Rubik's Cube

It is pretty straighforward, but great to make additional functionality

All we should do is use the kociemba library and kociemba.solve(cube_string) and it will return a string of turns to solve a cube

Solved cube is defined as: UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB

But kociemba library is troubled, that's why I cloned the pythonic algorithm from the repo directly to the kociemba folder

     [0]   [1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]    ← columns
[   ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9'], → cube_array[0]
    ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9'], → cube_array[1]
    ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'], → cube_array[2]
    ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9'], → cube_array[3]
    ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'], → cube_array[4]
    ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']  → cube_array[5]
]                                                                  ↑
                                                                  rows 
"""
import kociemba
from Facelets import *
from scramble import *
import time
from typing import Callable

def pack_cube_into_kociemba_string(list: list[list[str]]) -> str:
    s = ""
    for i in range(0, 9):
         s += f"{list[0][i]}"
    for i in range(0, 9):
         s += f"{list[3][i]}"
    for i in range(0, 9):
         s += f"{list[2][i]}"
    for i in range(0, 9):
         s += f"{list[5][i]}"
    for i in range(0, 9):
         s += f"{list[1][i]}"
    for i in range(0, 9):
         s += f"{list[4][i]}"

    s = s.replace("1", '').replace("2", '').replace("3", '').replace("4", '').replace("5", '').replace("6", '').replace("7", '').replace("8", '').replace("9", '').replace("\'", '')
    return s

def pack_kociemba_solve_string_into_func_list(kociemba_str: str) -> list[Callable]:
     kociemba_list = kociemba_str.split(' ')
     kociemba_list = list(map(lambda x: x.replace('\'', 'p'), kociemba_list))
     kociemba_list = list(map(lambda x: x.lower(), kociemba_list))
     kociemba_list = list(map(lambda x: globals()[x], kociemba_list))
     return kociemba_list


def solve_with_kociemba(cube_array: list[list[str]]) -> str:
     kociemba_to_solve_string = pack_cube_into_kociemba_string(cube_array)
     kociemba_solved_str = kociemba.solve(kociemba_to_solve_string)
     return kociemba_solved_str


def apply_kociemba_solve(cube_array: list[list[str]], kociemba_solved_str: str) -> list[list[str]]:
     kociemba_solved_list = pack_kociemba_solve_string_into_func_list(kociemba_solved_str)
     kociemba_composed = compose(kociemba_solved_list)
     kociemba_composed(cube_array)
     return cube_array



if __name__ == "__main__":
    cube = create_facelets(3)

    scramble = generate_scramble()
    print(f"Scramble: {get_scramble(scramble)}")
    apply_scramble(scramble, cube)
    print(f"Cube to be solved:\n{create_2D(cube)}")

    cube_to_solve_with_kociemba_string = pack_cube_into_kociemba_string(cube)
    print(f"kociemba formated cube string that has to be solved: {cube_to_solve_with_kociemba_string}")

    beg = time.perf_counter()
    kociemba_solved_str = kociemba.solve(cube_to_solve_with_kociemba_string)
    end = time.perf_counter()
    print(f"Computation time: {end - beg}")

    print(f"Kociemba algorithm to solve the cube: {kociemba_solved_str}")

    kociemba_solved_list = pack_kociemba_solve_string_into_func_list(kociemba_solved_str)

    kociemba_composed = compose(kociemba_solved_list)
    kociemba_composed(cube)
    print(f"Result:\n{create_2D(cube)}")

    