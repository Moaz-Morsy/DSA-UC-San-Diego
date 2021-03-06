# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4

    def binary_search_inside(keys, low, high, query):
        while low <= high:
            mid = low + ((high-low) // 2)
            if query == keys[mid]:
                return mid
            elif query > keys[mid]:
                low = mid + 1
            elif query < keys[mid]:
                high = mid - 1
        return -1


    low = 0
    high = len(keys) - 1
    return binary_search_inside(keys, low, high, query)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
