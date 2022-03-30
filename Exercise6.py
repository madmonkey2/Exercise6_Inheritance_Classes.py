class Vector:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __add__(self, other):
        a = []
        for coordinate1, coordinate2 in zip(self.coordinates, other.coordinates):
            if len(self.coordinates) != len(other.coordinates):
                raise VectorDimensionError
            else:
                a.append(coordinate1 + coordinate2)
        return f"x + y - > {self.__class__(*a)}"

    def __sub__(self, other):
        a = []
        for coordinate1, coordinate2 in zip(self.coordinates, other.coordinates):
            if len(self.coordinates) != len(other.coordinates):
                raise VectorDimensionError
            else:
                a.append(coordinate1 - coordinate2)
        return f"x - y - > {self.__class__(*a)}"

    def __len__(self):
        return f"len(x) -> {len(self.coordinates)}"

    def __abs__(self):
        a = 0
        for coordinate in self.coordinates:
            a += coordinate ** 2
        return int(abs((a ** (1 / 2))))

    def __getitem__(self, i):
        if i > len(self.coordinates):
            raise IndexError
        else:
            return self.coordinates[i]

    def __dot__(self, other):
        sum1 = 0
        for coordinate1, coordinate2 in zip(self.coordinates, other.coordinates):
            if len(self.coordinates) != len(other.coordinates):
                raise VectorDimensionError
            else:
                sum1 += coordinate1 * coordinate2
        return f"x.dot(y) -> {sum1}"

    def scale(self, other):
        a = []
        for coordinate in self.coordinates:
            a.append(coordinate * other)
        return f"x.scale({other}) -> {self.__class__(*a)}"

    def direction(self):
        a = []
        for coordinate in self.coordinates:
            a.append(coordinate / int(self.__abs__()))
        return f"x.direction() -> {self.__class__(*a)}"

    def __repr__(self):
        return self.__class__.__name__ + str(self.coordinates)


class VectorError(Exception, Vector):
    def __init__(self, *coordinates):
        super().__init__(*coordinates)

    def __str__(self):
        return f"VectorError"


class VectorDimensionError(Exception, Vector):
    def __init__(self, *coordinates):
        super().__init__(*coordinates)

    def __str__(self):
        return f"Vector length are not equal"


x = Vector(0, 3, 4, 0)
y = Vector(0, -3, 1, -4)
z = Vector(0, 0)
# other = int(input("Enter a number to scale x with: "))
# print(x.__add__(y))
# print(x.__sub__(y))
# print(x.__getitem__(i=2))
# print(x.__len__())
# print(x.__abs__())
# print(x.__dot__(z))
# print(x.scale(other))
# print(x.direction())
