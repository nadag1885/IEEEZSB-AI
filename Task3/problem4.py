def user_data():
    with open("D:\IEEE\AI\Task3-Nada_Gamal\dummy_grades.txt","r") as f:
        users={}
        for line in f:
            line = line.strip().split()
            user_id = line[0]
            name = line[1]
            score = line[2]
            birthday = line[4]
            sex = line[6]
            users[user_id] = {'name': name, 'score': score, 'birthday': birthday, 'sex': sex}
        return users       

print(user_data()) 
  



