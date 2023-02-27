dict = {}
n = int(input())
for i in range(n):
    a = input().split()
    a, b = a[0], int(a[1])
    dict.update({a: b})

print(dict)