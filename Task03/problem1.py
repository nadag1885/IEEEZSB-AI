list1=[5,7,7,8,8,8,10]
even=list(filter(lambda num : (num %2==0),list1))
print(len(even))