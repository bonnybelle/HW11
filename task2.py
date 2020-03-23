# Реализовать класс со своей операцией сложения. Например класс точка с 3-мя координатами.
# Сложение - сложение соответствующих координат.
import sys


class SumPoint:
    def __init__(self, points_1, points_2):
        self.points_1 = points_1
        self.points_2 = points_2
        self.result = []

    def process(self):
        if len(self.points_1) != len(self.points_2):
            sys.exit()
        for i in range(len(self.points_1)):
            a = self.points_1[i] + self.points_2[i]
            self.result.append(a)
        return self.result


coord = SumPoint([1, -2, -900], [1, -2, 9])
print(coord.process())
