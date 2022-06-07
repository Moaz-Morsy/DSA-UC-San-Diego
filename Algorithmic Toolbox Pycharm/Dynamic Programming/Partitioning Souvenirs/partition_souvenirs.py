# python3

from itertools import product
from sys import stdin


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    def mat(capacity,values):
        V = []
        for i in range(0,len(values)+1):
            v = []
            v.append(0)
            for j in range(1,capacity+1):
                v.append(0)
            V.append(v)
        return V

    if sum(values)%3 != 0:
        return 0
    else:
        capacity = sum(values)//3
        V = mat(capacity,values)

        for i in range(1,len(values)+1):
            for w in range(0,capacity+1):
                V[i][w] = V[i-1][w]
                if values[i-1] <= w:
                    val = V[i-1][w-values[i-1]]+values[i-1]
                    if V[i][w] < val:
                        V[i][w] = val

        if V[-1][-1] == sum(values)//3:
            return 1
        else:
            return 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
