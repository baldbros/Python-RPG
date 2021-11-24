import json 

data = json.load(open("data.txt"))

#Character experience gain part 
def exp_gain():
    data['hero_stats']['experience'] += 1
    for level in data['level_threshold']: 
        if data['hero_stats']['experience'] == data['level_threshold'][level]:
            print('You have reached ' + str(level) + '!!')

#Basic enemy 
class Monster:
    def __init__(self, MonsterName, MonsterExperience, MonsterLife, MonsterDamage):
        self.mn = MonsterName
        self.me = MonsterExperience
        self.ml = MonsterLife
        self.md = MonsterDamage

Ogre = Monster("Ogre", 1, 5, 2)

#Basic combat 
hero_damage = int(data['hero_stats']['strength']) + int(data['hero_stats']['weapon_damage'])

#Main game loop 
while True: 
    print("Ogre Spawned")
    current_monsters_life = int(Ogre.ml)
    print("Ogre has : " + str(current_monsters_life) + " Life")
    move = input("Do you attack?")
    if move == "yes":
        current_monsters_life -= hero_damage
    print("Ogre has : " + str(current_monsters_life) + " Life")
    



    exp_gained = input()
    if exp_gained == "yes":
        exp_gain()
        print(data['hero_stats']['experience'])

    
    json.dump(data, open("data.txt", "w"))
