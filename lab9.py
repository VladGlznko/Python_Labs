class Lab9:
    def task1_1(self):
        # створення змінної title
        title = 'Days of the Week:\n'
        # відкриття файлу для читання
        f = open('days.txt', 'r')

        # відкриття файлу для запису
        g = open('new_days.txt', 'w')
        # зчитування вмісту файлу days.txt у змінну days
        days = f.read()
        # запис до файлу new_days.txt заголовка
        g.write(title)
        # запис до файлу new_days.txt змінної days
        g.write(days)
        # закриття файлів
        f.close()
        g.close()
        # повідомлення про виконання програми
        print('The program is executed. Check the file')

    def task1_2(self):
        # ініціалізація нумератора рядків
        line_number = 0

        # відкриття файлів для читання та запису
        with open('days.txt', 'r') as f, open('num_days.txt', 'w') as g:
            # цикл опрацювання файлів
            for line in f:
                line_number += 1
                g.write('{:>4}. {}\n'.format(line_number, line))

        # повідомлення про виконання програми
        print("The programme is completed. Check the file.")

    def task2(self):
        # Вміст вірша
        poem_title = "Сніг"
        poem_lines = [
            "Сніг землю вкрив, неначе пух",
            "Білий, як він, усе навкруг.",
            "І сонце, немов заховавшись,",
            "Під ним із сльозою крижаною",
            "Скрізь іскристою стежкою",
            "Тримає шляхи протоптані.",
            "І ті, хто їде, й ті, що йдуть,",
            "Слідами білими гойдають."
        ]

        # Ім'я та прізвище автора
        author_name = "Тарас Шевченко"

        # Запис у файл
        with open("poem.txt", "w") as file:
            file.write(f"Назва вірша: {poem_title}\n\n")
            for line in poem_lines:
                file.write(f"{line}\n")
            file.write(f"\nАвтор: {author_name}")

        # Виведення на екран
        with open("poem.txt", "r") as file:
            print(file.read())

    def task3(self):
        with open("input1.txt", "r") as input_file:
            lines = input_file.readlines()

        with open("output1.txt", "w") as output_file:
            for line in lines:
                line = line.rstrip()
                output_file.write(f"{line}!\n")

        print("Файл успішно переписано з додаванням символу '!' в кінець кожного рядка.")

    def task4(self):
        import math

        # Відкриття початкового файлу для читання
        with open("input2.txt", "r") as input_file:
            # Читання чисел і фільтрація точних квадратів
            numbers = [int(num.strip()) for num in input_file.readlines()]

        # Відкриття нового файлу для запису
        with open("sum_min_max.txt", "w") as output_file:
            # Запис суми мін та макс числа у новий файл
            output_file.write(f"{min(numbers) + max(numbers)}\n")

        print("Сума мін та макс була успішно записана у файл 'sum_min_max.txt'.")