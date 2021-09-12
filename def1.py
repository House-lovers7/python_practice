def sayhello():
    print("こんにちは")


sayhello()


def postTaxPrice(price):
    ans = price * 1.08
    return ans


print(postTaxPrice(100), "円")
print(postTaxPrice(500), "円")
print(postTaxPrice(990), "円")


def myfunc():
    print("Hello")


myfunc()
