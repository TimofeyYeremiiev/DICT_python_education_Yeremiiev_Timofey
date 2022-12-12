def create_matrix(x, y):
    return {"rows": x, "columns": y, "nums": [[] for _ in range(0, x)]}


def get_matrix_from_input():
    print("Enter rows and columns:")
    temp = list(map(int, input(">").split()))
    matrix = create_matrix(temp[0], temp[1])
    print("Enter matrix:")
    for a in range(0, matrix["rows"]):
        matrix["nums"][a] = list(map(float, input(">").split()))[:matrix["columns"]]
    return matrix


def sum_matrix(matrix1, matrix2):
    if matrix1["rows"] != matrix2["rows"] or matrix1["columns"] != matrix2["columns"]:
        return "ERROR"
    matrix_res = create_matrix(matrix1["rows"], matrix2["columns"])
    for a in range(0, matrix_res["rows"]):
        matrix_res["nums"][a] = list(map((lambda x, y: x+y), matrix1["nums"][a], matrix2["nums"][a]))
    return matrix_res


def get_scalar_from_input():
    print("Enter scalar:")
    return int(input(">"))


def mul_matrix_by_scalar(matrix, scalar):
    matrix_res = create_matrix(matrix["rows"], matrix["columns"])
    for a in range(0, matrix["rows"]):
        matrix_res["nums"][a] = \
            list(map((lambda x, y: x*y), matrix["nums"][a], [scalar for _ in range(0, matrix["rows"])]))
    return matrix_res


def print_matrix(matrix):
    for a in range(0, matrix["rows"]):
        print(matrix["nums"][a])


def mul_matrix_by_matrix(matrix1, matrix2):
    if matrix1["columns"] != matrix2["rows"]:
        return "ERROR"
    matrix_res = create_matrix(matrix1["rows"], matrix2["columns"])
    for x in range(0, matrix1["rows"]):
        for y in range(0, matrix2["columns"]):
            res = 0
            for z in range(0, matrix1["columns"]):
                res += matrix1["nums"][x][z] * matrix2["nums"][z][y]
            matrix_res["nums"][x].append(res)
    return matrix_res


def transpose_matrix(matrix):
    matrix_res = create_matrix(matrix["rows"], matrix["columns"])
    for x in range(0, matrix_res["rows"]):
        for y in range(0, matrix_res["columns"]):
            matrix_res["nums"][x].append(matrix["nums"][y][x])
    return matrix_res


def transpose_matrix_pobob(matrix):
    return transpose_matrix(transpose_matrix_vertical(transpose_matrix_horizontal(matrix)))


def transpose_matrix_horizontal(matrix):
    matrix_res = {"rows": matrix["rows"], "columns": matrix["columns"],
                  "nums": list([list(reversed(matrix["nums"][a])) for a in range(0, matrix["columns"])])}
    return matrix_res


def transpose_matrix_vertical(matrix):
    matrix_res = {"rows": matrix["rows"], "columns": matrix["columns"],
                  "nums": list(reversed(matrix["nums"]))}
    return matrix_res


def minor(targ_matrix, x, y):
    mino = create_matrix(targ_matrix["rows"]-1, targ_matrix["columns"]-1)
    s = 0
    for a in range(0, targ_matrix["rows"]):
        if a != x:
            mas = targ_matrix["nums"][a].copy()
            mas.pop(y)
            mino["nums"][s] = mas
            s += 1
    return mino


def matrix_determinant(matrix):
    if matrix["rows"] != matrix["columns"]:
        return "ERROR"
    if len(matrix["nums"]) == 2:
        return matrix["nums"][0][0] * matrix["nums"][1][1] - matrix["nums"][0][1] * matrix["nums"][1][0]
    det = 0
    for i in range(0, matrix["columns"]):
        det += ((-1) ** i) * matrix["nums"][0][i] * matrix_determinant(minor(matrix, 0, i))
    return det


def minor_trans(matrix):
    if len(matrix["nums"]) == 2:
        return {"rows": matrix["rows"], "columns": matrix["columns"],
                "nums": list([[matrix["nums"][1][1], -matrix["nums"][1][0]],
                             [-matrix["nums"][0][1], matrix["nums"][0][0]]])}
    matrix_res = create_matrix(matrix["rows"], matrix["columns"])
    for x in range(0, matrix["rows"]):
        for y in range(0, matrix["columns"]):
            matrix_res["nums"][x].append(((-1)**(x+y)) * matrix_determinant(minor(matrix, x, y)))
    return matrix_res


def reversed_matrix(matrix):
    if matrix_determinant(matrix) == 0:
        return "ERR: det == 0 is true"
    return mul_matrix_by_scalar(transpose_matrix(minor_trans(matrix)), 1/matrix_determinant(matrix))


while True:
    print("""
    1. Add matrices
    2. Multiply matrix by scalar
    3. Multiply matrix by matrix
    4. Transpose matrix
    5. Determinant
    6. Reversed matrix
    0. Exit
    """)
    action = input("Choose your action: ")
    if action.isnumeric():
        match int(action):
            case 0: break
            case 1: print_matrix(sum_matrix(get_matrix_from_input(), get_matrix_from_input()))
            case 2: print_matrix(mul_matrix_by_scalar(get_matrix_from_input(), get_scalar_from_input()))
            case 3: print_matrix(mul_matrix_by_matrix(get_matrix_from_input(), get_matrix_from_input()))
            case 4:
                while True:
                    print("""   Transpose type
    1. Common
    2. Transpose Side diagonal
    3. Transpose horizontal
    4. Transpose vertical
    0. Exit
""")
                    action = input("Choose your action: ")
                    if action.isnumeric():
                        match int(action):
                            case 0: break
                            case 1: print_matrix(transpose_matrix(get_matrix_from_input()))
                            case 2: print_matrix(transpose_matrix_pobob(get_matrix_from_input()))
                            case 3: print_matrix(transpose_matrix_horizontal(get_matrix_from_input()))
                            case 4: print_matrix(transpose_matrix_vertical(get_matrix_from_input()))
            case 5: print("Det: " + str(matrix_determinant(get_matrix_from_input())))
            case 6: print_matrix(reversed_matrix(get_matrix_from_input()))
