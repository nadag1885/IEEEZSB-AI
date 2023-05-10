def mean_measure(list1):
    mean=sum(list1)/len(list1)
    print(f"mean:{mean}")

def median_measure(list1):
    list1.sort()
    x=len(list1)
    if x%2==0:
        mid=x/2
        median=(list1[int(mid)]+list1[int(mid-1)])/2
    elif x%2!=0:
        median=list1[int((x-1)/2)]
    print(f"median:{median}")        

def mode_measure(list1):
    max=0
    for i in list1:
        x=list1.count(list1[i])
        if x > max :
            max=x
            mode=list1[i]
    print(f"mode:{mode}")          


    
user_list=input("enter a list").split()
list1=[int(num) for num in user_list]
mean_measure(list1)
median_measure(list1)
mode_measure(list1)
    
