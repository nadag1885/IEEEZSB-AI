#question 1
with open("D:\IEEE\AI\Task3-Nada_Gamal\dummy_grades.txt","r") as f:
    users={}
    for line in f:
        line = line.strip().split()
        if line[2]=="N/A":
            continue
        user_id=line[0]
        user_data = {
            'name': line[1],
            'score': line[2],
            'birthday': line[4],
            'sex': line[6]
        }
        users[user_id] = user_data
    print(users)        

#question 2
with open("D:\IEEE\AI\Task3-Nada_Gamal\dummy_grades.txt","r") as f:
    oldest_user=2023
    oldest_id=0
    for line in f:
        line = line.strip().split()
        if int(line[4])<int(oldest_user):
            oldest_user=line[4]
            oldest_id=line[0]
    print("id of oldest user is :" +oldest_id)        


#question 3
with open("D:\IEEE\AI\Task3-Nada_Gamal\dummy_grades.txt","r") as f:
    sum=0
    for line in f:
        line = line.strip().split()
        if line[2]=="N/A":
            continue
        sum+=int(line[2])
    avg=int(sum/9)
    print(f"the average score is : {avg}")
    
#question 4
with open("D:\IEEE\AI\Task3-Nada_Gamal\dummy_grades.txt","r") as f:
    highest_score=0
    highest_sex=None
    for line in f:
        line = line.strip().split()
        if line[2]=="N/A":
            continue
        if int(line[2]) > int(highest_score) :
            highest_score=line[2]
            highest_sex=line[6]
if highest_sex == 'f':
    print("the sex of the user with the highest score is female")
elif highest_sex == 'm':
    print("the sex of the user with the highest score is male")

