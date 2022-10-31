



#(10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power. 


class Dinosaur():
    def __init__ (self):
        self.name = "K-T"
        self.attack_power_list = ["Claw Cleaver: -20 hp", "Tail Spin: -15 hp", "Brutal Bite: -25 hp"]
        self.health = 100
        self.attack_power_dict = {
            "Claw Cleaver": -20,
            "Tail Spin": -15,
            "Brutal Bite": -25
        }

    def attack(self, robot):
        
        print(self.name)
        key = input(f"Which attack would you like to use? {self.attack_power_list}")
        for key, value in self.attack_power_dict.items():
            if key == "Claw Cleaver":
                attack = self.attack_power_dict.get("Claw Cleaver")
                robot.health -= attack
            elif key == "Tail Spin":
                attack = self.attack_power_dict.get("Tail Spin")
                robot.health -= attack
            elif key == "Brutal Bite":
                attack = self.attack_power_dict.get("Brutal Bite")
                robot.health -= attack        
            print(f"Your opponent's health is now {robot.health}.")
        
        

    


 
