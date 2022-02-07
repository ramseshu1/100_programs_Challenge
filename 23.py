a = [1,2,3,4,1,2,3,1,2,3,4,1,2,3,4,1,2,3,4,1,1,2,2,1,2,1,4]
b = a
count_dict ={}
count=0
for i in a:
    while i in a:
        b.remove(i)
        count=count+1
    count_dict[i] = count



