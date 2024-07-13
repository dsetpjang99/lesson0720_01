import random


x = random.randint(1, 50)
print(x)
for i in range(5):
    y = eval(input("請猜一個數字："))
    i += 1

    if x == y:
        print("猜對了！")
        break
    else:
        if x > y:
            print("猜錯了，猜大一點！")
        else:
            print("猜錯了，猜小一點！")

if x != y:
    print(f"正確答案為{x}")
