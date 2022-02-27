number_string = input()
answer=''
#Tens digit
digit1 = int(number_string[0]) + int(number_string[-2])
if digit1>=10:
    answer = answer.join(str(digit1-10))
    print(answer)
else:
    answer = answer.join(str(digit1))
#Ones digit
print("a",answer)
digit2 = int(number_string[1]) + int(number_string[-1])
if digit2>=10:
    answer =answer +answer.join(str(digit2-10))
    print('a',answer)
else:
    answer = answer + answer.join(str(digit2))

print(digit1,digit2,answer)