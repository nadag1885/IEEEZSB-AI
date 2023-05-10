import statistics
def measures_of_spread(list1):
    list1.sort()
    x=len(list1)
    maximum=list1[x-1]
    minimum=list1[0]
    rangee=maximum-minimum
    q2 = statistics.median(list1)
    q1 = statistics.median(list1[0: x // 2])
    q3 = statistics.median(list1[(x + 1) // 2: x])
    iqr=q3-q1
    variance = statistics.variance(list1)
    std_dev = statistics.stdev(list1)
    print(f" min : {minimum} \n Q1 : {q1} \n Q2 : {q2} \n Q3 : {q3} \n max : {maximum} \n Range : {rangee} \n IQR : {iqr} \n Variance : {variance} \n Standard deviation : {std_dev} ")

user_list=input("enter a list").split()
list1=[int(num) for num in user_list]
measures_of_spread(list1)