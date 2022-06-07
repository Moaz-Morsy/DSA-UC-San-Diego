# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    V = []
    for i in range(0,len(weights)+1):
        v = []
        v.append(0)
        for j in range(1,capacity+1):
            v.append(0)
        V.append(v)

    for i in range(1,len(weights)+1):
        for w in range(0,capacity+1):
            V[i][w] = V[i-1][w]
            if weights[i-1] <= w:
                val = V[i-1][w-weights[i-1]]+weights[i-1]
                if V[i][w] < val:
                    V[i][w] = val

    return V[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
