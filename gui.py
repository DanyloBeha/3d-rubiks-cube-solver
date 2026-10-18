"""
So far all the other files refereed to the the logic layer
This is a separate GUI layer

This file will:
1. Make a 3D visualization
2. Add interface
3. Update the cube and animate it

Goals:
1. Make interface to choose between machine and human solving
2. Make options to choose between Fridrich and Kociemba methods
3. Output the scramble and the solving algorithms for the machine solving
4. Be able to color your cube to be solved???
5. Generate scramble algorithm, record solving time and save it into statistics
6. Be able to export statistics

How to make 3D vizualization:
1. Create a compound object consisting of cube and plates on it (1 for central piece, 2 for edge piece and 3 for corner piece)
    1. Create a cubie base - just a white cube
    2. Create colorful plates to it
    3. Append them to a list of a piece
    4. Make this list a compound object -> we got a cubie
2. Position a cubie and add to a list of cubies (list of 27 compound cubies)
3. Define rotations

How to make intefrace and buttons what work well:
We should create global variables state machine so that functions that we bind to the buttons can act on those global variables and states.
And we only show 1 cube at a time, so it will work perfectly with global variables for the cube (3D one and array one), e.g. when we want to create a 4 by 4 cube, we can overwrite the current one.

Maybe I am wrong and I should switch to OOP structure, basically we have a global variable (object) but in a better way?
"""
from vpython import *
from kociemba_applied import *
from Facelets import *
from scramble import *
from fridrich import *

"""Function for making a 3-dimensional cube"""
def create_3d_cube():
    full_cube = []

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                cubie = []
                cubie_base = box(size = vec(0.96, 0.96, 0.96), color = vec(0.9, 0.9, 0.9), opacity = 0.95)
                cubie.append(cubie_base)

                if x == 1:
                    plate = box(pos = vec(0.48, 0, 0), size = vec(0.02, 0.96, 0.96), color = color.red, shininess = 0.3)
                    cubie.append(plate)

                if x == -1:
                    plate = box(pos = vec(-0.48, 0, 0), size = vec(0.02, 0.96, 0.96), color = color.orange, shininess = 0.3)
                    cubie.append(plate)

                if y == 1:
                    plate = box(pos = vec(0, 0.48, 0), size = vec(0.96, 0.02, 0.96), color = color.yellow, shininess = 0.3)
                    cubie.append(plate)

                if y == -1:
                    plate = box(pos = vec(0, -0.48, 0), size = vec(0.96, 0.02, 0.96), color = color.white, shininess = 0.3)
                    cubie.append(plate)

                if z == 1:
                    plate = box(pos = vec(0, 0, 0.48), size = vec(0.96, 0.96, 0.02), color = color.blue, shininess = 0.3)
                    cubie.append(plate)

                if z == -1:
                    plate = box(pos = vec(0, 0, -0.48), size = vec(0.96, 0.96, 0.02), color = color.green, shininess = 0.3)
                    cubie.append(plate)

                compound_cubie = compound(cubie, pos = vec(x, y, z))
                full_cube.append(compound_cubie)
    return full_cube

"""Functions for animating turns"""
quantifier = 5

"""Right side"""
def r_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.x > 0.9:
                cubie.rotate(angle = (-pi/2) / quantifier, axis = vec(1, 0, 0), origin = vec(0, 0, 0))

def rp_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.x > 0.9:
                cubie.rotate(angle = (pi/2) / quantifier, axis = vec(1, 0, 0), origin = vec(0, 0, 0))

def r2_animate(cube):
    for _ in range(quantifier*2):
        rate(30)
        for cubie in cube:
            if cubie.pos.x > 0.9:
                cubie.rotate(angle = (-pi) / (quantifier*2), axis = vec(1, 0, 0), origin = vec(0, 0, 0))

"""Left side"""
def l_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.x < -0.9:
                cubie.rotate(angle = (-pi/2) / quantifier, axis = vec(-1, 0, 0), origin = vec(0, 0, 0))

def lp_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.x < -0.9:
                cubie.rotate(angle = (pi/2) / quantifier, axis = vec(-1, 0, 0), origin = vec(0, 0, 0))

def l2_animate(cube):
    for _ in range(quantifier*2):
        rate(30)
        for cubie in cube:
            if cubie.pos.x < -0.9:
                cubie.rotate(angle = (-pi) / (quantifier*2), axis = vec(-1, 0, 0), origin = vec(0, 0, 0))

"""Front side"""
def f_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.z > 0.9:
                cubie.rotate(angle = (-pi/2) / quantifier, axis = vec(0, 0, 1), origin = vec(0, 0, 0))

def fp_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.z > 0.9:
                cubie.rotate(angle = (pi/2) / quantifier, axis = vec(0, 0, 1), origin = vec(0, 0, 0))

def f2_animate(cube):
    for _ in range(quantifier*2):
        rate(30)
        for cubie in cube:
            if cubie.pos.z > 0.9:
                cubie.rotate(angle = (-pi) / (quantifier*2), axis = vec(0, 0, 1), origin = vec(0, 0, 0))

"""Back side"""
def b_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.z < -0.9:
                cubie.rotate(angle = (-pi/2) / quantifier, axis = vec(0, 0, -1), origin = vec(0, 0, 0))

def bp_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.z < -0.9:
                cubie.rotate(angle = (pi/2) / quantifier, axis = vec(0, 0, -1), origin = vec(0, 0, 0))

def b2_animate(cube):
    for _ in range(quantifier*2):
        rate(30)
        for cubie in cube:
            if cubie.pos.z < -0.9:
                cubie.rotate(angle = (-pi) / (quantifier*2), axis = vec(0, 0, -1), origin = vec(0, 0, 0))

"""Upper side"""
def u_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.y > 0.9:
                cubie.rotate(angle = (-pi/2) / quantifier, axis = vec(0, 1, 0), origin = vec(0, 0, 0))

def up_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.y > 0.9:
                cubie.rotate(angle = (pi/2) / quantifier, axis = vec(0, 1, 0), origin = vec(0, 0, 0))

def u2_animate(cube):
    for _ in range(quantifier*2):
        rate(30)
        for cubie in cube:
            if cubie.pos.y > 0.9:
                cubie.rotate(angle = (-pi) / (quantifier*2), axis = vec(0, 1, 0), origin = vec(0, 0, 0))

"""Down side"""
def d_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.y < -0.9:
                cubie.rotate(angle = (-pi/2) / quantifier, axis = vec(0, -1, 0), origin = vec(0, 0, 0))

def dp_animate(cube):
    for _ in range(quantifier):
        rate(30)
        for cubie in cube:
            if cubie.pos.y < -0.9:
                cubie.rotate(angle = (pi/2) / quantifier, axis = vec(0, -1, 0), origin = vec(0, 0, 0))

def d2_animate(cube):
    for _ in range(quantifier*2):
        rate(30)
        for cubie in cube:
            if cubie.pos.y < -0.9:
                cubie.rotate(angle = (-pi) / (quantifier*2), axis = vec(0, -1, 0), origin = vec(0, 0, 0))

"""Animating a sequence of turns"""
def animate_sequence(turns: list[Callable], cube: list):  # e.g. [rp, u, d2, f]
    for turn in turns:
        if turn.__name__ == "r":
            r_animate(cube)
        elif turn.__name__ == "rp":
            rp_animate(cube)
        elif turn.__name__ == "r2":
            r2_animate(cube)
        elif turn.__name__ == "l":
            l_animate(cube)
        elif turn.__name__ == "lp":
            lp_animate(cube)
        elif turn.__name__ == "l2":
            l2_animate(cube)
        elif turn.__name__ == "f":
            f_animate(cube)
        elif turn.__name__ == "fp":
            fp_animate(cube)
        elif turn.__name__ == "f2":
            f2_animate(cube)
        elif turn.__name__ == "b":
            b_animate(cube)
        elif turn.__name__ == "bp":
            bp_animate(cube)
        elif turn.__name__ == "b2":
            b2_animate(cube)
        elif turn.__name__ == "u":
            u_animate(cube)
        elif turn.__name__ == "up":
            up_animate(cube)
        elif turn.__name__ == "u2":
            u2_animate(cube)
        elif turn.__name__ == "d":
            d_animate(cube)
        elif turn.__name__ == "dp":
            dp_animate(cube)
        elif turn.__name__ == "d2":
            d2_animate(cube)


"""-----GUI------"""
"""Global state machine and event handlers"""
"""
#making a 3D model and a status comment
comment = label(text = "Status: rendering", pos = vec(0, 2, 0))
cube_3d = create_3d_cube()
comment.text = "Status: rendered, waiting for input"

#making a cube_array which will be permutated and represented by 3D model
cube_array = create_facelets(3)

#event handler for scrambling on button click
def scramble_on_click():
    scramble = generate_scramble()
    apply_scramble(scramble, cube_array)
    comment.text = "Status: scrambling"
    animate_sequence(scramble, cube_3d)
    comment.text = "Status: scrambled, waiting for input"


def control():
    button(bind = scramble_on_click, text = "Scramble")

def update():
    rate(30)
    

def start():
    control()
    while True:
        update()
    
start()
"""
if __name__ == "__main__":
    comment = label(text = "Status: rendering", pos = vec(0, 2, 0))
    test_cube_3d = create_3d_cube()


    cube_array = create_facelets(3)
    scramble = generate_scramble()
    print(f"Scramble: {get_scramble(scramble)}")
    apply_scramble(scramble, cube_array)
    scene.caption = f"\nScramble algorithm: {get_scramble(scramble)}"
    comment.text = "Scramble?"
    scene.waitfor('click keydown')
    comment.text = "Status: scrambling"
    animate_sequence(scramble, test_cube_3d)

    solve_functions1 = pack_kociemba_solve_string_into_func_list(solve_with_kociemba(cube_array))
    solve_functions2 = solve_with_fridrich(cube_array)

    comment.text = "Solve with kociemba?"
    scene.waitfor('click keydown')
    comment.text = "Status: solving with kociemba"
    animate_sequence(solve_functions1, test_cube_3d)

    comment.text = "Scramble again?"
    scene.waitfor('click keydown')
    comment.text = "Status: scrambling"
    animate_sequence(scramble, test_cube_3d)

    comment.text = "Solve with fridrich?"
    scene.waitfor('click keydown')
    comment.text = "Status: solving with fridrich"
    animate_sequence(solve_functions2, test_cube_3d)
    comment.text = "Status: demo is over!"

    while True:
        rate(30)



