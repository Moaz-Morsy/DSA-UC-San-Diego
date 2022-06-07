# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    def MergeSort_m(array):
        a = array
        i = 0
        if len(a) == 0:
            return 'No array entered'
        if len(a) == 1:
            return a, i

        m =  (len(a)) // 2
        b, i1 = MergeSort_m(a[:m])
        i += i1
        c, i2 = MergeSort_m(a[m:])
        i += i2
        def merge(b,c):
            d = []
            i = 0
            while not(b == []) and not(c == []):
                if b[0] <= c[0]:
                    #i += 1
                    d.append(b[0])
                    b.remove(b[0])
                else:
                    i += len(b)
                    d.append(c[0])
                    c.remove(c[0])
            d = d+b+c
            return d, i
        a_prime, i3 = merge(b,c)
        i += i3
        return a_prime, i
    sorted_a, inv = MergeSort_m(a)
    return inv



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
