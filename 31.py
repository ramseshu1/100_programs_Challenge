test_number = int(input())
number = input()
lower = int(number.split()[0])
upper = int(number.split()[1])
if test_number <upper and test_number>lower:
    print("yes")
else:
    print("no")