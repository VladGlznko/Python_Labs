class Lab4:
    def __print_items(self, text, array):
        for item in array:
            print(f"{text} {item}")

    def task1(self):
        lens = ("10см", "5м", "100км", "20см", "10м", "200км", "5см", "2м", "20см", "10м")

        self.__print_items("Item: ", lens)

    def task2(self, k):
        lens = ("10см", "5м", "100км", "20см", "10м", "200км", "5см", "2м", "20см", "10м")

        print(f"Item in index {k} is {lens[k]}")

    def task3(self):
        tuple_1 = (1, 2, 3, 4, 5)
        tuple_2 = (6, 7, 8)
        tuple_3 = tuple_1 + tuple_2

        print(tuple_3)
        print(f"max is {max(tuple_3)}")
        print(f"min is {min(tuple_3)}")

    def task4(self):
        lens = ("10см", "5м", "100км", "20см", "10м", "200км", "5см", "2м", "20см", "10м")

        item = input("Enter the item: ")

        if item in lens:
            print(f"{item} exist in tuple!")
            print(f"Index of first {item} in tuple is {lens.index(item)}")
            print(f"Count of {item} in tuple is {lens.count(item)}")
        else:
            print(F"{item} doesn't exist in tuple!")

    def task5(self):
        lens = ("10см", "5м", "100км", "20см", "10м", "200км", "5см", "2м", "20см", "10м")

        print(type(list(lens)))

        self.__print_items("Item: ", lens)

    def task6(self):
        plants = ["роза", "тюльпан", "сосна", "лилія", "ромашка",
                  "орхідея", "мак", "калина", "папороть", "ірис"]

        self.__print_items("Plant: ", plants)

    def task7(self):
        plants = ["роза", "тюльпан", "сосна", "лилія", "ромашка",
                  "орхідея", "мак", "калина", "папороть", "ірис"]

        self.__print_items("Plant: ", plants)

        plants.append("тюльпан")
        plants.append("папороть")
        plants.append("ромашка")

        self.__print_items("Plant: ", plants)

    def task8(self, index, plant):
        plants = ["роза", "тюльпан", "сосна", "лилія", "ромашка", "орхідея", "мак", "калина", "папороть", "ірис"]

        plants.insert(index, plant)

        self.__print_items("Plant: ", plants)

    def task9(self):
        numbers_1 = [1, 2, 3]
        numbers_2 = [4, 5, 6]

        numbers_1.extend(numbers_2)

        self.__print_items("Number: ", numbers_1)

        print("Length is " + str(len(numbers_1)))
        print("Max is " + str(max(numbers_1)))
        print("Min is " + str(min(numbers_1)))

    def task10(self, number):
        numbers = [1, 2, 3, 4, 5, 6, 7, 3]

        if number in numbers:
            print(f"Number {number} exist in list!")
            print(f"Count of item {number} in list is {numbers.count(number)}")
            print(f"First index of item {number} in list is {numbers.index(number)}")
        else:
            print(f"Number {number} doesn't exist in list!")

    def task11(self):
        numbers = [1, 3, 5, 4, 2, 3, 5, 9, 8, 7, 6]

        numbers = sorted(numbers)
        print("Sorted array: ", end="")
        print(" ".join(map(str, numbers)))

        numbers = reversed(numbers)
        print("Reverse sorted array: ", end="")
        print(" ".join(map(str, numbers)))

    def task12(self, value):
        numbers = [1, 3, 5, 4, 2, 3, 5, 9, 8, 2, 7, 6]

        print("Before: ", end="")
        print(" ".join(map(str, numbers)))
        print("Length is " + str(numbers) + "\n")

        numbers.remove(value)
        print("After: ", end="")
        print(" ".join(map(str, numbers)))
        print("Length is " + str(numbers) + "\n")

    def task13(self):
        numbers = [1, 3, 5, 4, 2, 3, 5, 9, 8, 2, 7, 6]

        print(" ".join(map(str, numbers)))
        print("Length is " + str(numbers) + "\n")

        del numbers[:2]
        print(" ".join(map(str, numbers)))
        print("Length is " + str(numbers) + "\n")

        del numbers[-2:]
        print(" ".join(map(str, numbers)))
        print("Length is " + str(numbers) + "\n")

        del numbers[1::2]
        print(" ".join(map(str, numbers)))
        print("Length is " + str(numbers) + "\n")

    def task14(self):
        numbers = [5, 2, 5, 8]

        print(" ".join(map(str, numbers)))

    def task15(self):
        numbers = [5, 2, 5, 8]

        numbers = reversed(tuple(set(numbers)))

        print(" ".join(map(str, numbers)))