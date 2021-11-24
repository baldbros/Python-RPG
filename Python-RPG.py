import json 

data = json.load(open("data.txt"))

def exp_gain():
    data['hero_stats']['experience'] += 1
    for level in data['level_threshold']: 
        if data['hero_stats']['experience'] == data['level_threshold'][level]:
            print('You have reached ' + str(level) + '!!')

print(data['hero_stats']['experience'])

while True: 
    exp_gained = input()
    if exp_gained == "yes":
        exp_gain()
        print(data['hero_stats']['experience'])

    
    json.dump(data, open("data.txt", "w"))

   
    
