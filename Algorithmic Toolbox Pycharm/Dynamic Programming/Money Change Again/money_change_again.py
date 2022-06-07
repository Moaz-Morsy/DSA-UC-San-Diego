# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coins = [1,3,4]
    money_change = list()
    money_change.append(0)
    for m in range(1,money+1):
        money_change.append(float('inf'))
        for i in coins:
            if m >= i:
                value = money_change[m-i]+1
                if value < money_change[m]:
                    money_change[m] = value
    return money_change[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
