class Lab3:
    def task1_1(self):
        price = 14.27
        n = int(input('Уведіть кількість товару -> '))

        if n != 0:
            cost = n * price
            print('Загальна вартість товару {:.2f} грн'.format(cost))
            print('Обчислено.')
            print('After conditional')

    def task1_2(self):
        amount = float(input("Уведіть вартість покупки -> "))

        if amount < 1000:
            discount = amount * 0.05
            print("Знижка складає {:.2f} грн".format(discount))
        else:
            discount = amount * 0.10
            print("Знижка складає {:.2f} грн".format(discount))

        to_pay = amount - discount
        print("До сплати {:.2f} грн".format(to_pay))

    def task1_3(self):
        score = int(input('Уведіть кількість балів -> '))
        if 90 <= score <= 100:
            letter = 'A'
        elif 82 <= score < 90:
            letter = 'B'
        elif 74 <= score < 82:
            letter = 'C'
        elif 64 <= score < 74:
            letter = 'D'
        elif 60 <= score < 64:
            letter = 'E'
        elif 35 <= score < 60:
            letter = 'Fx'
        elif 0 <= score < 35:
            letter = 'F'
        else:
            print('Такого рівня не існує')
            return

        print('Твій рівень -', letter)

    def task2(self):
        x = 11
        print(f"{2 < 5} {3 > 5} {x > 10} {2 * x < x} {type(True)}")

    def task3(self):
        try:
            a = int(input('Enter number a: '))
            b = int(input('Enter number b: '))

            max_value = a if a >= b else b
            print('max=', max_value)
        except ValueError:
            print("Please enter valid integers.")

    def task4(self, x, y, z):
        if x <= y <= z:
            return True
        else:
            return False

    def task5(self, month):
        months = {
            "січень": 31,
            "лютий": 28,  
            "березень": 31,
            "квітень": 30,
            "травень": 31,
            "червень": 30,
            "липень": 31,
            "серпень": 31,
            "вересень": 30,
            "жовтень": 31,
            "листопад": 30,
            "грудень": 31
        }

        month_lower = month.lower()

        if month_lower in months:
            return months[month_lower]
        else:
            return "Неправильно введена назва місяця"

lab = Lab3()

while True:
    task_choice = input("Введіть назву завдання (task1_1, task1_2, task1_3, task2, task3, task4, task5), або 'exit' для завершення: ")

    if task_choice == "task1_1":
        lab.task1_1()
    elif task_choice == "task1_2":
        lab.task1_2()
    elif task_choice == "task1_3":
        lab.task1_3()
    elif task_choice == "task2":
        lab.task2()
    elif task_choice == "task3":
        lab.task3()
    elif task_choice == "task4":
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            z = int(input("Enter z: "))
            if lab.task4(x, y, z):
                print("Послідовність є неспадною.")
            else:
                print("Послідовність не є неспадною.")
        except ValueError:
            print("Please enter valid integers.")
    elif task_choice == "task5":
        month_name = input("Введіть назву місяця (українською): ")
        print(f"У місяці {month_name} {lab.task5(month_name)} днів.")
    elif task_choice.lower() == 'exit':
        print("До побачення!")
        break
    else:
        print("Неправильне ім'я завдання.")
