# S = 5**5 + 10**10 + 15**15 + ........ + 100**100

sum = 0
for  x in range(5,105,5):
    sum = sum + x**x

print(sum)