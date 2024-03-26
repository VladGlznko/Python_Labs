class Lab6:
    __matrix = [[8, 8, 3, 2], [4, 5, 6, 8], [7, 8, 9, 3], [4, 8, 5, 4]]

    def __print_matrix(self, matrix):
        for i in range(len(matrix)):
            print("  ".join(map(str, matrix[i])))
        print()

    def task1(self, x):
        matrix = self.__matrix

        count, indices = 0, []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == x:
                    count += 1
                    indices.append((i, j))

        self.__print_matrix(matrix)

        print(f"Count: {count}")
        print(indices)

    def task2(self, matrix=__matrix):
        min_elem = matrix[len(matrix) - 1][len(matrix) - 1]
        self.__print_matrix(matrix)

        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i >= j and i >= n - 1 - j:
                    if min_elem > matrix[i][j]:
                        min_elem = matrix[i][j]
                    print(f"{matrix[i][j]} ", end="")
            print()
        print()

        print(f"Min element of two triangles is {min_elem}")

    def task3(self, f_x, f_y):
        length = 5

        matrix = [["+" for _ in range(length)] for _ in range(length)]

        for i in range(length):
            matrix[i][f_x] = '-'

        for i in range(length):
            matrix[f_y][i] = '-'

        matrix[f_y][f_x] = "X"

        self.__print_matrix(matrix)