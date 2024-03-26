class Lab8:
    __text = ("Python is a widely used high-level programming language. "
            "It was created by Guido van Rossum and first released in 1991. "
            "Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")

    def task1(self):
        print("Репліка 1: \"Привіт, як справи?\"")
        print("Репліка 2: \"Все гаразд, дякую!\"")
        print("Репліка 3: \"Ти готовий до зустрічі завтра?\"")
        print("Репліка 4: \"Так, звичайно, з нетерпінням чекаю!\"")

    def task2(self):
        string = "the early bird gets the worm"
        print("2.1.:", string[10:13])
        print("2.2.:", string[4:-3])
        print("2.3.:", string[0:2])
        print("2.4.:", string[-1:1])
        print("2.5.:", string[:19])
        print("2.6.:", string[20:])

    def task3(self, text=__text, substring="Python"):
        index_first = text.find(substring)
        index_last = text.rfind(substring)
        print("Індекс першого входження підрядка:", index_first)
        print("Індекс останнього входження підрядка:", index_last)

    def task4(self, text=__text, substring="Python"):
        index = text.find(substring)
        while index != -1:
            print("Індекс входження підрядка:", index)
            index = text.find(substring, index + 1)

    def task5(self, text=__text, substring="Python"):
        total_count = text.count(substring)
        interval_count = text[5:15].count(substring)  # Приклад інтервалу
        print("Кількість входжень підрядка у всьому рядку:", total_count)
        print("Кількість входжень підрядка у певному інтервалі:", interval_count)

    def task6(self, text=__text):
        modified_text = text.replace(".", "!").replace("№", "")
        reversed_text = modified_text[::-1]
        print("Змінений та реверсований рядок:", reversed_text)