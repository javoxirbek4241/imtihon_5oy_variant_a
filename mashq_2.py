# 2.n ta butun sonlardan iborat a massiv berilgan. b massivni hosil qiluvchi decorator yozilsin.
# b massivning har bir elementi quyidagicha hisoblanadi: b[k] = a[0] + a[1] + ... + a[k]


def deco(func):
    def wrapper(*args, **kwargs):
        s = []
        b = []
        natija = func(*args, **kwargs)
        for i in natija:
            s.append(i)
            b.append(sum(s))
        print(b)
    return wrapper
@deco
def test():
    return [1,2,3,4,5]
print(test())