"""
What representation and structure we are trying to achieve:
Note: that is a two-dimensional 6*9 array (6 faces with 9 facelets on each)
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
Todo: Make all the functions inside a class
"""
import Cube as C



"""Creating a class in which objects will act as separate facelets"""
class Facelets(C.Cube):
    def __init__(self, face: str, index: int, dimension = 0):
        super().__init__(dimension)
        self.face = face
        self.index = str(index)
        self.position = self.face + self.index



"""Creating a function that will create our cube for different dimensions"""

def create_facelets(dimension: int) -> list[list[str]]:
    facelets = []
    cube = C.Cube(dimension)
    faces = ["U", "L", "F", "R", "B", "D"]
    for f in faces:
        facelets_sublist = []
        for i in range(1, cube.dimension ** 2 + 1):  #we use cube.dimension here to be able to create any x*x cube
            facelet = Facelets(f, i)
            facelets_sublist.append(facelet.position)
        facelets += [facelets_sublist]
    return facelets



"""Pack our cube into one string"""
def pack_into_string(list: list[list[str]]) -> str:
    num_of_elements = len(list[0])  #we use num_of_elements to be able to pack_into_string a cube of any dimension
    s = ""
    for i in range(0, 5):
        for j in range(0, num_of_elements):
                s += f"{list[i][j]}-"
    for i in range(0, (num_of_elements - 1)):
        s += f"{list[5][i]}-"
    s += f"{list[5][-1]}"
    return s



"""Unpack our cube from a string"""
def unpack_from_string(s: str) -> list[list[str]]:
    list_final: list[list] = [[], [], [], [], [], []]
    list_of_elements = s.split("-") #also works for any dimension

    """I have not managed to do this in a for cycle"""
    list_final[0] = list(filter(lambda x: "U" in x , list_of_elements))   #filter - functional programming here. no map and reduce for now, unfortunately
    list_final[1] = list(filter(lambda x: "L" in x , list_of_elements))
    list_final[2] = list(filter(lambda x: "F" in x , list_of_elements))
    list_final[3] = list(filter(lambda x: "R" in x , list_of_elements))
    list_final[4] = list(filter(lambda x: "B" in x , list_of_elements))
    list_final[5] = list(filter(lambda x: "D" in x , list_of_elements))

    return list_final



"""Pack our cube into 2D string"""
def create_2D(list: list[list[str]]) -> str:
    s = "\t  " + "_"*8 + f"\n\t |{list[0][0]} {list[0][1]} {list[0][2]}|"
    s += f"\n\t |{list[0][3]} {list[0][4]} {list[0][5]}|"
    s += f"\n\t |{list[0][6]} {list[0][7]} {list[0][8]}|"
    s += "\n " + "_"*8 + "|" + "_"*8 + "|" + "_"*8 + " " + "_"*8
    s += f"\n|{list[1][0]} {list[1][1]} {list[1][2]}|{list[2][0]} {list[2][1]} {list[2][2]}|{list[3][0]} {list[3][1]} {list[3][2]}|{list[4][0]} {list[4][1]} {list[4][2]}|"
    s += f"\n|{list[1][3]} {list[1][4]} {list[1][5]}|{list[2][3]} {list[2][4]} {list[2][5]}|{list[3][3]} {list[3][4]} {list[3][5]}|{list[4][3]} {list[4][4]} {list[4][5]}|"
    s += f"\n|{list[1][6]} {list[1][7]} {list[1][8]}|{list[2][6]} {list[2][7]} {list[2][8]}|{list[3][6]} {list[3][7]} {list[3][8]}|{list[4][6]} {list[4][7]} {list[4][8]}|"
    s += "\n" + "|" + "_"*8 + "|" + "_"*8 + "|" + "_"*8 + "|" + "_"*8 + "|"
    s += "\t   " + f"\n\t |{list[5][0]} {list[5][1]} {list[5][2]}|"
    s += f"\n\t |{list[5][3]} {list[5][4]} {list[5][5]}|"
    s += f"\n\t |{list[5][6]} {list[5][7]} {list[5][8]}|"
    s += "\n\t |" + "_"*8 + "|"
    
    return s



if __name__ == "__main__":
    """Creating a cube and visualization"""
    cube = create_facelets(3)
    print(cube)
    print(create_2D(cube))

    """Packing into a string"""
    cube_in_string = pack_into_string(cube)
    print(cube_in_string)

    """Unpacking from a string"""
    print(unpack_from_string(cube_in_string))