import random

i = 0
x = random.randint(1, 50)
print(x)
while True:
    y = eval(input("請猜一個數字："))
    i += 1
    if x == y:
        print("猜對了！")
        break
    else:
        print("猜錯了！")
        if i < 5:
            print(f"還可以再猜{5-i}次")
        else:
            print(f"正確答案為{x}")
            break
