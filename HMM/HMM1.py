# 4 4 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.8 0.1 0.1 0.0
# 4 4 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.1 0.0 0.0 0.9
# 1 4 1.0 0.0 0.0 0.0
# 8 0 1 2 3 0 1 2 3

def alfa_t(A, prev_alfa, b_t):
    prevalfa_A = [[sum(a*b for a, b in zip(X_row, Y_col))
                   for Y_col in zip(*A)] for X_row in zip(*prev_alfa)]
    print(prevalfa_A, 'prealpha_A')
    alfa_t = []
    for i in range(len(prevalfa_A[0])):
        alfa_t.append([prevalfa_A[0][i]*b_t[i][0]])
    print(alfa_t, 'alfa_t')

    return alfa_t


def b_i_Ot(B, t):
    B_O = []
    for i in B:
        B_O.append([i[t]])
    return B_O


def output(pie, A, B, seq):
    B1 = b_i_Ot(B, seq.pop(0))
    print(B1, 'b1')
    # alfa1 = [[sum(a*b for a, b in zip(X_row, Y_col)) for Y_col in zip(*pie)] for X_row in B1]
    alfa1 = []
    print(pie[0])
    for i in range(len(pie[0])):
        alfa1.append([pie[0][i]*B1[i][0]])

    print(pie)
    print(alfa1, 'Alfa1')
    print(A, 'A')

    for i in seq:
        bi = b_i_Ot(B, i)
        alfa1 = alfa_t(A, alfa1, bi)

    summa = 0
    for item in alfa1:
        summa += item[0]
    print(round(summa, 6))


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
    seq = list(map(int, input().strip().split()))
    seq.pop(0)
    pie_matrix = create_matrix(pie)
    B_matrix = create_matrix(B)
    A_matrix = create_matrix(A)
    output(pie_matrix, A_matrix, B_matrix, seq)


main()
