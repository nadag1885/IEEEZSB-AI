list1=[4,2,3,1,7]
target=int(input("enter a number: "))
if list1.count(target) !=0:
    print(list1.index(target))
else :
    list1.sort()
    print(list1)
    for i in list1:
        if target<i:
            print(list1.index(i))
            break    