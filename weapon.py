from random import randint

class Weapon():
    def __init__(self, name):
        self.name = name
        # self.attack_power = attack_power
        self.weapon_list = ["Electric Shock: take 20 hp", "Mind Control: -15 hp to one of your opponent's attacks", "AI: Take a 1 in 3 chance to remove one of your opponent's attacks"]
        self.active_weapon = ""


    def mind_control(self, dinosaur):
        attack_to_diminish = randint(0, len(list(dinosaur.attack_power_dict.keys()))-1)
        attack_names = []
        attack_names = list(dinosaur.attack_power_dict.keys()) 
        #yields list of attack names.
        attack_name_to_diminish = attack_names[attack_to_diminish]
        #yeilds the attack name to be diminished
        attack_hp = dinosaur.attack_power_dict.get(attack_name_to_diminish)
        if attack_hp > 0:
            attack_hp -= 15
            if attack_hp < 0:
                attack_hp = 0
                print(f"Your opponent's {attack_name_to_diminish} attack now does 0 damage!")
                if dinosaur.attack_power_dict[attack_name_to_diminish] < 15:
                    var = 0
                    dinosaur.attack_power_dict[attack_name_to_diminish] = var
                    return dinosaur.attack_power_dict, dinosaur.health
                else:             
                    old_attack_damage = dinosaur.attack_power_dict.get(attack_name_to_diminish)
                    new_attack_damage = old_attack_damage - 15
                    dinosaur.attack_power_dict[attack_name_to_diminish] = new_attack_damage
                    return dinosaur.attack_power_dict, dinosaur.health
                # return attack_name_to_diminish
            else: 
                print(f"Your opponent's {attack_name_to_diminish} attack now does {attack_hp} damage!")
                if dinosaur.attack_power_dict[attack_name_to_diminish] < 15:
                    var = 0
                    dinosaur.attack_power_dict[attack_name_to_diminish] = var
                    return dinosaur.attack_power_dict, dinosaur.health
                else:             
                    old_attack_damage = dinosaur.attack_power_dict.get(attack_name_to_diminish)
                    new_attack_damage = old_attack_damage - 15
                    dinosaur.attack_power_dict[attack_name_to_diminish] = new_attack_damage
                    return dinosaur.attack_power_dict, dinosaur.health
                # return attack_name_to_diminish
        else:
            print("Mind Control has no effect.")
            return dinosaur.attack_power_dict, dinosaur.health
  

    def electric_shock(self, dinosaur):
            dinosaur.health -= 20
            print (f"Your opponent's health is now {dinosaur.health}")
            return dinosaur.attack_power_dict, dinosaur.health
        

    def ai(self, dinosaur):
        rand_int = randint(0, 2)
        if rand_int == 0:
            randint(0, len(dinosaur.attack_power_list)-1)
            attack_names = []
            attack_names = list(dinosaur.attack_power_dict.keys())
            attack_name = attack_names[0]
            dinosaur.attack_power_dict.pop(attack_name)
            print(f"Oh no! {dinosaur.name} just lost {attack_name} to AI!")
        else:
            print("AI has no effect!")
        return dinosaur.attack_power_dict, dinosaur.health


    def choose_weapon(self, dinosaur):
        weapon_choice = input(f"Which attack would you like to use? {self.weapon_list}")
        if weapon_choice == "Mind Control":
            result = self.mind_control(dinosaur)
            return result
        elif weapon_choice == "Electric Shock":
            result = self.electric_shock(dinosaur)
            return result
        elif weapon_choice == "AI":
            result = self.ai(dinosaur)
            return result
        else: 
            print("Input Error, forfeit round")
            return dinosaur.attack_power_dict, dinosaur.health


  


