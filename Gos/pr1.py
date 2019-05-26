from os import path
import numpy as np


def replace_min_max(path_file=None):
    # TODO: создать функции с чтением из файла
    if path_file is None:
        matrix = [[1, 5, 9],
                  [4, 2, 8],
                  [7, 1, 1]]
    else:
        print("\nВведите числа через ','\n")
        matrix = [list(input("Строка ", i).split(',')) for i in range(10)]
    maximum = max(map(max, matrix))
    minimum = min(map(min, matrix))
    for i in range(len(matrix)):
        if minimum in matrix[i] or maximum in matrix[i]:
            # replace min on max and max on min
            matrix[i] = list(map(lambda x: maximum if x == minimum else (minimum if x == maximum else x), matrix[i]))

    if path_file is None:
        _ = [print(i) for i in matrix]
    else:
        pass


if __name__ == '__main__':
    replace_min_max()