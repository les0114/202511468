
def get_integer():
    return int(input("동전으로 교환하고자 하는 금액은?"))


def exchange(amount):
    coin_500 = amount // 500
    amount %= 500

    coin_100 = amount // 100
    amount %= 100

    coin_50 = amount // 50
    amount %= 50

    coin_10 = amount // 10
    amount %= 10


    print(f"500원 동전의 개수: {coin_500}")
    print(f"100원 동전의 개수: {coin_100}")
    print(f"50원 동전의 개수: {coin_50}")
    print(f"10원 동전의 개수: {coin_10}")


money = get_integer()
exchange(money)
