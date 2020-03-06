# A short script I wrote to easily calculate how many turns it would take to
# regain population from any given amount of population during a balacing meeting
# for Byte-le Royale 2020. We didn't really end up needing it but I kept it for a while
# mainly because the "rate" variable was originally called "babies" and that amused me :)
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
