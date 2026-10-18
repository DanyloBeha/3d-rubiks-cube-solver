from abc import ABC, abstractmethod

class Renderable(ABC):
    @abstractmethod
    def render(self):
        pass


class Plate(Renderable):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def render(self):
        return "H"

class Cube(Renderable):
    def __init__(self, size=3):
        self.size = size
        self.plates = self.generate_plates()

    def generate_plates(self):
        plates = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    plates.append(Plate(x, y, z))
        return plates

    def render(self):
        face = ""
        for y in range(-1, 2):
            for x in range(-1, 2):
                face += "Plate "
            face += "\n"
        return face



cube = Cube()
print(cube.render())