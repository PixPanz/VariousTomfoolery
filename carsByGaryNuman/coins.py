# simple script to calculate minimum number of coins needed to make change for any given amount
change = int(input()) # input should be in cents, not dollars
coins_needed = 0
coin_types = [25,10,5,1] # coin denominations - Only up to the quarter. Half-dollars are rare. Sorry JFK.
while change > 0:
    for coin in coin_types:
        if change - coin >= 0:
            change -= coin
            coins_needed += 1
            break
print(coins_needed)
# I wrote this because I was bored at work and was wondering what the most coins you could possibly need
# in order to break change under a dollar would be and I felt like it'd be fun to code in like 2 minutes
# Also I didn't code this at work thanks for asking I'm very good at staying on task, clearly.