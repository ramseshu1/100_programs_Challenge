# S = 1**2 + 2**2 + 3**2 + ........ + n**2

n = int(input("Enter the value of n "))

if n<0:
    n=n*-1

sum = 0
for  x in range(1,n+1):
    sum = sum + x**2

print(sum)