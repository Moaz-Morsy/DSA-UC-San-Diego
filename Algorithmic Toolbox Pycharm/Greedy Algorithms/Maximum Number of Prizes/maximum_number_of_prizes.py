# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    if n > 2:
        #k = n
        p = n
        c = [0]
        i = 1
        while (p != 0):
            if i > p:
                c.append(p+c[-1])
                c.pop(-2)
                p = 0
            else:
                c.append(i)
                p -= i
                i += 1
        summands = c[1:]
        return summands
    else:
        summands.append(n)
        return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
