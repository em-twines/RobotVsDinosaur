
#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon. 


from weapon import Weapon 

class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("")

    def attack(self, dinosaur):
        result = {}
        result = self.active_weapon.choose_weapon(dinosaur)
        if dinosaur.attack_power_dict.get(result) < 15:
            var = 0
            dinosaur.attack_power_dict[result] = var
            return dinosaur.attack_power_dict, dinosaur.health

        elif type(result) is tuple:
                return result
        else: 
            old_attack_damage = dinosaur.attack_power_dict.get(result)
            new_attack_damage = old_attack_damage - 15
            dinosaur.attack_power_dict[result] = new_attack_damage
            return dinosaur.attack_power_dict, dinosaur.health
    

    #     result = ()
    #     # if result != None == True:
    #     result = self.active_weapon.choose_weapon(dinosaur)
    #     if result0 != None == True:
    #         result0 = result[0]
    #         #name
    #         result1 = result[1]
    #         # index
    #         old_attack_damage = dinosaur.attack_power_dict.get(result0)
    #         new_attack_damage = old_attack_damage - 15
    #         dinosaur.attack_power_dict[result0] = new_attack_damage
    #         # dinosaur.attack_power_dict[result1] = new_attack_damage
    #         return dinosaur.attack_power_dict
    #     else:
    #         return result
    # # dinosaur.attack_power_dict[attack_name_to_change] = new_attack_damage
    # else:
    #     self.active_weapon.choose_weapon(dinosaur)
        