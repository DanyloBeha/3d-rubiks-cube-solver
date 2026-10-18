"""
This file is the realization of the begginer-fridrich solving method, i.e. the translation of human intuitive-algorithmic method into code

In short about how human algorithm works:
1. We solve the cross on one of the sides (usually the bottom side):
            __________
           |          |
           |    U5    |
           |          |
 __________|__________|__________ __________
|          |          |          |          |
|    L5    |    F5    |    R5    |    B5    |
|    L8    |    F8    |    R8    |    B8    |
|__________|__________|__________|__________|
           |    D2    |
           | D4 D5 D6 |
           |    D8    |
           |__________|

2. We solve the first layer by inserting the corners:
            __________
           |          |
           |    U5    |
           |          |
 __________|__________|__________ __________
|          |          |          |          |
|    L5    |    F5    |    R5    |    B5    |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | D1 D2 D3 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

3. We solve the second layer (together the first 3 steps are called F2L - "First 2 Layers")
            __________
           |          |
           |    U5    |
           |          |
 __________|__________|__________ __________
|          |          |          |          |
| L4 L5 L6 | F4 F5 F6 | R4 R5 R6 | B4 B5 B6 |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | D1 D2 D3 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

4. We solve the cross on last layer (first step of the OLL)
            __________
           |    U     |
           | U  U5 U  |
           |    U     |
 __________|__________|__________ __________
|          |          |          |          |
| L4 L5 L6 | F4 F5 F6 | R4 R5 R6 | B4 B5 B6 |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | D1 D2 D3 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

5. OOL ("Orientation of the Last Layer"): We orientate all the pieces on the final layer with upper color to the upper side, e.g. all facelets will look yellow on the top of the upper side is yellow
            __________
           | U  U  U  |
           | U  U  U  |
           | U  U  U  |
 __________|__________|__________ __________
|          |          |          |          |
| L4 L5 L6 | F4 F5 F6 | R4 R5 R6 | B4 B5 B6 |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | D1 D2 D3 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

6. We solve PLL cross
            __________
           | U  U2 U  |
           | U4 U5 U6 |
           | U  U8 U  |
 __________|__________|__________ __________
|    L2    |    F3    |    R2    |    B2    |
| L4 L5 L6 | F4 F5 F6 | R4 R5 R6 | B4 B5 B6 |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | D1 D2 D3 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

7. PLL ("Permutation of the Last Layer"): We permutate all the pieces in the last layer so that the cube is solved
            __________
           | U1 U2 U3 |
           | U4 U5 U6 |
           | U7 U8 U9 |
 __________|__________|__________ __________
| L1 L2 L3 | F1 F3 F3 | R1 R2 R3 | B1 B2 B3 |
| L4 L5 L6 | F4 F5 F6 | R4 R5 R6 | B4 B5 B6 |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | D1 D2 D3 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

The solving function should return a string to solve the cube and do not permutate the cube itself
"""
from turns import *
from Facelets import *
from scramble import *
import time
from typing import Callable
#import tracemalloc
#from functools import lru_cache



"""Make a function to find an index of an element"""
def find_index(facelet: str, proxy_cube) -> list[int]:
    for i in range(6):
        if facelet in proxy_cube[i]:
            index = [i, proxy_cube[i].index(facelet)]
    return index



"""-------THE function (human-like layer by layer solving)-------"""
def solve_with_fridrich(cube_array: list[list[str]]) -> list[Callable]:

    solving_algo = []  # list in which we will add the moves from temporary_algo
    temporary_algo = []  # list which will store moves only for current permutation

    """Creating a proxy cube which will be permuitated so that we don't touch the original cube"""
    proxy_cube: list[list] = [[], [], [], [], [], []]
    for i in range(len(cube_array)):
        for j in range(len(cube_array[i])):
            proxy_cube[i].append(cube_array[i][j])




    """-------Solving the cross-------"""
    """Nested match-case in match-case may seem a bit frightening, but we are dealing with
       hand-crafted permutations for 2D list and this is the only way to get to the face level"""

    # finding how to put D2 in it's place
    D2_index = find_index("D2", proxy_cube)

    match D2_index[0]:
        case 0:
            match D2_index[1]:
                case 1:
                    temporary_algo.extend([u2, f2])
                case 3:
                    temporary_algo.extend([up, f2])
                case 5:
                    temporary_algo.extend([u, f2])
                case 7:
                    temporary_algo.extend([f2])
        case 1:
            match D2_index[1]:
                case 1:
                    temporary_algo.extend([l, fp])
                case 3:
                    temporary_algo.extend([l2, fp])
                case 5:
                    temporary_algo.extend([fp])
                case 7:
                    temporary_algo.extend([lp, fp])
        case 2:
            match D2_index[1]:
                case 1:
                    temporary_algo.extend([f, rp, dp])
                case 3:
                    temporary_algo.extend([l, d])
                case 5:
                    temporary_algo.extend([rp, dp])
                case 7:
                    temporary_algo.extend([fp, rp, dp])
        case 3:
            match D2_index[1]:
                case 1:
                    temporary_algo.extend([rp, f])
                case 3:
                    temporary_algo.extend([f])
                case 5:
                    temporary_algo.extend([r2, f])
                case 7:
                    temporary_algo.extend([r, f])
        case 4:
            match D2_index[1]:
                case 1:
                    temporary_algo.extend([bp, r, dp])
                case 3:
                    temporary_algo.extend([r, dp])
                case 5:
                    temporary_algo.extend([lp, d])
                case 7:
                    temporary_algo.extend([b, r, dp])
        case 5:
            match D2_index[1]:
                # in case 1 D2 is already in place
                case 3:
                    temporary_algo.extend([d])
                case 5:
                    temporary_algo.extend([dp])
                case 7:
                    temporary_algo.extend([d2])
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put D4 in it's place without messing up D2
    D4_index = find_index("D4", proxy_cube)

    match D4_index[0]:
        case 0:
            match D4_index[1]:
                case 1:
                    temporary_algo.extend([up, l2])
                case 3:
                    temporary_algo.extend([l2])
                case 5:
                    temporary_algo.extend([u2, l2])
                case 7:
                    temporary_algo.extend([u, l2])
        case 1:
            match D4_index[1]:
                case 1:
                    temporary_algo.extend([u, b, lp])
                case 3:
                    temporary_algo.extend([bp, up, l2])
                case 5:
                    temporary_algo.extend([fp, dp, f])
                case 7:
                    temporary_algo.extend([lp, fp, dp, f])
        case 2:
            match D4_index[1]:
                case 1:
                    temporary_algo.extend([fp, l, f])
                case 3:
                    temporary_algo.extend([l])
                case 5:
                    temporary_algo.extend([f2, l, f2])
                # case 7 is impossible since F8 is already there
        case 3:
            match D4_index[1]:
                case 1:
                    temporary_algo.extend([rp, f, dp, fp])
                case 3:
                    temporary_algo.extend([f, dp, fp])
                case 5:
                    temporary_algo.extend([b, up, l2])
                case 7:
                    temporary_algo.extend([r, f, dp, fp])
        case 4:
            match D4_index[1]:
                case 1:
                    temporary_algo.extend([b, lp])
                case 3:
                    temporary_algo.extend([b2, lp])
                case 5:
                    temporary_algo.extend([lp])
                case 7:
                    temporary_algo.extend([bp, lp])
        case 5:
            match D4_index[1]:
                # case 1 is impossible since D2 is already there
                # in case 3 D4 is already in place
                case 5:
                    temporary_algo.extend([rp, b2, lp])
                case 7:
                    temporary_algo.extend([f, d, fp])

    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put D6 in it's place without messing up D2 and D4
    D6_index = find_index("D6", proxy_cube)

    match D6_index[0]:
        case 0:
            match D6_index[1]:
                case 1:
                    temporary_algo.extend([u, r2])
                case 3:
                    temporary_algo.extend([u2, r2])
                case 5:
                    temporary_algo.extend([r2])
                case 7:
                    temporary_algo.extend([up, r2])
        case 1:
            match D6_index[1]:
                case 1:
                    temporary_algo.extend([u, bp, r])
                case 3:
                    temporary_algo.extend([bp, u, r2])
                case 5:
                    temporary_algo.extend([fp, lp, d, l, f])
                # case 7 is impossible since L8 is already there
        case 2:
            match D6_index[1]:
                case 1:
                    temporary_algo.extend([f, rp, fp])
                case 3:
                    temporary_algo.extend([f2, rp, f2])
                case 5:
                    temporary_algo.extend([rp])
                # case 7 is impossible since F8 is already there
        case 3:
            match D6_index[1]:
                case 1:
                    temporary_algo.extend([up, bp, r])
                case 3:
                    temporary_algo.extend([r, up, bp, r])
                case 5:
                    temporary_algo.extend([rp, up, bp, r])
                case 7:
                    temporary_algo.extend([r2, up, bp, r])
        case 4:
            match D6_index[1]:
                case 1:
                    temporary_algo.extend([bp, r])
                case 3:
                    temporary_algo.extend([r])
                case 5:
                    temporary_algo.extend([b2, r])
                case 7:
                    temporary_algo.extend([b, r])
        case 5:
            match D6_index[1]:
                # in case 1 D2 is already in place
                # in case 3 D4 is already in place
                # in case 5 D6 is already in place
                case 7:
                    temporary_algo.extend([b2, u, r2])
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put D8 in it's place without messing up D2, D4 and D6
    D8_index = find_index("D8", proxy_cube)

    match D8_index[0]:
        case 0:
            match D8_index[1]:
                case 1:
                    temporary_algo.extend([b2])
                case 3:
                    temporary_algo.extend([u, b2])
                case 5:
                    temporary_algo.extend([up, b2])
                case 7:
                    temporary_algo.extend([u2, b2])
        case 1:
            match D8_index[1]:
                case 1:
                    temporary_algo.extend([lp, b, l])
                case 3:
                    temporary_algo.extend([b])
                case 5:
                    temporary_algo.extend([l2, b, l2])
                # case 7 is impossible since L8 is already there
        case 2:
            match D8_index[1]:
                case 1:
                    temporary_algo.extend([u, lp, b, l])
                case 3:
                    temporary_algo.extend([lp, u, b2, l])
                case 5:
                    temporary_algo.extend([r, up, b2, rp])
                # case 7 is impossible since F8 is already there
        case 3:
            match D8_index[1]:
                case 1:
                    temporary_algo.extend([r, bp, rp])
                case 3:
                    temporary_algo.extend([r2, bp, r2])
                case 5:
                    temporary_algo.extend([bp])
                # case 7 is impossible since R8 is already there
        case 4:
            match D8_index[1]:
                case 1:
                    temporary_algo.extend([u, r, bp, rp])
                case 3:
                    temporary_algo.extend([b, u, r, bp, rp])
                case 5:
                    temporary_algo.extend([bp, u, r, bp, rp])
                case 7:
                    temporary_algo.extend([b2, u, r, bp, rp])
        # in case 5 D2, D4, D6 and D8 are already in place
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()




    """-------Solving the first layer by inserting the corners-------"""
    # finding how to put D1 in it's place
    D1_index = find_index("D1", proxy_cube)

    match D1_index[0]:
        case 0:
            match D1_index[1]:
                case 0:
                    temporary_algo.extend([l, up, l2, u, l])
                case 2:
                    temporary_algo.extend([u, fp, u, f2, up, fp])
                case 6:
                    temporary_algo.extend([up, fp, u, f2, up, fp])
                case 8:
                    temporary_algo.extend([fp, u, f2, up, fp])
        case 1:
            match D1_index[1]:
                case 0:
                    temporary_algo.extend([u2, lp, u, l])
                case 2:
                    temporary_algo.extend([u, f, up, fp])
                case 6:
                    temporary_algo.extend([l, u, l2, u2, l])
                case 8:
                    temporary_algo.extend([fp, l, f, lp]*2)
        case 2:
            match D1_index[1]:
                case 0:
                    temporary_algo.extend([up, lp, u, l])
                case 2:
                    temporary_algo.extend([u2, f, up, fp])
                case 6:
                    temporary_algo.extend([f, u, fp, up, f, u, fp])
                case 8:
                    temporary_algo.extend([fp, u2, f2, up, fp])
        case 3:
            match D1_index[1]:
                case 0:
                    temporary_algo.extend([lp, u, l])
                case 2:
                    temporary_algo.extend([f, u2, fp])
                case 6:
                    temporary_algo.extend([lp, r, u, l, rp])
                case 8:
                    temporary_algo.extend([rp, f, u2, fp, r])
        case 4:
            match D1_index[1]:
                case 0:
                    temporary_algo.extend([lp, u2, l])
                case 2:
                    temporary_algo.extend([f, up, fp])
                case 6:
                    temporary_algo.extend([b, lp, u2, l, bp])
                case 8:
                    temporary_algo.extend([bp, f, up, fp, b])
        case 5:
            match D1_index[1]:
                # in case 0 D1 is already in place
                case 2:
                    temporary_algo.extend([r, u, rp, u, f, up, fp])
                case 6:
                    temporary_algo.extend([bp, up, b, up, lp, u, l])
                case 8:
                    temporary_algo.extend([b, u, bp, u2, f, up, fp])
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put D3 in it's place without messing up cross and D1
    D3_index = find_index("D3", proxy_cube)

    match D3_index[0]:
        case 0:
            match D3_index[1]:
                case 0:
                    temporary_algo.extend([l, up, lp, up, fp, u, f])
                case 2:
                    temporary_algo.extend([rp, u, r2, up, rp])
                case 6:
                    temporary_algo.extend([up, fp, u, f, r, u2, rp])
                case 8:
                    temporary_algo.extend([fp, u, f, r, u2, rp])
        case 1:
            match D3_index[1]:
                case 0:
                    temporary_algo.extend([fp, u2, f])
                case 2:
                    temporary_algo.extend([r, up, rp])
                case 6:
                    temporary_algo.extend([l, u, lp, fp, u, f])
                # case 8 is impossible since L9 is already there
        case 2:
            match D3_index[1]:
                case 0:
                    temporary_algo.extend([u2, fp, u, f])
                case 2:
                    temporary_algo.extend([u, r, up, rp])
                # case 6 is impossible since F7 is already there
                case 8:
                    temporary_algo.extend([rp, f, r, fp]*2)
        case 3:
            match D3_index[1]:
                case 0:
                    temporary_algo.extend([up, fp, u, f])
                case 2:
                    temporary_algo.extend([u2, r, up, rp])
                case 6:
                    temporary_algo.extend([r, u, rp, up, r, u, rp])
                case 8:
                    temporary_algo.extend([rp, up, r2, u2, rp])
        case 4:
            match D3_index[1]:
                case 0:
                    temporary_algo.extend([fp, u, f])
                case 2:
                    temporary_algo.extend([r, u2, rp])
                case 6:
                    temporary_algo.extend([b, u, bp, up, fp, u, f])
                case 8:
                    temporary_algo.extend([bp, up, b, r, up, rp])
        case 5:
            match D3_index[1]:
                # in case 0 D1 is already in place
                # in case 2 D3 is already in place
                case 6:
                    temporary_algo.extend([l, u, lp, up, r, u2, rp])
                case 8:
                    temporary_algo.extend([rp, up, r, fp, u2, f])
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put D7 in it's place without messing up cross, D1 and D3
    D7_index = find_index("D7", proxy_cube)

    match D7_index[0]:
        case 0:
            match D7_index[1]:
                case 0:
                    temporary_algo.extend([l, up, lp, bp, u2, b])
                case 2:
                    temporary_algo.extend([b, up, b2, u, b])
                case 6:
                    temporary_algo.extend([u, l, up, lp, bp, u2, b])
                case 8:
                    temporary_algo.extend([up, b, up, b2, u, b])
        case 1:
            match D7_index[1]:
                case 0:
                    temporary_algo.extend([up, bp, u, b])
                case 2:
                    temporary_algo.extend([up, l, u2, lp])
                case 6:
                    temporary_algo.extend([l, u, lp, up, l, u, lp])
                # case 8 is impossible since L9 is already there
        case 2:
            match D7_index[1]:
                case 0:
                    temporary_algo.extend([bp, u, b])
                case 2:
                    temporary_algo.extend([l, u2, lp])
                # case 6 is impossible since F7 is already there
                # case 8 is impossible since F9 is already there
        case 3:
            match D7_index[1]:
                case 0:
                    temporary_algo.extend([bp, u2, b])
                case 2:
                    temporary_algo.extend([l, up, lp])
                # case 6 is impossible since R7 is already there
                case 8:
                    temporary_algo.extend([rp, l, up, lp, r])
        case 4:
            match D7_index[1]:
                case 0:
                    temporary_algo.extend([u, bp, u2, b])
                case 2:
                    temporary_algo.extend([u, l, up, lp])
                case 6:
                    temporary_algo.extend([b, u, b2, u2, b])
                case 8:
                    temporary_algo.extend([bp, u2, b, l, u2, lp])
        case 5:
            match D7_index[1]:
                # in case 0 D1 is already in place
                # in case 2 D3 is already in place
                # in case 7 D7 is already in place
                case 8:
                    temporary_algo.extend([b, u, bp, l, u2, lp])
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put D9 in it's place without messing up cross, D1 D3 and D7
    D9_index = find_index("D9", proxy_cube)

    match D9_index[0]:
        case 0:
            match D9_index[1]:
                case 0:
                    temporary_algo.extend([u, b, up, bp, rp, u2, r])
                case 2:
                    temporary_algo.extend([b, up, bp, rp, u2, r])
                case 6:
                    temporary_algo.extend([u2, b, up, bp, rp, u2, r])
                case 8:
                    temporary_algo.extend([up, b, up, bp, rp, u2, r])
        case 1:
            match D9_index[1]:
                case 0:
                    temporary_algo.extend([rp, u, r])
                case 2:
                    temporary_algo.extend([b, u2, bp])
                # case 6 is impossible since L7 is already there
                # case 8 is impossible since L9 is already there
        case 2:
            match D9_index[1]:
                case 0:
                    temporary_algo.extend([rp, u2, r])
                case 2:
                    temporary_algo.extend([b, up, bp])
                # case 6 is impossible since F7 is already there
                # case 8 is impossible since F9 is already there
        case 3:
            match D9_index[1]:
                case 0:
                    temporary_algo.extend([u, rp, u2, r])
                case 2:
                    temporary_algo.extend([u, b, up, bp])
                # case 6 is impossible since R7 is already there
                case 8:
                    temporary_algo.extend([rp, u2, r, b, u2, bp])
        case 4:
            match D9_index[1]:
                case 0:
                    temporary_algo.extend([up, rp, u, r])
                case 2:
                    temporary_algo.extend([u2, b, up, bp])
                case 6:
                    temporary_algo.extend([b, u, bp, u, rp, u2, r])
                # case 8 is impossible since B9 is already there
        # in case 5 the first layer is solved
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()




    """-------Solving the second layer-------"""
    # finding how to put F4-L6 edge in it's place
    F4_index = find_index("F4", proxy_cube)

    match F4_index[0]:
        case 0:
            match F4_index[1]:
                case 1:
                    temporary_algo.extend([f, up, fp, up, lp, u, l])
                case 3:
                    temporary_algo.extend([u, f, up, fp, up, lp, u, l])   # basic edge piece insert algo
                case 5:
                    temporary_algo.extend([up, f, up, fp, up, lp, u, l])
                case 7:
                    temporary_algo.extend([u2, f, up, fp, up, lp, u, l])
        case 1:
            match F4_index[1]:
                case 1:
                    temporary_algo.extend([u2, lp, u, l, u, f, up, fp])
                case 3:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp, up, f, up, fp, up, lp, u, l]) # insert L2 to L4: up, bp, u, b, u, l, up, lp
                case 5:
                    temporary_algo.extend([up, lp, u, l, u, f, up, fp, u, lp, u, l, u, f, up, fp])
        case 2:
            match F4_index[1]:
                case 1:
                    temporary_algo.extend([up, lp, u, l, u, f, up, fp])   # basic edge piece insert algo
                # in case 3 F4 is already in place
                case 5:
                    temporary_algo.extend([u, r, up, rp, up, fp, u, f2, up, fp, up, lp, u, l]) # insert F2 to F6: u, r, up, rp, up, fp, u, f
        case 3:
            match F4_index[1]:
                case 1:
                    temporary_algo.extend([lp, u, l, u, f, up, fp])
                case 3:
                    temporary_algo.extend([u, r, up, rp, up, fp, u, f, u, lp, u, l, u, f, up, fp])
                case 5:
                    temporary_algo.extend([u, b, up, bp, up, rp, u, r, u, f, up, fp, up, lp, u, l]) # insert R2 to R6: u, b, up, bp, up, rp, u, r
        case 4:
            match F4_index[1]:
                case 1:
                    temporary_algo.extend([u, lp, u, l, u, f, up, fp])
                case 3:
                    temporary_algo.extend([u, b, up, bp, up, rp, u, r, u2, lp, u, l, u, f, up, fp])
                case 5:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp, lp, u, l, u, f, up, fp]) # insert L2 to L4: up, bp, u, b, u, l, up, lp
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put R4-F6 edge in it's place
    F6_index = find_index("F6", proxy_cube)

    match F6_index[0]:
        case 0:
            match F6_index[1]:
                case 1:
                    temporary_algo.extend([fp, u, f, u, r, up, rp])
                case 3:
                    temporary_algo.extend([u, fp, u, f, u, r, up, rp])
                case 5:
                    temporary_algo.extend([up, fp, u, f, u, r, up, rp])   # insert R2 to R4
                case 7:
                    temporary_algo.extend([u2, fp, u, f, u, r, up, rp])
        case 1:
            match F6_index[1]:
                case 1:
                    temporary_algo.extend([r, up, rp, up, fp, u, f])
                case 3:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp, up, fp, u, f, u, r, up, rp]) # insert L2 to L4: up, bp, u, b, u, l, up, lp
                # case 5 is impossible since L6 is already there
        case 2:
            match F6_index[1]:
                case 1:
                    temporary_algo.extend([u, r, up, rp, up, fp, u, f])   # insert F2 to F6
                # case 3 is impossible since F4 is already there
                # in case 5 F6 is in it's place
        case 3:
            match F6_index[1]:
                case 1:
                    temporary_algo.extend([u2, r, up, rp, up, fp, u, f])
                case 3:
                    temporary_algo.extend([up, fp, u, f, u, r, up, rp, u, fp, u, f, u, r, up, rp])
                case 5:
                    temporary_algo.extend([u, b, up, bp, up, rp, u, r, u, fp, u, f, u, r, up, rp]) # insert R2 to R6: u, b, up, bp, up, rp, u, r
        case 4:
            match F6_index[1]:
                case 1:
                    temporary_algo.extend([up, r, up, rp, up, fp, u, f])
                case 3:
                    temporary_algo.extend([u, b, up, bp, up, rp, u, r2, up, rp, up, fp, u, f])
                case 5:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp, u2, r, up, rp, up, fp, u, f]) # insert L2 to L4: up, bp, u, b, u, l, up, lp
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put B4-R6 edge in it's place
    R6_index = find_index("R6", proxy_cube)

    match R6_index[0]:
        case 0:
            match R6_index[1]:
                case 1:
                    temporary_algo.extend([up, rp, u, r, u, b, up, bp]) # insert B2 to B4
                case 3:
                    temporary_algo.extend([rp, u, r, u, b, up, bp])
                case 5:
                    temporary_algo.extend([u2, rp, u, r, u, b, up, bp])
                case 7:
                    temporary_algo.extend([u, rp, u, r, u, b, up, bp])
        case 1:
            match R6_index[1]:
                case 1:
                    temporary_algo.extend([up, b, up, bp, up, rp, u, r])
                case 3:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp, u2, rp, u, r, u, b, up, bp]) # insert L2 to L4: up, bp, u, b, u, l, up, lp
                # case 5 is impossible since L6 is already there
        case 2:
            match R6_index[1]:
                case 1:
                    temporary_algo.extend([b, up, bp, up, rp, u, r])
                # case 3 is impossible since F4 is already there
                # in case 5 F6 is in it's place
        case 3:
            match R6_index[1]:
                case 1:
                    temporary_algo.extend([u, b, up, bp, up, rp, u, r])
                # case 3 is impossible since R4 is already there
                # in case 5 R6 is in it's plac
        case 4:
            match R6_index[1]:
                case 1:
                    temporary_algo.extend([u2, b, up, bp, up, rp, u, r])
                case 3:
                    temporary_algo.extend([u, b, up, bp, up, rp, u, r, up, b, up, bp, up, rp, u, r])
                case 5:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp, u, b, up, bp, up, rp, u, r]) # insert L2 to L4: up, bp, u, b, u, l, up, lp
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to put L4-B6 edge in it's place
    L4_index = find_index("L4", proxy_cube)

    match L4_index[0]:
        case 0:
            match L4_index[1]:
                case 1:
                    temporary_algo.extend([u, l, up, lp, up, bp, u, b]) # insert L2 to L4
                case 3:
                    temporary_algo.extend([u2, l, up, lp, up, bp, u, b])
                case 5:
                    temporary_algo.extend([l, up, lp, up, bp, u, b])
                case 7:
                    temporary_algo.extend([up, l, up, lp, up, bp, u, b])
        case 1:
            match L4_index[1]:
                case 1:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp])
                # in case 3 L4 is in it's place
                # case 5 is impossible since L6 is already there
        case 2:
            match L4_index[1]:
                case 1:
                    temporary_algo.extend([bp, u, b, u, l, up, lp])
                # case 3 is impossible since F4 is already there
                # in case 5 F6 is in it's place
        case 3:
            match L4_index[1]:
                case 1:
                    temporary_algo.extend([u, bp, u, b, u, l, up, lp])
                # case 3 is impossible since R4 is already there
                # in case 5 R6 is in it's plac
        case 4:
            match L4_index[1]:
                case 1:
                    temporary_algo.extend([u2, bp, u, b, u, l, up, lp])
                # case 3 is impossible since B4 is already there
                case 5:
                    temporary_algo.extend([up, bp, u, b, u, l, up, lp, u, bp, u, b, u, l, up, lp]) # insert L2 to L4: up, bp, u, b, u, l, up, lp
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to solve upper cross
    upper_side = proxy_cube[0][1][0] + proxy_cube[0][3][0] + proxy_cube[0][5][0] + proxy_cube[0][7][0] # e.g. upper_side: UUUU or FRLB

    match upper_side.count("U"):
        case 0:
            temporary_algo.extend([f, r, u, rp, up, fp, b, u, l, up, lp, bp])
        # case 1 is impossible due to rubik's cube mechanics
        case 2:
            if upper_side[2:] == "UU":
                temporary_algo.extend([b, u, l, up, lp, bp])
            elif upper_side[:2] == "UU":
                temporary_algo.extend([u2, b, u, l, up, lp, bp])
            elif upper_side[1] == "U" and upper_side[3] == "U":
                temporary_algo.extend([up, b, u, l, up, lp, bp])
            elif upper_side[0] == "U" and upper_side[3] == "U":
                temporary_algo.extend([u, f, r, u, rp, up, fp])
            elif upper_side[1] == "U" and upper_side[2] == "U":
                temporary_algo.extend([f, r, u, rp, up, fp])
            else:
                temporary_algo.extend([u, b, u, l, up, lp, bp])
        # case 3 is impossible due to rubik's cube mechanics
        # in case 4 upper cross is already solved
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to solve OLL
    upper_side = ""
    for j in range(9):
        upper_side += proxy_cube[0][j][0] # e.g. solved upper_side: UUUUUUUUU

    match upper_side.count("U"):
        case 5:
            if proxy_cube[1][0][0] == "U" and proxy_cube[1][2][0] == "U" and proxy_cube[3][2][0] == "U":
                temporary_algo.extend([r, u, rp, u, r, up, rp, u, r, u2, rp])
            elif proxy_cube[4][0][0] == "U" and proxy_cube[4][2][0] == "U" and proxy_cube[2][2][0] == "U":
                temporary_algo.extend([u, r, u, rp, u, r, up, rp, u, r, u2, rp])
            elif proxy_cube[1][0][0] == "U" and proxy_cube[1][2][0] == "U" and proxy_cube[2][2][0] == "U":
                temporary_algo.extend([r, u2, r2, up, r2, up, r2, u2, r])
            elif proxy_cube[2][0][0] == "U" and proxy_cube[2][2][0] == "U" and proxy_cube[3][2][0] == "U":
                temporary_algo.extend([u, r, u2, r2, up, r2, up, r2, u2, r])
            elif proxy_cube[3][0][0] == "U" and proxy_cube[3][2][0] == "U" and proxy_cube[4][2][0] == "U":
                temporary_algo.extend([u2, r, u2, r2, up, r2, up, r2, u2, r])
            else:
                temporary_algo.extend([up, r, u2, r2, up, r2, up, r2, u2, r])
        case 6:
            if proxy_cube[1][0][0] == "U" or proxy_cube[2][0][0] == "U":
                if proxy_cube[0][2][0] == "U":
                    temporary_algo.extend([u, lp, up, l, up, lp, u2, l])
                elif proxy_cube[0][0][0] == "U":
                    temporary_algo.extend([u2, lp, up, l, up, lp, u2, l])
                elif proxy_cube[0][6][0] == "U":
                    temporary_algo.extend([up, lp, up, l, up, lp, u2, l])
                else:
                    temporary_algo.extend([lp, up, l, up, lp, u2, l])
            else:
                if proxy_cube[0][0][0] == "U":
                    temporary_algo.extend([up, r, u, rp, u, r, u2, rp])
                elif proxy_cube[0][2][0] == "U":
                    temporary_algo.extend([u2, r, u, rp, u, r, u2, rp])
                elif proxy_cube[0][8][0] == "U":
                    temporary_algo.extend([u, r, u, rp, u, r, u2, rp])
                else:
                    temporary_algo.extend([r, u, rp, u, r, u2, rp])
        case 7:
            if proxy_cube[0][0][0] == proxy_cube[0][8][0] or proxy_cube[0][2][0] == proxy_cube[0][6][0]:
                if proxy_cube[1][2][0] == "U":
                    temporary_algo.extend([u2, rp, f, r, bp, rp, fp, r, b])
                elif proxy_cube[1][0][0] == "U":
                    temporary_algo.extend([up, rp, f, r, bp, rp, fp, r, b])
                elif proxy_cube[3][0][0] == "U":
                    temporary_algo.extend([u, rp, f, r, bp, rp, fp, r, b])
                else:
                    temporary_algo.extend([rp, f, r, bp, rp, fp, r, b])
            else:
                if proxy_cube[1][0][0] == "U" and proxy_cube[1][2][0] == "U":
                    temporary_algo.extend([up, r2, d, rp, u2, r, dp, rp, u2, rp])
                elif proxy_cube[2][0][0] == "U" and proxy_cube[2][2][0] == "U":
                    temporary_algo.extend([r2, d, rp, u2, r, dp, rp, u2, rp])
                elif proxy_cube[3][0][0] == "U" and proxy_cube[3][2][0] == "U":
                    temporary_algo.extend([u, r2, d, rp, u2, r, dp, rp, u2, rp])
                elif proxy_cube[4][0][0] == "U" and proxy_cube[4][2][0] == "U":
                    temporary_algo.extend([r2, dp, r, u2, rp, d, r, u2, r])
                elif proxy_cube[2][2][0] == "U" and proxy_cube[4][0][0] == "U":
                    temporary_algo.extend([rp, fp, l, f, r, fp, lp, f])
                elif proxy_cube[1][2][0] == "U" and proxy_cube[3][0][0] == "U":
                    temporary_algo.extend([up, rp, fp, l, f, r, fp, lp, f])
                elif proxy_cube[4][2][0] == "U" and proxy_cube[2][0][0] == "U":
                    temporary_algo.extend([u2, rp, fp, l, f, r, fp, lp, f])
                elif proxy_cube[3][2][0] == "U" and proxy_cube[1][0][0] == "U":
                    temporary_algo.extend([u, rp, fp, l, f, r, fp, lp, f])
        # case 8 is impossible, in case 9 OLL is solved
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()


    # finding how to solve PLL cross
    U2_index = proxy_cube[0].index("U2")
    U4_index = proxy_cube[0].index("U4")
    U6_index = proxy_cube[0].index("U6")
    U8_index = proxy_cube[0].index("U8")

    upper_side = proxy_cube[0]
    #check if not solved already
    if U2_index == 1 and U4_index == 3 and U6_index == 5 and U8_index == 7:
        pass
    elif U2_index == 5 and U4_index == 1 and U6_index == 7 and U8_index == 3:
        temporary_algo.append(up)
    elif U2_index == 7 and U4_index == 5 and U6_index == 3 and U8_index == 1:
        temporary_algo.append(u2)
    elif U2_index == 3 and U4_index == 7 and U6_index == 1 and U8_index == 5:
        temporary_algo.append(u)
    
    #t-perm
    elif U2_index == 1 and U8_index == 7:
        temporary_algo.extend([r, u, rp, up, rp, f, r2, up, rp, up, r, u, rp, fp])
    elif U2_index == 7 and U8_index == 1:
        temporary_algo.extend([u2, r, u, rp, up, rp, f, r2, up, rp, up, r, u, rp, fp])
    elif U2_index == 3 and U8_index == 5:
        temporary_algo.extend([u, r, u, rp, up, rp, f, r2, up, rp, up, r, u, rp, fp])
    elif U2_index == 5 and U8_index == 3:
        temporary_algo.extend([up, r, u, rp, up, rp, f, r2, up, rp, up, r, u, rp, fp])

    #y-perm
    #when U2 and U6 are in place
    elif U2_index == 1 and U6_index == 5:
        temporary_algo.extend([u, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, up])
    elif U2_index == 3 and U6_index == 1:
        temporary_algo.extend([u2, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, up])
    elif U2_index == 7 and U6_index == 3:
        temporary_algo.extend([up, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, up])
    elif U2_index == 5 and U6_index == 7:
        temporary_algo.extend([f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, up])
    #when U6 and U8 are in place
    elif U6_index == 1 and U8_index == 5:
        temporary_algo.extend([u, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp])
    elif U6_index == 3 and U8_index == 1:
        temporary_algo.extend([u2, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp])
    elif U6_index == 7 and U8_index == 3:
        temporary_algo.extend([up, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp])
    elif U6_index == 5 and U8_index == 7:
        temporary_algo.extend([f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp])
    #when U8 and U4 are in place
    elif U8_index == 1 and U4_index == 5:
        temporary_algo.extend([u, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u])
    elif U8_index == 3 and U4_index == 1:
        temporary_algo.extend([u2, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u])
    elif U8_index == 7 and U4_index == 3:
        temporary_algo.extend([up, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u])
    elif U8_index == 5 and U4_index == 7:
        temporary_algo.extend([f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u])
    #when U4 and U2 are in place
    elif U4_index == 1 and U2_index == 5:
        temporary_algo.extend([u, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u2])
    elif U4_index == 3 and U2_index == 1:
        temporary_algo.extend([u2, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u2])
    elif U4_index == 7 and U2_index == 3:
        temporary_algo.extend([up, f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u2])
    elif U4_index == 5 and U2_index == 7:
        temporary_algo.extend([f, r, up, rp, up, r, u, rp, fp, r, u, rp, up, rp, f, r, fp, u2])
    
    
    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()
    

    # finding how to solve PLL
    U1_index = proxy_cube[0].index("U1")
    U3_index = proxy_cube[0].index("U3")
    U7_index = proxy_cube[0].index("U7")
    U9_index = proxy_cube[0].index("U9")

    #check if not solved already
    if U1_index == 0 and U3_index == 2 and U7_index == 6 and U9_index == 8:
        pass
    
    #ckeck for h-perm
    elif U1_index == 8 and U3_index == 6 and U7_index == 2 and U9_index == 0:
        temporary_algo.extend([u2, r2, l2, d, r2, l2, u2, r2, l2, d, r2, l2])

    #check for horizontal e-perm
    elif U1_index == 2 and U3_index == 0 and U7_index == 8 and U9_index == 6:
        temporary_algo.extend([l, up, r, d2, rp, u, lp, r, up, l, d2, lp, u, rp])
    
    #check for verical e-perm
    elif U1_index == 6 and U3_index == 8 and U7_index == 0 and U9_index == 2:
        temporary_algo.extend([u, l, up, r, d2, rp, u, lp, r, up, l, d2, lp, u, rp, up])

    #check for a-perm
    #when U9 is in place
    elif U9_index == 8:
        if U3_index == 6:
            temporary_algo.extend([l, fp, l, b2, lp, f, l, b2, l2])
        elif U3_index == 0:
            temporary_algo.extend([u, rp, f, rp, b2, r, fp, rp, b2, r2, up])
    #when U7 is in place
    elif U7_index == 6:
        if U3_index == 0:
            temporary_algo.extend([rp, f, rp, b2, r, fp, rp, b2, r2])
        elif U3_index == 8:
            temporary_algo.extend([up, l, fp, l, b2, lp, f, l, b2, l2, u])
    #when U3 is in place
    elif U3_index == 2:
        if U1_index == 6:
            temporary_algo.extend([u2, rp, f, rp, b2, r, fp, rp, b2, r2, u2])
        elif U1_index == 8:
            temporary_algo.extend([u, l, fp, l, b2, lp, f, l, b2, l2, up])
    #when U1 is in place
    elif U1_index == 0:
        if U3_index == 6:
            temporary_algo.extend([up, rp, f, rp, b2, r, fp, rp, b2, r2, u])
        elif U3_index == 8:
            temporary_algo.extend([u2, l, fp, l, b2, lp, f, l, b2, l2, u2])
    

    compose(temporary_algo)(proxy_cube)   # apply those moves to proxy cube to solve it further
    solving_algo.extend(temporary_algo)   # add those moves to solving algo
    temporary_algo.clear()

    return solving_algo





if __name__ == "__main__":
    print("-"*20 + "Testing" + "-"*20)

    counter = 0
    solve_time = []
    solve_turns = []
    while True:
        cube = create_facelets(3)
        scramble = generate_scramble()
        apply_scramble(scramble, cube)

        beg_t = time.perf_counter()
        list_turns_to_solve = solve_with_fridrich(cube)
        end_t = time.perf_counter()
        solve_t = end_t-beg_t
        solve_time.append(solve_t)
        solve_turns.append(len(list_turns_to_solve))



        print(f"Solve: {list(map(lambda x: x.__name__.upper(), list_turns_to_solve))}")
        list_turn_to_solve_composed = compose(list_turns_to_solve)
        list_turn_to_solve_composed(cube)

        print(create_2D(cube))
        #tracemalloc.start()
        #print(tracemalloc.get_traced_memory())

        """Crash testing"""
        counter += 1
        print(f"⬆⬆⬆  {counter}  ⬆⬆⬆\n\n")
        if cube != create_facelets(3):
            print(f"Error in solve №{counter}")
            break
        elif counter == 5000:
            print("Successful")
            print(f"Average solve time: {sum(solve_time)/len(solve_time)}")
            print(f"Average solve length in turns: {sum(solve_turns)/len(solve_turns)}")
            print(f"Maximum solve length: {max(solve_turns)} and minimum: {min(solve_turns)}")

            #tracemalloc.stop()
            break
        
        #break
        #mypy final_project/fridrich.py
        
    
    