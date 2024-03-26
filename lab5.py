import random


class Lab5:
    def task1(self, length, left_border, right_border):
        return [random.randint(left_border, right_border) for _ in range(length)]

    def task2(self, length, left_border, right_border):
        numbers = self.task1(length, left_border, right_border)

        positive_numbers, negative_numbers  = [], []

        for num in numbers:
            if num >= 0:
                positive_numbers.append(num)
            else:
                negative_numbers.append(num)

        print("Згенерований масив: ", numbers)
        print("Позитивні числа:", positive_numbers)
        print("Негативні числа:", negative_numbers)

    def task3(self, length, left_border, right_border):
        numbers = self.task1(length, left_border, right_border)

        opposite_count = 0
        for i in range(1, len(numbers) - 1):
            if numbers[i] * numbers[i + 1] < 0 and numbers[i] * numbers[i - 1] < 0:
                opposite_count += 1

        print(numbers)
        print(opposite_count)