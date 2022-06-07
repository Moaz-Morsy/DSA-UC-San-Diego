# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    a = elements
    def ckeck_element(a):
        if len(a) == 0:
            return 0
        if len(a) == 1:
            return a[0]

        mid = len(a) // 2
        b = ckeck_element(a[:mid])
        c = ckeck_element(a[mid:])

        if a.count(b) > mid:
            return b
        if a.count(c) > mid:
            return c
        return 0

    e = ckeck_element(a)
    if e == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
