score = 90
if score >= 80:
    print("やったね")
    print("次もその調子だよ")

for i in range(10):
    print(5, "*", i, "=", 5*i)

scorelist = [64, 100, 78, 80, 72]
for i in scorelist:
    print(i)

print("累積合計値")
scorelist = [64, 100, 78, 80, 72]
total = 0
for i in scorelist:
    total = total + i
    print(total)
