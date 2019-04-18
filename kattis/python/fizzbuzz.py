i = input().split()
fizz = int(i[0])
buzz = int(i[1])
count = int(i[2])
curr = 1
out = ""
while curr <= count:
    if curr % fizz == 0:
        if curr % buzz == 0:
            out = "FizzBuzz"
        else: 
            out = "Fizz"
    elif curr % buzz == 0:
        out = "Buzz"
    else: 
        out = curr
    print(out)
    curr += 1