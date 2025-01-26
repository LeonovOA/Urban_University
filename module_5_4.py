class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        name = args[0]
        cls.houses_history.append(name)
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __eq__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        return self.floors == other.floors

    def __ne__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        return self.floors != other.floors

    def __lt__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        return self.floors < other.floors

    def __le__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        return self.floors <= other.floors

    def __gt__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        return self.floors > other.floors

    def __ge__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        return self.floors >= other.floors

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

#Примеры из задания
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

del h1