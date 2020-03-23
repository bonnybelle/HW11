# Реализовать класс со своей операцией сложения. Например класс точка с 3-мя координатами.
# Сложение - сложение соответствующих координат.


class SumPoint:
    def __init__(self, coordinates_1, coordinates_2, coordinates_3):
        self.coordinates_1 = coordinates_1
        self.coordinates_2 = coordinates_2
        self.coordinates_3 = coordinates_3
        self.result = []

    def process(self):
        if len(self.coordinates_1) != len(self.coordinates_2) != len(self.coordinates_3):
            return False
        for i in range(len(self.coordinates_1)):
            a = self.coordinates_1[i] + self.coordinates_2[i] + self.coordinates_3[i]
            self.result.append(a)
        return self.result


my_point = SumPoint([1, -2, -900], [1, -2, 9], [3, 3, 3])
print(my_point.process())
