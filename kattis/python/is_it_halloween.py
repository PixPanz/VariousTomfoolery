i = input().split()
ans = "nope"
if i[0] == "OCT":
    if i[1] == "31":
        ans = "yup"
if i[0] == "DEC":
    if i[1] == "25":
        ans = "yup"
print(ans)