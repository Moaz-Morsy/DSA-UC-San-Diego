# python3


# def build_heap(data):
#     """Build a heap from ``data`` inplace.

#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps

def heapify(arr, n, i):
    # Find smallest among root and children
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    # If root is not smallest, swap with smallest and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        arr.append((i, smallest))
        heapify(arr, n, smallest)
  
  
def Buildheap_min(n, arr):

    # Build min heap
    for i in range((n//2)-1, -1, -1):
        heapify(arr, n, i)




# def main():
#     n = int(input())
#     data = list(map(int, input().split()))
#     assert len(data) == n

#     swaps = build_heap(data)

#     print(len(swaps))
#     for i, j in swaps:
#         print(i, j)
def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    Buildheap_min(n, data)
    swaps = data[n:]

    print(len(swaps))
    for i in range(len(swaps)):
        print(swaps[i][0], swaps[i][1])

if __name__ == "__main__":
    main()
