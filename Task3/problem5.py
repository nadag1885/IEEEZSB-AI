from problem4 import user_data
dic=user_data()
# print(dic)
with open(r"D:\IEEE\AI\Task3-Nada_Gamal\busted.txt","w") as f:
    for user_id, data in dic.items():
        name = data['name']
        birthday = data['birthday']
        line = f"{user_id},{name},{birthday}\n"
        f.write(line)
