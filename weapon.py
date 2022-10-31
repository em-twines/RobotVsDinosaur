import random

class Weapon():
    def __init__(self, name):
        self.name = name
        # self.attack_power = attack_power
        self.weapon_list = ["Electric Shock: take 20 hp", "Mind Control: -15 hp to one of your opponent's attacks", "AI: remove one of your opponent's attacks"]
        self.active_weapon = ""
    
    def choose_weapon(self, dinosaur):
        print("Hal")
        weapon_choice = input(f"Which attack would you like to use? {self.weapon_list}")
        if weapon_choice == "Mind Control":
            key, value = random.choice(list(dinosaur.attack_power.values())) 
            value -= 15
        elif weapon_choice == "Electric Shock":
            dinosaur.health -= 20
            print (f"Your opponent's health is now {dinosaur.health}")
        elif weapon_choice == "AI":
            dinosaur.attack_power.attack_choice[0].remove
            print(dinosaur.attack_power)

