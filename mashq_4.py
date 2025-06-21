# 4.   10 ta random son chiqaruvchi threadlar
# Har bir thread bitta random son chiqarsin. Ular tartibsiz chiqishi kerak.
import threading
import random
def random_son():
    x = random.randint(1, 100)
    print(x)
n = []
for i in range(10):
    t = threading.Thread(target=random_son)
    n.append(t)
    t.start()
for i in n:
    t.join()










