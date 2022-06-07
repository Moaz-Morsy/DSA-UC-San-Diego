# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    def IsBetter(number,max_number):
        if int(str(number)+str(max_number)) > int(str(max_number)+str(number)):
            return True
        else:
            return False

    S = ""
    numbers = sorted(numbers, reverse=True)
    while not(numbers == []):
        max_number = 0
        for number in numbers:
            if IsBetter(number,max_number):
                max_number = number

        S += str(max_number)
        numbers.remove(max_number)

    return int(S)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
