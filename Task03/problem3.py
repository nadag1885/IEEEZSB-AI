def closist (list1,target):
    list1.sort()
    a , b ,c ,d =list1[0] , list1[1] , list1[2] , list1[3]
    sum=a+b+c+d
    for i in range(1,len(list1)):
        for j in range(i+1,len(list1)):
            for k in range(j+1,len(list1)):
                for l in range(k+1,len(list1)):
                    close=list1[i]+list1[j]+list1[k]+list1[l]
                    if abs(close-target)<abs(sum-target):
                        sum=close
                        a,b,c,d=list1[i] , list1[j] , list1[k] , list1[l]
    print(a)
    print(b)
    print(c)
    print(d)

list1 = [1,2,3,4,7,12]
target=28
closist(list1,target)     
