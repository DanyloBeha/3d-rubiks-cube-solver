"""
How will scrambling work:

As it takes 20 moves to get the cube to any possible position:

Turns      	Count of Positions
0	        1
1	        18
2	        243
3	        3,240
4	        43,239
5	        574,908
6	        7,618,438
7	        100,803,036
8	        1,332,343,288
9	        17,596,479,795
10	        232,248,063,316
11	        3,063,288,809,012
12	        40,374,425,656,248
13	        531,653,418,284,628
14	        6,989,320,578,825,358
15	        91,365,146,187,124,313
16	        about 1,100,000,000,000,000,000
17	        about 12,000,000,000,000,000,000
18	        about 29,000,000,000,000,000,000
19	        about 150,000,000,000,000,000,000
20	        about 490,000,000,000,000,000,000

We will use exactly 20 moves to scramble the cube, for the sake of mathematical beauty

We will generate 20 moves from: u, u2, up, l, l2, lp, f, f2, fp, r, r2, rp, b, b2, bp, d, d2, dp

First, we will create a fucntion to compose the moves into one algorithm

Then, we will make a function that will randomly generate moves and put them into a compose function
"""
import json
from turns import *
from Facelets import *
import random
import secrets
from typing import Callable
random.seed(a = None, version = 2)

"""Composing all turns into a single sequence/algorithm"""
def compose(turns: list[Callable]) -> Callable:                       #closure, function composition. functional programming here
    def composed(cube_array: list) -> list:
        permutated_cube_array = cube_array
        for turn in turns:
            permutated_cube_array = turn(cube_array)
        return permutated_cube_array
    return composed

scramble_algo_str_json = ""     #global variable for json
"""Generationg a random set of 20 turns (scramble algorithm)"""
def generate_scramble() -> list[Callable]:
    all_turns = [f, f2, fp, l, l2, lp, r, r2, rp, b, b2, bp, u, u2, up, d, d2, dp]
    random.shuffle(all_turns)
    scramble_algo: list[Callable] = []
    for i in range(20):
        scramble_algo.append(secrets.choice(all_turns))
    random.shuffle(scramble_algo)
    for k in range(1, len(scramble_algo)):
        while scramble_algo[k].__name__[0] == scramble_algo[k-1].__name__[0]:
            scramble_algo[k] = random.choice(all_turns)
    for q in range(2, len(scramble_algo)):
        while scramble_algo[q].__name__[0] == scramble_algo[q-2].__name__[0] or scramble_algo[q].__name__[0] == scramble_algo[q-1].__name__[0]:
            scramble_algo[q] = random.choice(all_turns)
    for p in range(1, len(scramble_algo)):
        while scramble_algo[p].__name__[0] == scramble_algo[p-1].__name__[0]:
            scramble_algo[p] = random.choice(all_turns)

    return scramble_algo
    

"""Outputting a scramble algorithm"""
def get_scramble(scramble_algo_obj: list[Callable]) -> str:
    scramble_algo_str_list: list[str] = [i.__name__.upper() for i in scramble_algo_obj]        #Getting the names of the function in upper case
    #reveal_type(scramble_algo_str_list)

    scramble_algo_str = ""
    for j in scramble_algo_str_list:
        if "P" in j:
            j = j.replace("P", "\'")        #Replacing all the "P" (means prime or 90° anti-clockwise) to ', e.g. FP → F'
        scramble_algo_str += f"{j} " #if i != scramble_algo_str_list[19] else f"{i}"              # creating a string with all the turns of a scramble, if expression here for functional programming

    global scramble_algo_str_json
    scramble_algo_str_json = scramble_algo_str

    return scramble_algo_str

"""Composing an applying a scramble algorithm to a cube"""
def apply_scramble(scramble_algo: list[Callable], cube_array: list[list[str]]) -> list[list[str]]:
    return compose(scramble_algo)(cube_array)        #Applying the scramble to a cube



if __name__ == "__main__":
    cube = create_facelets(3)
    print(create_2D(cube))
    initial_cube_json = pack_into_string(cube)   # for JSON

    scramble = generate_scramble()
    print(f"Scramble: {get_scramble(scramble)}")
    apply_scramble(scramble, cube)
    print(create_2D(cube))
    scrambled_cube_json = pack_into_string(cube)     # for JSON

    scramble_data = {"Initial_cube": initial_cube_json,
                     "Scramble": scramble_algo_str_json,
                     "Scrambled_cube": scrambled_cube_json}

    print("JSON")
    print(json.dumps(scramble_data))
