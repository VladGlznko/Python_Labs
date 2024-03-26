import math


class Lab10:
    def fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def __f_3(self, x):
        return math.cos(x / 2)

    def task2(self, n):
        return self.task2_recursive(n, 0)

    def task2_recursive(self, n, sum):
        if n < 0:
            return sum

        return self.task2_recursive(n - 1, sum + round(self.__f_3(n), 4))
