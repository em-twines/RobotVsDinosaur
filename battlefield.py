
from robot import Robot
from dinosaur import Dinosaur 


class Battlefield():

    def __init__(self):
        self.robot = Robot("Hal")
        self.dinosaur = Dinosaur()
        # self.dinosaur.name == "K-T"

    def display_welcome(self):
        print('''
        Welcome to Robot v Dinosaur, the simulation you've all been asking for, answering the question, 
        'Which is more resilient: nature or technology?' While history may have offered one response, we're here today to put history on trial. 
        Let's play: 'ROBOT! V! DINOSAUR!''')


    def display_winner(self, winner):
        print(f'''
        And the winner is... {winner}! Congrtulations to both our participants today, and, as always, thanks to our amazing AUDIENCE! 
        Remember, none of this is possible without viewers like you. Thank you, and goodnight.''')
    
    
    def battle_phase(self):
        battle_phase = 1

        while self.robot.health > 0 and self.dinosaur.health > 0:
            #robot attacks
            result = ()
            result = self.robot.attack(self.dinosaur)
            
            self.dinosaur.attack_power_dict = result[0]
            self.dinosaur.health = result[1]

            if self.dinosaur.health > 0:
                if len(self.dinosaur.attack_power_dict) == 0 or (len(self.dinosaur.attack_power_dict) == 1 and self.dinosaur.attack_power_dict.get("Recover Attack Strength") != None):
                    self.dinosaur.attack_power_dict["Recover Attack"] = 0
                    print(f"{self.dinosaur.name} has unlocked 'Recover Attack!' If used, it will have a 1 in 3 chance of recovering one of their missing attacks!")
                    
                if (all(value == 0 for value in self.dinosaur.attack_power_dict.values())) or (all(value == 0 for value in self.dinosaur.attack_power_dict.values()) and self.dinosaur.attack_power_dict.get("Recover Attack") != None and len(self.dinosaur.attack_power_dict) > 1):
                    self.dinosaur.attack_power_dict["Recover Attack Strength"] = 0
                    print(f"{self.dinosaur.name} has unlocked 'Recover Attack Strength!' If used, it will have a 1 in 3 chance of recovering 20 damage points on one of their attacks!")

                
                
                #dinosaur attacks
                result_dino_attack = ()
                result_dino_attack = self.dinosaur.attack(self.robot) 
                self.robot.health = result_dino_attack[0]
                self.dinosaur.attack_power_dict = result_dino_attack[1]
                    
                battle_phase += 1
                print(f"Battle Round :{battle_phase}")


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        if self.robot.health <= 0:
            self.robot.health = 0
            self.display_winner(self.dinosaur.name)
        elif self.dinosaur.health <= 0:
           self.dinosaur.health = 0
           self.display_winner(self.robot.name)



          