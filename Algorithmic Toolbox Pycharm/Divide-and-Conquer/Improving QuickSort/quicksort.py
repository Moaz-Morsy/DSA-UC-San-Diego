# python3

from random import randint


def partition3(array, left, right):
    a = array
    l = left
    r = right
    x = a[left]
    i = left
    while (i <= r):
        if a[i] < x:
            a[i], a[l] = a[l], a[i]
            l += 1
            i += 1
        elif a[i] > x:
            a[i], a[r] = a[r], a[i]
            r -= 1
        else:
            i += 1

    return l, r


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    #make a call to partition3 and then two recursive calls
    #to randomized_quick_sort
    m1,m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
