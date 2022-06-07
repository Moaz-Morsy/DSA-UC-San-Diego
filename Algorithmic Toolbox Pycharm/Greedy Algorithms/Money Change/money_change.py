# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    change = []
    while not(money == 0):
        if money >= 10 :
            change.append(10)
        elif (money < 10) and (money >= 5):
            change.append(5)
        elif money < 5 :
            change.append(1)
        money = money - change[-1]

    return len(change)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
