a = int(input())
b = int(input())
c = int(int((b % a == 0)) + int((a % b == 0)) >= 1)
print(c)