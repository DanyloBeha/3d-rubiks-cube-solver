"""
This file defines all the turns that can be applied to a cube

Info: let X be any side (e.g. U, L, F, R, B, D).
Then X is clockwise 90° turn of X side (i.e. as if we are facing that side)
X2 is 180° turn or X X
X' is anti-clockwise 90° turn or X X X
X' is read as X prime and we will call a function xp because ' is invalid for funcion name

We will define turns by defining the permuitation that these turns imply
We will use "is moved/carried to" logic

For example, this is our front side: ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9']
                                       ⬇      ⬇     ⬇     ⬇     ⬇     ⬇     ⬇     ⬇     ⬇
                                     toF3   toF6  toF9  toF2  toF5   toF8  toF1  toF4  toF7
                                       ⬇      ⬇     ⬇     ⬇     ⬇     ⬇     ⬇     ⬇     ⬇
And when we apply F turn we get:     ['F7', 'F4', 'F1', 'F8', 'F5', 'F2', 'F9', 'F6', 'F3']

But this is only for the front side, we will also have to define permutations for U, L, R and D sides (in the rows that are the closest to F side)

Let's bring an example and show the F permutation for a clear cube:

            __________
           | U1 U2 U3 |
           | U4 U5 U6 |
           | U7 U8 U9 |
 __________|__________|__________ __________
| L1 L2 L3 | F1 F2 F3 | R1 R2 R3 | B1 B2 B3 |
| L4 L5 L6 | F4 F5 F6 | R4 R5 R6 | B4 B5 B6 |
| L7 L8 L9 | F7 F8 F9 | R7 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | D1 D2 D3 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

F turn ⬇   ⬇   ⬇   ⬇   ⬇   ⬇   ⬇   ⬇   ⬇   ⬇ F turn

            __________
           | U1 U2 U3 |
           | U4 U5 U6 |
           | L9 L6 L3 |
 __________|__________|__________ __________
| L1 L2 D1 | F7 F4 F1 | U7 R2 R3 | B1 B2 B3 |
| L4 L5 D2 | F8 F5 F2 | U8 R5 R6 | B4 B5 B6 |
| L7 L8 D3 | F9 F6 F3 | U9 R8 R9 | B7 B8 B9 |
|__________|__________|__________|__________|
           | R7 R4 R1 |
           | D4 D5 D6 |
           | D7 D8 D9 |
           |__________|

OOP and algorithmic thinking at it's purest :)

two-dimensional cube array we work with (for a reference):

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
from Facelets import *


"""Compose fuctnions for xp and x2 permutations"""
def make_double_permutation(turn, cube_array):
   return turn(turn(cube_array))                      #first-class citizen - functional programming here

def make_prime_permutation(turn, cube_array):         #overall this file is very functional because it is full of pure functions
   return turn(turn(turn(cube_array)))





"""Turn fucnctions for front side"""
def f(cube_array: list[list[str]]) -> list[list[str]]:
    """Permutations on the front side"""
    formerF1 = cube_array[2][0]
    formerF2 = cube_array[2][1]
    formerF3 = cube_array[2][2]
    formerF4 = cube_array[2][3]
    formerF5 = cube_array[2][4]
    formerF6 = cube_array[2][5]
    formerF7 = cube_array[2][6]
    formerF8 = cube_array[2][7]
    formerF9 = cube_array[2][8]
    
    cube_array[2][0] = formerF7
    cube_array[2][1] = formerF4
    cube_array[2][2] = formerF1
    cube_array[2][3] = formerF8
    cube_array[2][4] = formerF5
    cube_array[2][5] = formerF2
    cube_array[2][6] = formerF9
    cube_array[2][7] = formerF6
    cube_array[2][8] = formerF3

    """Permutations on the up, right, down and left sides"""
    formerU7 = cube_array[0][6]
    formerU8 = cube_array[0][7]
    formerU9 = cube_array[0][8]
    
    formerR1 = cube_array[3][0]
    formerR4 = cube_array[3][3]
    formerR7 = cube_array[3][6]
    
    formerD1 = cube_array[5][0]
    formerD2 = cube_array[5][1]
    formerD3 = cube_array[5][2]

    formerL3 = cube_array[1][2]
    formerL6 = cube_array[1][5]
    formerL9 = cube_array[1][8]

    cube_array[0][6] = formerL9
    cube_array[0][7] = formerL6
    cube_array[0][8] = formerL3

    cube_array[3][0] = formerU7
    cube_array[3][3] = formerU8
    cube_array[3][6] = formerU9

    cube_array[5][0] = formerR7
    cube_array[5][1] = formerR4
    cube_array[5][2] = formerR1

    cube_array[1][2] = formerD1
    cube_array[1][5] = formerD2
    cube_array[1][8] = formerD3

    return cube_array


def f2(cube_array: list[list[str]]) -> list[list[str]]:
   return make_double_permutation(f, cube_array)


def fp(cube_array: list[list[str]]) -> list[list[str]]:
   return make_prime_permutation(f, cube_array)





"""
Cube reference (perspective) from the left side for making L turn:
            __________
           | U3 U6 U9 |
           | U2 U5 U8 | ← here you rewrite the columns from the regular U matrix as rows
           | U1 U4 U7 |
 __________|__________|__________ __________
| B1 B2 B3 | L1 L2 L3 | F1 F2 F3 | R1 R2 R3 |
| B4 B5 B6 | L4 L5 L6 | F4 F5 F6 | R4 R5 R6 |
| B7 B8 B9 | L7 L8 L9 | F7 F8 F9 | R7 R8 R9 |
|__________|__________|__________|__________|
           | D7 D4 D1 |
           | D8 D5 D2 | ← here you rewrite the columns from the regular D matrix as inversed rows
           | D9 D6 D3 |
           |__________|
"""

"""Turn fucnctions for left side"""
def l(cube_array: list[list[str]]) -> list[list[str]]:
    """Permutations on the left side"""
    formerL1 = cube_array[1][0]
    formerL2 = cube_array[1][1]
    formerL3 = cube_array[1][2]
    formerL4 = cube_array[1][3]
    formerL5 = cube_array[1][4]
    formerL6 = cube_array[1][5]
    formerL7 = cube_array[1][6]
    formerL8 = cube_array[1][7]
    formerL9 = cube_array[1][8]
    
    cube_array[1][0] = formerL7
    cube_array[1][1] = formerL4
    cube_array[1][2] = formerL1
    cube_array[1][3] = formerL8
    cube_array[1][4] = formerL5
    cube_array[1][5] = formerL2
    cube_array[1][6] = formerL9
    cube_array[1][7] = formerL6
    cube_array[1][8] = formerL3

    """Permutations on the up, front, down and back sides"""
    formerU1 = cube_array[0][0]
    formerU4 = cube_array[0][3]
    formerU7 = cube_array[0][6]
    
    formerF1 = cube_array[2][0]
    formerF4 = cube_array[2][3]
    formerF7 = cube_array[2][6]
    
    formerD7 = cube_array[5][6]
    formerD4 = cube_array[5][3]
    formerD1 = cube_array[5][0]

    formerB3 = cube_array[4][2]
    formerB6 = cube_array[4][5]
    formerB9 = cube_array[4][8]

    cube_array[0][0] = formerB9
    cube_array[0][3] = formerB6
    cube_array[0][6] = formerB3

    cube_array[2][0] = formerU1
    cube_array[2][3] = formerU4
    cube_array[2][6] = formerU7

    cube_array[5][6] = formerF7
    cube_array[5][3] = formerF4
    cube_array[5][0] = formerF1

    cube_array[4][2] = formerD7
    cube_array[4][5] = formerD4
    cube_array[4][8] = formerD1

    return cube_array


def l2(cube_array: list[list[str]]) -> list[list[str]]:
   return make_double_permutation(l, cube_array)


def lp(cube_array: list[list[str]]) -> list[list[str]]:
   return make_prime_permutation(l, cube_array)





"""
Cube reference (perspective) from the right side for making R turn:
            __________
           | U7 U4 U1 |
           | U8 U5 U2 | ← here you rewrite the columns from the regular U matrix as inversed rows
           | U9 U6 U3 |
 __________|__________|__________ __________
| F1 F2 F3 | R1 R3 R3 | B1 B2 B3 | L1 L2 L3 |
| F4 F5 F6 | R4 R5 R6 | B4 B5 B6 | L4 L5 L6 |
| F7 F8 F9 | R7 R8 R9 | B7 B8 B9 | L7 L8 L9 |
|__________|__________|__________|__________|
           | D3 D6 D9 |
           | D2 D4 D8 | ← here you rewrite the columns from the regular D matrix as inversed rows
           | D1 D4 D7 |
           |__________|
"""

"""Turn fucnctions for right side"""
def r(cube_array: list[list[str]]) -> list[list[str]]:
    """Permutations on the right side"""
    formerR1 = cube_array[3][0]
    formerR2 = cube_array[3][1]
    formerR3 = cube_array[3][2]
    formerR4 = cube_array[3][3]
    formerR5 = cube_array[3][4]
    formerR6 = cube_array[3][5]
    formerR7 = cube_array[3][6]
    formerR8 = cube_array[3][7]
    formerR9 = cube_array[3][8]
    
    cube_array[3][0] = formerR7
    cube_array[3][1] = formerR4
    cube_array[3][2] = formerR1
    cube_array[3][3] = formerR8
    cube_array[3][4] = formerR5
    cube_array[3][5] = formerR2
    cube_array[3][6] = formerR9
    cube_array[3][7] = formerR6
    cube_array[3][8] = formerR3

    """Permutations on the up, front, down and back sides"""
    formerU9 = cube_array[0][8]
    formerU6 = cube_array[0][5]
    formerU3 = cube_array[0][2]
    
    formerB1 = cube_array[4][0]
    formerB4 = cube_array[4][3]
    formerB7 = cube_array[4][6]
    
    formerD3 = cube_array[5][2]
    formerD6 = cube_array[5][5]
    formerD9 = cube_array[5][8]

    formerF3 = cube_array[2][2]
    formerF6 = cube_array[2][5]
    formerF9 = cube_array[2][8]

    cube_array[0][8] = formerF9
    cube_array[0][5] = formerF6
    cube_array[0][2] = formerF3

    cube_array[4][0] = formerU9
    cube_array[4][3] = formerU6
    cube_array[4][6] = formerU3

    cube_array[5][2] = formerB7
    cube_array[5][5] = formerB4
    cube_array[5][8] = formerB1

    cube_array[2][2] = formerD3
    cube_array[2][5] = formerD6
    cube_array[2][8] = formerD9

    return cube_array


def r2(cube_array: list[list[str]]) -> list[list[str]]:
   return make_double_permutation(r, cube_array)


def rp(cube_array: list[list[str]]) -> list[list[str]]:
   return make_prime_permutation(r, cube_array)





"""
Cube reference (perspective) from the back side for making B turn:
            __________
           | U9 U8 U7 |
           | U6 U5 U4 | ← here you rewrite the columns from the regular U matrix as inversed rows in reversed order
           | U3 U2 U1 |
 __________|__________|__________ __________
| R1 R2 R3 | B1 B2 B3 | L1 L2 L3 | F1 F2 F3 |
| R4 R5 R6 | B4 B5 B6 | L4 L5 L6 | F4 F5 F6 |
| R7 R8 R9 | B7 B8 R9 | L7 L8 L9 | F7 F8 F9 |
|__________|__________|__________|__________|
           | D9 D8 D7 |
           | D6 D5 D4 | ← here you rewrite the columns from the regular D matrix as inversed rows in reversed order
           | D3 D2 D1 |
           |__________|
"""

"""Turn fucnctions for back side"""
def b(cube_array: list[list[str]]) -> list[list[str]]:
    """Permutations on the back side"""
    formerB1 = cube_array[4][0]
    formerB2 = cube_array[4][1]
    formerB3 = cube_array[4][2]
    formerB4 = cube_array[4][3]
    formerB5 = cube_array[4][4]
    formerB6 = cube_array[4][5]
    formerB7 = cube_array[4][6]
    formerB8 = cube_array[4][7]
    formerB9 = cube_array[4][8]
    
    cube_array[4][0] = formerB7
    cube_array[4][1] = formerB4
    cube_array[4][2] = formerB1
    cube_array[4][3] = formerB8
    cube_array[4][4] = formerB5
    cube_array[4][5] = formerB2
    cube_array[4][6] = formerB9
    cube_array[4][7] = formerB6
    cube_array[4][8] = formerB3

    """Permutations on the up, front, left and down sides"""
    formerU3 = cube_array[0][2]
    formerU2 = cube_array[0][1]
    formerU1 = cube_array[0][0]
    
    formerL1 = cube_array[1][0]
    formerL4 = cube_array[1][3]
    formerL7 = cube_array[1][6]
    
    formerD9 = cube_array[5][8]
    formerD8 = cube_array[5][7]
    formerD7 = cube_array[5][6]

    formerR3 = cube_array[3][2]
    formerR6 = cube_array[3][5]
    formerR9 = cube_array[3][8]

    cube_array[0][2] = formerR9
    cube_array[0][1] = formerR6
    cube_array[0][0] = formerR3

    cube_array[1][0] = formerU3
    cube_array[1][3] = formerU2
    cube_array[1][6] = formerU1

    cube_array[5][8] = formerL7
    cube_array[5][7] = formerL4
    cube_array[5][6] = formerL1

    cube_array[3][2] = formerD9
    cube_array[3][5] = formerD8
    cube_array[3][8] = formerD7

    return cube_array


def b2(cube_array: list[list[str]]) -> list[list[str]]:
   return make_double_permutation(b, cube_array)


def bp(cube_array: list[list[str]]) -> list[list[str]]:
   return make_prime_permutation(b, cube_array)





"""
Cube reference (perspective) from the upper side for making U turn:
            __________
           | B9 B8 B7 |
           | B6 B5 B4 |
           | B3 B2 B1 |
 __________|__________|__________ __________
| L7 L4 L1 | U1 U2 U3 | R3 R6 R9 | D9 D8 D7 |
| L8 L5 L2 | U4 U5 U6 | R2 R5 R8 | D6 D5 D4 |  ← here instead of going aroung vertical axis,
| L9 L6 L3 | U7 U8 U9 | R1 R4 R7 | D3 D2 D1 |  ← we go around horizontal axis, the one looking "away from" or "to" us
|__________|__________|__________|__________|
           | F1 F2 F3 |
           | F4 F5 F6 |
           | F7 F8 F9 |
           |__________|
"""

"""Turn fucnctions for upper side"""
def u(cube_array: list) -> list:
    """Permutations on the upper side"""
    formerU1 = cube_array[0][0]
    formerU2 = cube_array[0][1]
    formerU3 = cube_array[0][2]
    formerU4 = cube_array[0][3]
    formerU5 = cube_array[0][4]
    formerU6 = cube_array[0][5]
    formerU7 = cube_array[0][6]
    formerU8 = cube_array[0][7]
    formerU9 = cube_array[0][8]
    
    cube_array[0][0] = formerU7
    cube_array[0][1] = formerU4
    cube_array[0][2] = formerU1
    cube_array[0][3] = formerU8
    cube_array[0][4] = formerU5
    cube_array[0][5] = formerU2
    cube_array[0][6] = formerU9
    cube_array[0][7] = formerU6
    cube_array[0][8] = formerU3

    """Permutations on the back, right, front and left sides"""
    formerB3 = cube_array[4][2]
    formerB2 = cube_array[4][1]
    formerB1 = cube_array[4][0]
    
    formerR3 = cube_array[3][2]
    formerR2 = cube_array[3][1]
    formerR1 = cube_array[3][0]
    
    formerF3 = cube_array[2][2]
    formerF2 = cube_array[2][1]
    formerF1 = cube_array[2][0]

    formerL3 = cube_array[1][2]
    formerL2 = cube_array[1][1]
    formerL1 = cube_array[1][0]

    cube_array[4][2] = formerL3
    cube_array[4][1] = formerL2
    cube_array[4][0] = formerL1

    cube_array[3][2] = formerB3
    cube_array[3][1] = formerB2
    cube_array[3][0] = formerB1

    cube_array[2][2] = formerR3
    cube_array[2][1] = formerR2
    cube_array[2][0] = formerR1

    cube_array[1][2] = formerF3
    cube_array[1][1] = formerF2
    cube_array[1][0] = formerF1

    return cube_array


def u2(cube_array: list[list[str]]) -> list[list[str]]:
   return make_double_permutation(u, cube_array)


def up(cube_array: list[list[str]]) -> list[list[str]]:
   return make_prime_permutation(u, cube_array)





"""
Cube reference (perspective) from the down side for making D turn:
            __________
           | F1 F2 F3 |
           | F4 F5 F6 |
           | F7 F8 F9 |
 __________|__________|__________ __________
| L3 L6 L9 | D1 D2 D3 | R7 R4 R1 | U9 U8 U7 |
| L2 L5 L8 | D4 D5 D6 | R8 R5 R2 | U6 U5 U4 |  ← here instead of going aroung vertical axis,
| L1 L4 L7 | D7 D8 D9 | R9 R6 R3 | U3 U2 U1 |  ← we go around horizontal axis, the one looking "away from" or "to" us
|__________|__________|__________|__________|
           | B9 B8 B7 |
           | B6 B5 B4 |
           | B3 B2 B1 |
           |__________|
"""

"""Turn fucnctions for down side"""
def d(cube_array: list[list[str]]) -> list[list[str]]:
    """Permutations on the down side"""
    formerD1 = cube_array[5][0]
    formerD2 = cube_array[5][1]
    formerD3 = cube_array[5][2]
    formerD4 = cube_array[5][3]
    formerD5 = cube_array[5][4]
    formerD6 = cube_array[5][5]
    formerD7 = cube_array[5][6]
    formerD8 = cube_array[5][7]
    formerD9 = cube_array[5][8]
    
    cube_array[5][0] = formerD7
    cube_array[5][1] = formerD4
    cube_array[5][2] = formerD1
    cube_array[5][3] = formerD8
    cube_array[5][4] = formerD5
    cube_array[5][5] = formerD2
    cube_array[5][6] = formerD9
    cube_array[5][7] = formerD6
    cube_array[5][8] = formerD3

    """Permutations on the front, right, back and left sides"""
    formerF7 = cube_array[2][6]
    formerF8 = cube_array[2][7]
    formerF9 = cube_array[2][8]
    
    formerR7 = cube_array[3][6]
    formerR8 = cube_array[3][7]
    formerR9 = cube_array[3][8]
    
    formerB7 = cube_array[4][6]
    formerB8 = cube_array[4][7]
    formerB9 = cube_array[4][8]

    formerL7 = cube_array[1][6]
    formerL8 = cube_array[1][7]
    formerL9 = cube_array[1][8]

    cube_array[2][6] = formerL7
    cube_array[2][7] = formerL8
    cube_array[2][8] = formerL9

    cube_array[3][6] = formerF7
    cube_array[3][7] = formerF8
    cube_array[3][8] = formerF9

    cube_array[4][6] = formerR7
    cube_array[4][7] = formerR8
    cube_array[4][8] = formerR9

    cube_array[1][6] = formerB7
    cube_array[1][7] = formerB8
    cube_array[1][8] = formerB9

    return cube_array


def d2(cube_array: list[list[str]]) -> list[list[str]]:
   return make_double_permutation(d, cube_array)


def dp(cube_array: list[list[str]]) -> list[list[str]]:
   return make_prime_permutation(d, cube_array)


if __name__ == "__main__":
  cube = create_facelets(3)
  print(cube)
  d(cube)
  print(create_2D(cube))