> [!Note]
> About difficulty: *"I can both solve the cube and have thought about an implementation. If I were teaching programming, I'd never assign this to either a first or second semester programming course. Why? First, it's hard to get all the algorithms right. Second, it's hard to get the data representation right."* - [reddit soure](https://www.reddit.com/r/learnprogramming/comments/rwu8tt/comment/hreq8to/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

#### Nevertheless!
## Stage 1 : repo

## Stage 2: OOP

### 0. What we have to create
- moves (turns)
- facelets
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
    - (our way) two-dimensional 6 * 9 arrays
    - single one-dimensional 54 array
- we can treat it as natural numbers (coordinate level)
- matrix
- binary - interesting, similar to 6 * 9 array
- and much more, there are whole scientific papers on this topic

### 3. Hot to represent the colors in the cube
We have to decide how to store colors:
- we can treat each facelet as a color, i.e. facelet will store a color
- (our choice) we can treat each facelet as an element from a certain side (e.g. F1, F2, ..., F9, R1, ..., R9, Ln, Bn, Dn, Un), i.e. facelet will store a location. We use this method because it is a more general approach and it does not limit us to colors but we always can assign colors, e.g. blue to F, yellow to U etc.

## Stage 3: Solving
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

### 2. How to scramble the cube
It is easy, we just apply 20-30 random moves. All the moves act as a permutation on our facelets.

## Stage 4: Scripting (WIP)
We can use scripting for gluing everything into one application that can be launched be a double-clicking from the desktop.  
Also we can use it to write log files about scrambles, cube states, solution (for machine solving) and about solve times and statistics (for human solving)

## Stage 5: GUI (WIP)
Our goal is to represent the cube as a 3D model using VPython.  
The interface can be done in two ways:
- we can make the interface inside VPython (the most convinient way)
- we can make the interface in TKinter and launch VPython from it.