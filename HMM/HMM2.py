def alfa_t(A, prev_alfa, b_t):

    alfa_t = []

    for i in range(len(b_t)):
        obs = []
        for j in range(len(A)):
            obs.append([prev_alfa[j][0] * A[j][i] * b_t[i][0], [i, j]])

        alfa_t.append(max(obs)) # den här är vektorn längst till höger
                                # för varje uträkning som i tutorial övningen
                                # där j = vilken state som är max för varje rad
                                # och i är vilken rad
    return alfa_t


def b_i_Ot(B, t):
    B_O = []
    for i in B:
        B_O.append([i[t]])
    return B_O


def output(pie, A, B, seq):
    B1 = b_i_Ot(B, seq.pop(0))
    alfa1 = []
    pi_max = []
    for i in range(len(pie[0])):
        alfa1.append([pie[0][i]*B1[i][0]])
        pi_max.append([pie[0][i], [i, i]]) #lägger dit [i, i] för att den ska matcha formatet 
                                            #de andra har som har två värden

    states = []
    states.append(pi_max)
    for i in seq:
        bi = b_i_Ot(B, i)
        alfa1 = alfa_t(A, alfa1, bi)
        states.append(alfa1)

    states.reverse()

    output = [[]]

    # backtrack starts
    best_seq = max(states[0])
    states.pop(0)
    i = best_seq[1][0]
    j = best_seq[1][1]

    output[0].append(i)

    for state in states:
        i = j
        j = state[i][1][1]
        output[0].append(i)

    output[0].reverse()

    for item in output:
        print(*item)


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
