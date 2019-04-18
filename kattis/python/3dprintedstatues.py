statues_needed = int(input())
printers = 1
days = 1
while printers < statues_needed:
    printers = printers * 2
    days += 1
print(days)