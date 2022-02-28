while(True):
    temp = input()
    endletter = len(temp)
    for i in range(0,endletter):
        if(i==endletter-1):
            print(temp[i])
            break
        print(temp[i],end=",")
