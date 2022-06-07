# python3


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    def split_dataset(string):
        numbers = []
        operations = []
        for i in range(len(string)):
            if i%2==0:
                numbers.append(string[i])
            else:
                operations.append(string[i])
        return numbers, operations

    def matrix(n):
        Mat = []
        for i in range(0,len(n)):
            mat = []
            for j in range(0,len(n)):
                if i==j:
                    mat.append(n[i])
                else:
                    mat.append(0)
            Mat.append(mat)
        return Mat

    def MinAndMax(m,M,ops,i,j):
        mini = float('inf')
        maxi = float('-inf')

        for k in range(i,j):
            if ops[k]=='+':
                a = M[i][k] + M[k+1][j]
                b = M[i][k] + m[k+1][j]
                c = m[i][k] + M[k+1][j]
                d = m[i][k] + m[k+1][j]
                mini = min(mini,a,b,c,d)
                maxi = max(maxi,a,b,c,d)
            elif ops[k]=='-':
                a = M[i][k] - M[k+1][j]
                b = M[i][k] - m[k+1][j]
                c = m[i][k] - M[k+1][j]
                d = m[i][k] - m[k+1][j]
                mini = min(mini,a,b,c,d)
                maxi = max(maxi,a,b,c,d)
            elif ops[k]=='*':
                a = M[i][k] * M[k+1][j]
                b = M[i][k] * m[k+1][j]
                c = m[i][k] * M[k+1][j]
                d = m[i][k] * m[k+1][j]
                mini = min(mini,a,b,c,d)
                maxi = max(maxi,a,b,c,d)
        return mini, maxi

    numbers, operations = split_dataset(dataset)
    numbers = list(map(lambda x: int(x), numbers))
    M = matrix(numbers)
    m = matrix(numbers)

    for s in range(1,len(numbers)):
        for i in range(1,(len(numbers)-s)+1):
            j = i+s
            m[i-1][j-1], M[i-1][j-1] = MinAndMax(m,M,operations,i-1,j-1)

    return M[0][len(numbers)-1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
