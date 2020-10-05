d1, d2 = map(int, input().split())
s = d1 + d2
dic = {}
for i in range(2, s + 1):
    dic[i] = 0
for i in range(1, d1 + 1):
    for j in range(1, d2 + 1):
        dic[i + j] += 1
top = 0
out = []
for key in dic:
    if dic[key] == top:
        out.append(key)
    elif dic[key] > top:
        top = dic[key]
        out = []
        out.append(key)
    else: continue
for i in out:
    print(i) 