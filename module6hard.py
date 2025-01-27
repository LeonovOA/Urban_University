import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        valid_sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.__sides = valid_sides[:self.sides_count] if len(valid_sides) == self.sides_count else [1] * self.sides_count
        self.filled = True

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(s, int) and s > 0 for s in sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def get_square(self):
        return (self.get_sides()[0] ** 2) / (4 * math.pi)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        processed_sides = [sides[0]] * self.sides_count if len(sides) == 1 else [1] * self.sides_count
        super().__init__(color, *processed_sides)

    def set_sides(self, *sides):
        processed_sides = list(sides) * self.sides_count if len(sides) == 1 else list(sides)
        super().set_sides(*processed_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Пример из задания
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)
print(cube1.get_color())  # [222, 35, 130]

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())  # [6, 6, ..., 6] (12 раз)

circle1.set_sides(15)
print(circle1.get_sides())  # [15]

print(len(circle1))  # 15
print(cube1.get_volume())  # 216