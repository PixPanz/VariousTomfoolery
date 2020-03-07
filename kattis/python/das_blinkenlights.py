import math

p, q, s = map(int, input().split())
lcm = 0
if math.gcd(p,q) != 1:
    lcm = p*q / math.gcd(p,q)
else:
    if p < q:
        a = q
        q = p
        p = a
    if p % q == 0: lcm = p
    else: lcm = p*q

if lcm <= s:
    print("yes")
else: print("no")

#I had no idea Python didn't have a built in Least Common
#Multiple function built in. This actually took me a minute
#and around 5 failed submissions to iron out... embarassing.