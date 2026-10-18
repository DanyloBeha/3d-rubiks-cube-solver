class SmallCube:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def position(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return f"Plate({self.x}, {self.y}, {self.z})"