class Lab13:
    __arr = [5, 1, 2, 3, 9, 8, 0]
    __target = 3

    def insertion_sort(self, A=__arr):
        # цикл сортування починається з другого елемента (індекс 1)

        for j in range(1, len(A)):
            # наступний елемент вставляється у відсортовану
            # елемент, з якого починається порівняння
            # переміщення ключового елемента поки він менший
            # за елемент відсортованої частини і
            # його індекс більший за -1

            key = A[j]
            i = j - 1

            while (i > -1) and key < A[i]:
                # переміщення елемента списку вправо
                # перехід до наступного елемента
                # A[i] не більше, ніж ключовий елемент,
                # який стає на місце з індексом i+1

                A[i + 1] = A[i]
                i = i - 1

            A[i + 1] = key
        return A

    def selection_sort(self, A=__arr):
        for i in range(len(A)):
            # визначення позиції для мінімального елемента
            min_position = i

            # знаходження мінімального елемента
            for j in range(i + 1, len(A)):
                if A[min_position] > A[j]:
                    min_position = j

            # обмін місцями знайденого мінімального елемента
            # і елемента на мінімальні позиції
            A[i], A[min_position] = A[min_position], A[i]

        return A

    def bubble_sort(self, A=__arr):

        # визначення діапазону для порівняння елементів
        # (1-ша ітерація: n, 2-га ітерація: n-1 і т.д.)
        for i in range(len(A) - 1, 0, -1):
            # Comparing within set range
            for j in range(i):
                # порівняння у заданому діапазоні
                if A[j] > A[j + 1]:
                    # обмін
                    A[j], A[j + 1] = A[j + 1], A[j]

        return A

    def binary_search_recursive(self, arr=__arr, low=0, high=5, x=__target):
        if high >= low:
            mid = low + (high - low)

            # Якщо елемент знаходиться прямо в середині
            if arr[mid] == x:
                return mid

            # Якщо елемент менший, ніж середній, шукаємо зліва
            elif arr[mid] > x:
                return self.binary_search_recursive(arr, low, mid - 1, x)

            # Якщо елемент більший, ніж середній, шукаємо справа
            else:
                return self.binary_search_recursive(arr, mid + 1, high, x)

        else:
            # Елемент не знайдено у масиві
            return -1

    def sort_cities_by_postal_code(self, file_path):
        # Відкриття файлу для читання
        with open(file_path, 'r', encoding="utf-8") as file:
            # Зчитування рядків з файлу
            lines = file.readlines()

            # Розбиття рядків на назву міста та поштовий індекс
            cities = [line.strip().split(' ') for line in lines]

            # Сортування міст за зростанням поштового індексу
            sorted_cities = sorted(cities, key=lambda city: int(city[1]))

            return sorted_cities

    def find_city_by_postal_code(self, sorted_cities, postal_code):
        # Пошук міста за заданим поштовим індексом
        for city in sorted_cities:
            if city[1] == postal_code:
                return city[0]
        return None