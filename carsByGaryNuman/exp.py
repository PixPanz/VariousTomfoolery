# A short script to calculate number of time periods needed using increasing returns
# to reach a goal number from a given starting number
import math
count = 0
add = 0
start = int(input("start: ")) # Starting number
end = int(input("end: ")) # Goal number
rate = int(input("rate: ")) # Denom of fraction of start added each loop 
while (end > start):
    count += 1
    add = math.floor(start/rate)
    start += add
print(count)