p, q, s = map(int, input().split())
out = "no"
if s < p or s < q:
    out = "no"
elif s == 1:
    if p == 1 and q == 1:
        out = "yes"
    else: out = "no"
else:
    for sec in range(2, s):
        if p == 1 or q == 1:
            out = "yes"
        elif sec % p == 0 and sec % q == 0:
            out = "yes"
print(out)
#something still incorrect here