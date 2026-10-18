# Rubik's Cube solver: What is this project about?
> [!Note]
> About difficulty: *"I can both solve the cube and have thought about an implementation. If I were teaching programming, I'd never assign this to either a first or second semester programming course. Why? First, it's hard to get all the algorithms right. Second, it's hard to get the data representation right."* - [reddit soure](https://www.reddit.com/r/learnprogramming/comments/rwu8tt/comment/hreq8to/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
## Problems
The problems that formed the basis of the project concept and whose solution is the goal:
- **Philosophical component:**
    1. The decline of the culture of assembling Rubik's Cubes.
    2. Create an environment for learning and practising Rubik's Cube assembly.

- **Practical component:**
    1. Environment component:
        1. Create a 3D visualisation of the Rubik's Cube.
        2. Create a UI/UX that is comfortable for visual perception and learning.
        3. Adapt algorithms and logic for Rubik's Cubes of other dimensions.
    2. Automatic solving component:
        1. Create an algorithm for disassembling the Rubik's Cube.
        2. Create an algorithm for assembling the Rubik's Cube using the fastest possible combination.
    3. Manual solving component:
        1. Create an algorithm for disassembling a Rubik's Cube according to speedcubing rules.
        2. Create timer logic for Rubik's Cube assemblies.
        3. Create statistics for Rubik's Cube assemblies with memory and leaderboard.

## Paradigms covered in the course and used to implement the project:
1. **Object-oriented programming** to represent the Rubik's Cube and its elements.
2. **Functional programming** for turning faces, generating a disassembly algorithm, creating a "human assembly" algorithm, checking the correctness of the Rubik's Cube state, and optimising algorithms.
3. **Script programming** for keeping statistics.

# Design
## Stage 1: OOP - structure and cube

### 0. What we have to create
- cube
### 1. How to show the cube
First step is to represent the cube, second is to solve.  
For the first step we can use 3D engine, 2D colors representation or text-based representation.  
We will start with text representation and move to 2D, then 3D.  
Also we have to think about N-sized cubes and how to represent them

### 2. How to represent the cube in code
We have to decide how to represent the cube:
- we can treat it as a collection of pieces (the corner and edge cubies level)
- (our way) we can treat it as a collection of colors/location (the facelet level)
    - three-dimensional 6 * 3 * 3 arrays
    - (our way) two-dimensional 6 * 9 arrays - because this is most higher-level data structure so that it is possible for us to make our own algorithm
    - single one-dimensional 54 array
- we can treat it as natural numbers (coordinate level)
- matrix
- binary - interesting, similar to 6 * 9 array
- and much more, there are whole scientific papers on this topic  
The representation is implemeted by using a Cube parent class to define the dimensions and Facelets subclass to create a data structure that will represent the cube
```
That is a two-dimensional 6*9 array (6 faces with 9 facelets on each):
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

Note: U - Up, L - Left, F - Front, R - Right, B - Back, D - Down
Note: during permutation all pieces will move to other pieces former places, e.g. 90° clockwise means F1 -> F3. So we do not mean "is replaced by" but we mean "is carried to"
Note: during permutation all center pieces (U5, L5, ..., D5) will always stay the same.
Note: in the GUI part we can assign each of the faces a color
```

### 3. Hot to represent the colors in the cube
We have to decide how to store colors:
- we can treat each facelet as a color, i.e. facelet will store a color
- (our choice) we can treat each facelet as an element from a certain side (e.g. F1, F2, ..., F9, R1, ..., R9, Ln, Bn, Dn, Un), i.e. facelet will store a location. We use this method because it is a more general approach and it does not limit us to colors but we always can assign colors, e.g. blue to F, yellow to U etc.

## Stage 2: Functional - turns, scrambling and solving
### 0. How to turn the cube
```
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
Permutations are an example of functional programming since they are pure and deterministic funcitons 
```
### 1. How to solve the cube
There are numerous ways and algorithms to solve the cube, all of them differ in speed, complexity etc.
- (our initial choice) we can translate intuitive and human methods to algorithms. Intuitive but slow (will take 60-200 moves)
- (our choice) we can use just pure computing
- we can train neural networks
- we can use algorithms, concepts of which already exist:
    - Thistlethwaite’s algorithm - 52 moves
    - Korf's algorithm (God's algorithm) - fewer than 20 moves
    - (our choice) Kociemba/2-Phase Algorithm
    - Reid's algorithm - 29 moves

Each of the algorithms is pure funciton and kociembe_applied uses functional list operations

### 2. How to scramble the cube
It is easy, we just apply 20-30 random moves. All the moves act as a permutation on our facelets. Scrambling and assembling turns into sequence is made using funciton closures

## Stage 3: Scripting
We can use scripting for gluing everything into one application that can be launched be a double-clicking from the desktop.  
Also we can use it to write log files about scrambles, cube states, solution (for machine solving) and about solve times and statistics (for human solving)

## Stage 4: GUI
Our goal is to represent the cube as a 3D model using VPython.  
The interface can be done in two ways:
- we can make the interface inside VPython (the most convinient way)
- we can make the interface in TKinter and launch VPython from it.

> [!Note]
> More about implementation can be read in each of the .py files, there are a lot of comments there

# What was learned
The most valuable skill is to understand and to be able to use all paradigms together in one program to solve a specific problem. Integration and integrity of all the files is key.  
It was challenging to write a solving algorithm and to figure out how all files (data structure, solving algorithm, scramble and GUI) should communicate to each other.  
Lessons learned:
- to avoid global variables
- to use global state machine for GUI (event handlers that use global variables)
- to make functions atomic
- project time managment

# Conculusion
My program can create, scramble and solve the Rubik's cube all by itself and then demostrate it in 3D environment. That is a great achievement, I guess. But I have not brought to live all my plans.  
So the project will be imporved over the course of the holidays, e.g. implementation of OpenCV for visual color recognition