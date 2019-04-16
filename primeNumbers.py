a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    r = []
    if(i == 1):
        continue
    initialDisvisor =2
    for j in range(initialDisvisor,i):
        remainder = i % j
        r.append(remainder)
    if 0 not in r:
        print (i)




    
    # remainder = i % initialDisvisor
    # if(remainder == 0):
    #     continue
    # else:
    #     initialDisvisor = initialDisvisor + 1
    #     if(initialDisvisor >= i):
    #         print(i)

