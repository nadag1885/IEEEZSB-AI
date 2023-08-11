#problem1
N= int(input("enter a number: "))
sum=(N * (N+1))/2
print("the summation of the numbers that between 1 and ",N, "is", sum)


#problem 2
A =int(input("enter first number"))
B = int(input("enter second number"))
C = int(input("enter third number"))
numbers=[A , B ,C]
numbers.sort()
print(numbers[0],numbers[1],numbers[2])



#problem 3
x=int(input("enter a number: "))
i=1
factor=1
while i<=x :
    factor*=i
    i+=1
print("the factorial of ",x, "is : ",factor)




#problem 4
user_list=input("enter a list")
list1= user_list.split()
unique=list(set(list1))
print(unique)



# problem 5
# output >>>  false
# in The round() function, Exact halfway cases are rounded to the nearest even result instead of away from zero.
# round(6.5) >>>  6
# round(3.5) >>>  4
# round(6.5)-round(3.5) >>>  2
