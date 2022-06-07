# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    zipped_lists = zip(prices, weights)
    values = [x/y for x,y in zipped_lists]

    zipped_lists = zip(values, prices, weights)
    dummy = [(x,y,z) for x,y,z in zipped_lists]
    dummy = sorted(dummy, reverse=True)
    values = [ x for x,_,_ in dummy]
    prices = [ y for _,y,_ in dummy]
    weights = [ z for _,_,z in dummy]

    V = 0

    for i in range(len(weights)):
        while not (weights[i] == 0):
            take = min(weights[i],capacity)
            V += take*values[i]
            weights[i] -= take
            capacity -= take
            if (capacity == 0) or (sum(weights) == 0):
                return V


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
