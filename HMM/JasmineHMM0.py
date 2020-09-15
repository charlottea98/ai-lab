def output(pie, A, B):
    X_one = [[sum(a*b for a, b in zip(X_row, Y_col))
              for Y_col in zip(*A)] for X_row in pie]
    O_one = [[sum(a*b for a, b in zip(X_row, Y_col))
              for Y_col in zip(*B)] for X_row in X_one]
    rows = len(O_one)
    columns = len(O_one[0])
    O_one[0].insert(0, rows)
    O_one[0].insert(1, columns)
    for i in O_one:
        print(*i)


def create_matrix(inputlist):
    columns = int(inputlist[1])
    inputlist.pop(0)
    inputlist.pop(0)
    amount_of_cells = len(inputlist)
    matrix = [inputlist[i:i+columns]
              for i in range(0, amount_of_cells, columns)]

    return matrix


def main():
    A = list(map(float, input().strip().split()))
    B = list(map(float, input().strip().split()))
    pie = list(map(float, input().strip().split()))
    pie_matrix = create_matrix(pie)
    B_matrix = create_matrix(B)
    A_matrix = create_matrix(A)
    output(pie_matrix, A_matrix, B_matrix)
