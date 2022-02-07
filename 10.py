#Fibonacci using recursion

first = 0
second = 1
third = 0

def fibonacci(num1,num2):
    third = num1 + num2
    print(third,"\n")
    fibonacci(num2,third)

print(first,second)

fibonacci(first, second)