import random


def omikuji():
    kuji = ["大吉", "中吉", "小吉", "凶"]
    return random.choice(kuji)


kekka = omikuji()
print("御神籤のけっか発表", kekka, "じゃぞ!!!")
