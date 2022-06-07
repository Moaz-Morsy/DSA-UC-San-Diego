# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    c = [0]
    num = []
    for m in range(1,n+1):
        val_1 = c[m-1]+1
        val = val_1
        number = m-1
        if (m%2==0):
            val_2 = c[(m//2)]+1
            if val_2 < val:
                val = val_2
                number = m//2
        if (m%3==0):
            val_3 = c[(m//3)]+1
            if val_3 < val:
                val = val_3
                number = m//3
        c.append(val)
        num.append(number)
    k = n
    numbers = []
    num = [0]+num
    while k > 0:
        numbers.append(k)
        k = num[k]
#     numbers.reverse()
    numbers = sorted(numbers)
    c2 = list(map(lambda m: m-1,c))
    ops = len(numbers)-1
    return numbers


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
