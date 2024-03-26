import math


class Lab3:
    def __f_1(self, x, y):
        return (x * x + x * y - y * y) / (1 + x + y) + (x - y) / (x * x + y  * y + 2)

    def task1(self, a, b):
        print("The result of u is " + str(self.__f_1(0.5, a) + self.__f_1(a + b, a - b)))

    def __f_2(self, x, n):
        return math.pow(-2, n) * math.pow(x, 2 * n)

    def task2(self, n):
        sum = 0
        for x in range(n + 1):
            sum += round(self.__f_2(x, n), 4)

        print(f"Result is {sum:.4f}")

