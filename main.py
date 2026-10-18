"""
Either this or rubik.bash file will glue everyting together.

Maybe this will become the GUI file which will also kinda glue everything - NO, since GUI layer should be in separate module

"""
from Facelets import *
from scramble import *
from gui import *
from fridrich import *
from kociemba import *


"""MAIN FUNCTION"""



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