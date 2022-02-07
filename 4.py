# S = 5**2 + 10**2 + 15**2 + ........ + 100**2

sum = 0
for  x in range(5,105,5):
    sum = sum + x**2

print(sum)