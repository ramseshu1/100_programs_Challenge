
def lcm(number1,number2):
    if(number2<number1):
        small = number2
        large = number1
    elif( number2 == number1):
        print(number1)
        return
    else:
        small = number1
        large = number2

    lcm1 = 1
    for i in range(1,small):
        if(small%i==0 and large%i==0):
            small=small/i
            large=large/i
            lcm1=lcm1*i
            #print(lcm1)

    lcm1=lcm1*small*large
    print(lcm1)


number1 = int(input("Enter the number 1 "))
number2 = int(input("Enter the number 2 "))

lcm(number1,number2)