# python3


def fibonacci_number_naive(n):
#    print("Compute F sub", n)
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)

#print(fibonacci_number_naive(40))
def fibonacci_number(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    F = list([])
    F.append(0)
    F.append(1)
    for i in range(2, n+1):
        F.append(F[i-2]+F[i-1])
    return F[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
