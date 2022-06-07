# python3


def edit_distance(first_string, second_string):
    A = '0'+first_string
    B = '0'+second_string
    D = []
    for i in range(0,len(A)):
        d = []
        d.append(i)
        for j in range(1,len(B)):
            if i == 0:
                d.append(j)
            else:
                d.append(0)
        D.append(d)

    for j in range(1,len(B)):
        for i in range(1,len(A)):
            ins = D[i][j-1]+1
            det = D[i-1][j]+1
            mat = D[i-1][j-1]
            mis = D[i-1][j-1]+1
            if A[i]==B[j]:
                D[i][j] = min(ins,det,mat)
            else:
                D[i][j] = min(ins,det,mis)

    return D[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
