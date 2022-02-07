#Factorlal

n = int(input("Emter the number "))

def func(n):
    for x in range(1,10000):
        if(n%x==0 and n!=0):
            print(x)
            n=n/x

func(n)
            

