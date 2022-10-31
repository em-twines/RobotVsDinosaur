from random import randint

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
            attack_to_diminish = randint(0, len(dinosaur.attack_power_list)-1)
            attack_names = []
            attack_names = list(dinosaur.attack_power_dict.keys())
            #yields list of attack names.
            attack_name_to_diminish = attack_names[attack_to_diminish]
            #yeilds the attack name to be diminished
            attack_hp = dinosaur.attack_power_dict.get(attack_name_to_diminish)
            attack_hp -= 15
            print(f"Your opponent's {attack_name_to_diminish} attack now does {attack_hp} damage!")
        elif weapon_choice == "Electric Shock":
            dinosaur.health -= 20
            print (f"Your opponent's health is now {dinosaur.health}")
        elif weapon_choice == "AI":
            dinosaur.attack_power.attack_choice[0].remove
            print(dinosaur.attack_power)

