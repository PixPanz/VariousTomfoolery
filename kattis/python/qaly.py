import math

ans = 0.0
years = 0.0
n = int(input())
for i in range(n):
    temp = input().split()
    ans += (float(temp[0]) * float(temp[1]))
print(round(ans, 3))