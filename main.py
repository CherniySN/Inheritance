class Polygon:

    def __int__(self, sides, uglu):
        self._sides = sides
        self._uglu = list(uglu)
        if len(self._uglu) != self._sides:
            raise ValueError('Не верное количество углов!')

    def sides(self):
        return self._sides


class Chetrehug(Polygon):
    def __init__(self, uglu):
        Polygon.__init__(self, 4, uglu)

    def __str__(self):
        return "Это четерехугольник!"


class Triangle(Polygon):
    def __init__(self, uglu):
        Polygon.__init__(self, 3, uglu)

    def __str__(self):
        return "Это Треугольник!"
