number = int(input())
digits =[]
while(number>0):
    digits.append(number%10)
    number=number//10

[print(i,end=" ") for i in sorted(digits) if (i%2)==0]
print("")

 
for i in sorted(digits) :
    print(" ")
    if (i%2)!=0:
        print(i,end="")
