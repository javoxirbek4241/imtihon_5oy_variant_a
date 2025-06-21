# 1.Fibonacci generatori
# Generator yozing: kiritilgan `n` ta fibonacci sonlarini chiqaradi


# 1-mashq

def fibo(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x, y = y, x+y

gen = fibo(10)

for i in gen:
    print(i)