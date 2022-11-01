
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
        
        # if type(result) is not tuple:
        #     if dinosaur.attack_power_dict[result] < 15:
        #         var = 0
        #         dinosaur.attack_power_dict[result] = var
        #         return dinosaur.attack_power_dict, dinosaur.health
        #     else:             
        #         old_attack_damage = dinosaur.attack_power_dict.get(result)
        #         new_attack_damage = old_attack_damage - 15
        #         dinosaur.attack_power_dict[result] = new_attack_damage
        #         return dinosaur.attack_power_dict, dinosaur.health
        
        # elif type(result) is tuple:
        return result
         