#Fibonacci

def fibonacci(limit):
    first = 0
    second = 1
    third = 1
    print(first,end=" ")
    while(limit>third):
        print(third,end=" ")
        third = first + second
        first = second
        second = third


limit = int(input('Enter the positive integer\n'))
if(limit<0):
    print("Incorrect response")

fibonacci(limit)