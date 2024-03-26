import math

class Lab2:
    def task1(self):
        eps = float(input('Уведіть необхідну точність -> '))

        s = 0
        i = 1

        add = 1 / (4 ** i)

        while add >= eps:
            s += add
            i += 1
            add = 1 / (4 ** i)

        # виведення результату
        print('s= {:.6f}'.format(s))

    def __print_information_of_number(self, number):
        print(f"Printed number {number}")

    def task2_a(self):
        for number in range(5):
            self.__print_information_of_number(number)

    def task2_b(self):
        for number in range(5, 10):
            self.__print_information_of_number(number)

    def task2_c(self):
        for number in range(1, 10, 2):
            self.__print_information_of_number(number)

    def task2_d(self):
        for number in range(-2, 5):
            self.__print_information_of_number(number)

    def task2_e(self):
        for number in range(100, 0, -20):
            self.__print_information_of_number(number)

    def __function_1(self, x):
        return 1 / math.sqrt(1 + x * x)

    def task3(self):
        for x in range(1, 11):
            print(f"[{x}] equals -> {self.__function_1(x)}")

    def task4(self, a, b):
        product = a
        for i in range(a, b - 1, -1):
            product += i
            print(f"The product in [{i}] equals {product}")

    def __function_2(self, x):
        return math.sqrt(math.pow(math.cos(x/2), 2))

    def task5(self, a, b):
        for x in range(a, b + 1):
            print(f"The result of [{x}] is {self.__function_2(x)}")

    def __function_3(self, x):
        return math.tan(0.5 * x) / (x * x * x + 7.5)

    def task6(self):
        for x in range(1, 12, 1):
            x_float = x / 10
            print(f"x = [{x_float}] result: {self.__function_3(x_float)}")

    def __function_4(self, n):
        return 1 / (math.pow(3, n) + 3 * n)

    def task7(self, n):
        sum = 0;
        if n > 0:
            for i in range(1, n + 1):
                sum += self.__function_4(n)

        print(f"Result: {sum} n = {n}")