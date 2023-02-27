a = list(map(int, input().split()))
x = int(input())
try:
    a.remove(x)
    print(a)
except:
    print(f"числа {x} нет в вашем массиве")