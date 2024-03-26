class Lab7:
    def task1(self):
        # Geek Translator
        # Demonstrates using dictionaries

        geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
                "Googling": "searching the Internet for background information on a person.",
                "Keyboard Plaque": "the collection of debris found in computer keyboards.",
                "Link Rot": "the process by which web page links become obsolete.",
                "Percussive Maintenance": "the act of striking an electronic device to make it work.",
                "Uninstalled": "being fired.  Especially popular during the dot-bomb era."}

        choice = None
        while choice != "0":

            print(
                """
                Geek Translator
    
                0 - Quit
                1 - Look Up a Geek Term
                2 - Add a Geek Term
                3 - Redefine a Geek Term
                4 - Delete a Geek Term
                """
            )

            choice = input("Choice: ")
            print()

            # exit
            if choice == "0":
                print("Good-bye.")

            # get a definition
            elif choice == "1":
                term = input("What term do you want me to translate?: ")
                if term in geek:
                    definition = geek[term]
                    print("\n", term, "means", definition)
                else:
                    print("\nSorry, I don't know", term)

            # add a term-definition pair
            elif choice == "2":
                term = input("What term do you want me to add?: ")
                if term not in geek:
                    definition = input("\nWhat's the definition?: ")
                    geek[term] = definition
                    print("\n", term, "has been added.")
                else:
                    print("\nThat term already exists!  Try redefining it.")

            # redefine an existing term
            elif choice == "3":
                term = input("What term do you want me to redefine?: ")
                if term in geek:
                    definition = input("What's the new definition?: ")
                    geek[term] = definition
                    print("\n", term, "has been redefined.")
                else:
                    print("\nThat term doesn't exist!  Try adding it.")

            # delete a term-definition pair
            elif choice == "4":
                term = input("What term do you want me to delete?: ")
                if term in geek:
                    del geek[term]
                    print("\nOkay, I deleted", term)
                else:
                    print("\nI can't do that!", term, "doesn't exist in the dictionary.")

            # some unknown choice
            else:
                print("\nSorry, but", choice, "isn't a valid choice.")

        input("\n\nPress the enter key to exit.")

    def __init__(self):
        self.dictionary = {
            "Toyota": "BC1234",
            "Honda": "XY5678",
            "Ford": "ZA9876",
            "BMW": "FG4321",
            "Mercedes": "KL7890",
            "Audi": "RW3456",
            "Volkswagen": "MN6789",
            "Chevrolet": "PQ9012",
            "Nissan": "UV2345",
            "Hyundai": "DE7890"
        }

    def task2(self):
        key = input("Введіть ключ: ")
        value = self.dictionary.get(key)
        if value:
            print(f"Значення елемента з ключем '{key}': {value}")
        else:
            print("Елемент з таким ключем не знайдено.")

    def task3(self):
        value_to_find = input("Введіть значення для пошуку: ")
        if value_to_find in self.dictionary.values():
            print(f"Значення {value_to_find} є серед елементів словника.")
        else:
            print(f"Значення {value_to_find} не знайдено серед елементів словника.")

    def task4(self):
        sorted_dict = dict(sorted(self.dictionary.items(), key=lambda item: item[0]))
        print("Відсортований словник:")
        print(sorted_dict)

    def task5(self):
        tuple_list = list(self.dictionary.items())
        for key, _ in tuple_list:
            print(key)

    def task6(self):
        key_to_delete = input("Введіть ключ для видалення: ")
        del self.dictionary[key_to_delete]
        print("Словник після видалення:")
        print(self.dictionary)
        print("Довжина словника після видалення:", len(self.dictionary))

    def task7(self):
        new_dict = {
            "BMW": "FG4321",
            "Mercedes": "KL7890",
            "Audi": "RW3456",
        }
        self.dictionary.update(new_dict)
        print("Оновлений словник:")
        print(self.dictionary)
        print("Довжина оновленого словника:", len(self.dictionary))
        dict_copy = self.dictionary.copy()
        print("Копія словника:")
        print(dict_copy)

    def task8(self):
        topics_list = ["lists", "tuples", "dictionaries"]
        new_dict = dict.fromkeys(topics_list, "Python")
        print("Створений словник зі списку:")
        print(new_dict)
