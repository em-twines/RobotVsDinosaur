



#(10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power. 

from random import randint

class Dinosaur():
    def __init__ (self, name):
        self.name = name
        self.attack_power_list = ["Claw Cleaver: -20 hp", "Tail Spin: -15 hp", "Brutal Bite: -25 hp"]
        self.health = 100
        self.attack_power_dict = {
            "Claw Cleaver": 20,
            "Tail Spin": 15,
            "Brutal Bite": 25
        }


    def attack(self, robot):
        
        key = input(f"{self.name}: Which attack would you like to use? {self.attack_power_dict}")
        # for key, value in self.attack_power_dict.items():
        if key == "Claw Cleaver":
            attack = self.attack_power_dict.get("Claw Cleaver")
            robot.health -= attack
            print(f"Your opponent's health is now {robot.health}.")
            return robot.health, self.attack_power_dict
        elif key == "Tail Spin":
            attack = self.attack_power_dict.get("Tail Spin")
            robot.health -= attack
            print(f"Your opponent's health is now {robot.health}.")
            return robot.health, self.attack_power_dict
        elif key == "Brutal Bite":
            attack = self.attack_power_dict.get("Brutal Bite")
            robot.health -= attack        
            print(f"Your opponent's health is now {robot.health}.")
            return robot.health, self.attack_power_dict
        elif key == "Recover Attack":
            rand_int = randint(0, 2)
            if rand_int == 0:
                rand_int1 = randint(0, 2)
                list_options = ["Claw Cleaver", "Tail Spin", "Brutal Bite"]
                attack_to_restore = list_options[rand_int1]
                for key in self.attack_power_dict.keys():
                    if attack_to_restore == key:
                        print("Recover Attack was ineffective!")
                        return robot.health, self.attack_power_dict   
                else:
                    self.attack_power_dict[attack_to_restore] = 20
                    print(f"{attack_to_restore} has been restored! It now does 20 damage.")
            else: 
                print("Recover Attack was ineffective!")
            return robot.health, self.attack_power_dict
        elif key == "Recover Attack Strength":
            rand_int = randint(0, 2)
            if rand_int == 0:
                attack_names = []
                attack_names = list(self.attack_power_dict.keys())
                attack_names.remove("Recover Attack Strength")
                if "Recover Attack" in attack_names:
                    attack_names.remove("Recover Attack")
                    if len(attack_names) == 0:
                        print("You cannot use Recover Attack Strength without having any attacks that do damage!")
                        return robot.health, self.attack_power_dict

                    else: 
                        randint(0, len(attack_names)-1)
                        attack_name = attack_names[rand_int]
                        if self.attack_power_dict.get("attack_name") != 0:
                            print("Recover Attack Strength was ineffective!")
                            attack_names.append("Recover Attack Strength")
                            return robot.health, self.attack_power_dict
                        else:
                            self.attack_power_dict[attack_name] = 20
                            attack_names.insert(0, "Recover Attack")
                            return robot.health, self.attack_power_dict

                else:
                    randint(0, len(attack_names)-1)
                    attack_name = attack_names[rand_int]
                    if self.attack_power_dict.get(attack_name) != 0:
                        print("Recover Attack Strength was ineffective!")
                        attack_names.append("Recover Attack Strength")
                        return robot.health, self.attack_power_dict
                    else: 
                        self.attack_power_dict[attack_name] = 20
                        print(f"Recover Attack Strength restored 20 damage points to {attack_name}!")
                        attack_names.append("Recover Attack Strength")
                        return robot.health, self.attack_power_dict

            else:
                print("Recover Attack Strength was ineffective!")
                return robot.health, self.attack_power_dict

        else: 
            print("Input Error, forfeit round")
            return robot.health, self.attack_power_dict

        
        



 
