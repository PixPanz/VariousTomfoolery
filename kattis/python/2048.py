#too tired to think about this one right now
l1 = input().split()
l2 = input().split()
l3 = input().split()
l4 = input().split()
lol = [l1, l2, l3, l4]
direction = input()
ans = ""

if direction == 0: #left move
    for i in lol:
        for j in range(3):
            if i[j+1]: print('yup')
            #I don't know why I don't like this problem.


elif direction == 1: #up move
    print()

elif direction == 2: #right move
    print()

elif direction == 3: #down move
    print()

for i in lol:
    for j in i:
        ans += str(j) + " "
    print(ans.strip())
    ans = ''
