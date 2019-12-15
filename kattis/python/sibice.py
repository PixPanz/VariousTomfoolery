import math
n,w,h = input().split()
m = math.sqrt(int(w)**2 + int(h)**2)
for i in range(int(n)):
    if int(input()) <= m: print('DA')
    else: print('NE') 