#Trying to get prime numbers under a certain number


number = int(input("Enter number "))

prime = 0


for i in range(2,number+1):
    for j in range(2, i+1):
        print(i,j)
        if(i%j==0):
            break
        else:
            prime = j
        if(j==i-1):
            print(prime)