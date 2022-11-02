
#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon. 


from weapon import Weapon 

class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.active_weapon = Weapon("")

    def attack(self, dinosaur):
        result = {}
        result = self.active_weapon.choose_weapon(dinosaur, self)    
        return result
         