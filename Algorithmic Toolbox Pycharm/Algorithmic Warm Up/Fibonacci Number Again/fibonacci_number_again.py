# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    def pisano_period(m):
        p = list([])
        p.append(0)
        p.append(1)
        for i in range(2, (m*m)+1):
            p.append((p[i-2]+p[i-1]) % m)
            if (p[-2] == 0) and (p[-1] == 1):
                return len(p[:-2])

    #return pisano_period(m)
    if n <= 1:
        return n
    p = pisano_period(m)
    #n = n % p
    F = list([])
    F.append(0)
    F.append(1)
    for i in range(2, p+1):
        F.append((F[i-2]+F[i-1]) % m)
        #if (F[-2] == 0) and (F[-1] == 1) :
    return F[n % p]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
