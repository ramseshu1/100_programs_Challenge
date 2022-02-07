#LCM of lot of numbers using loops and functions


def lcm(*args):

    number1=[]

    for i in numbers:
        number1.append(int(i))

    number1.sort()

    lcm1 = 1
    for i in range(1,number1[0]):
        j%i==0 for j in number1
        
        if(small%i==0 and large%i==0):
            small=small/i
            large=large/i
            lcm1=lcm1*i
            #print(lcm1)

    lcm1=lcm1*small*large
    print(lcm1)


numbers = input("Enter the numbers")

lcm(numbers)