def replace_min_max(path_file=None):
    if path_file is None:
        print("\nВведите числа через ','\n")
        matrix = [list(input("Строка "+str(i)+":").split(',')) for i in range(10)]
    else:
        matrix = [list(row.replace('\n', '').split(',')) for row in open(path_file, 'r').readlines()]
    # all values to int
    matrix = list(map(lambda x: list(map(int, x)), matrix))

    maximum = max(map(max, matrix))
    minimum = min(map(min, matrix))
    for i in range(len(matrix)):
        if minimum in matrix[i] or maximum in matrix[i]:
            # replace min on max and max on min
            matrix[i] = list(map(lambda x: maximum if x == minimum else (minimum if x == maximum else x), matrix[i]))

    if path_file is None:
        _ = [print(i) for i in matrix]
    else:
        file = open(path_file, 'w')
        _ = [file.write(str(i)[1:len(str(i))-1] + '\n') for i in matrix]
        file.close()


if __name__ == '__main__':
    replace_min_max(
         # 'matrix.txt'
    )
