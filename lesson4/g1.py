a = list(map(int, input().split()))
x = int(input())
if x in a:
    a.remove(x)
    print(a)
else:
    print(f"числа {x} нет в вашем массиве")