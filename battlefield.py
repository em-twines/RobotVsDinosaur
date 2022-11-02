
from robot import Robot
from dinosaur import Dinosaur 
from herd import Herd
from fleet import Fleet


class Battlefield():

    def __init__(self):
        self.robot = Robot("Hal")
        self.robot1 = Robot("The Singularity")
        self.robot2 = Robot("Bender")

        self.dinosaur = Dinosaur("K-T")
        self.dinosaur1 = Dinosaur("Rex")
        self.dinosaur2 = Dinosaur("Little Foot")

        self.fleet = Fleet(self.robot, self.robot1, self.robot2 )
        self.herd = Herd(self.dinosaur, self.dinosaur1, self.dinosaur2)


    def display_welcome(self):
        answer = input('''
        Welcome to Robot v Dinosaur, the simulation you've all been asking for, answering the question, 
        'Which is more resilient: nature or technology?' While history may have offered one response, we're here today to put history on trial. 
        Let's play: 'ROBOT! V! DINOSAUR! 
        
        Would you like to play in single or group mode? (single/group)''')

        return answer

    def display_winner(self, winner):
        print(f'''
        And the winner is... {winner}! Congrtulations to both our participants today, and, as always, thanks to our amazing AUDIENCE! 
        Remember, none of this is possible without viewers like you. Thank you, and goodnight.''')
        exit()
    
    
    def battle_phase_individual(self):
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




#--------------------------------------------------------------------------------------------------------------------




    def battle_phase_group(self):
        battle_phase = 1


        while (self.fleet.robot.health > 0 or self.fleet.robot1.health > 0 or self.fleet.robot2.health > 0) and (self.herd.dinosaur.health > 0 or self.herd.dinosaur1.health > 0 or self.herd.dinosaur2.health > 0):
            result = []
            for key, value in self.fleet.robot_dict.items():
                result += (key, value)
        
            fighter = input(f"Robots: Choose a fighter {result}")
            if fighter == "Hal":
                fighter_int = 0
            elif fighter == "The Singularity":
                fighter_int = 1
            elif fighter == "Bender":
                fighter_int = 2
            else:
                fighter = input(f"I'm sorry, I didn't understand that request.Robots: Choose a fighter {result}")

            result_dino = []
            for key, value in self.herd.dino_dict.items():    
                result_dino += (key, value)

            opponent = input(f"Choose an opponent {result_dino}")
            if opponent == "K-T":
                opponent_int = 0
            elif opponent == "Rex":
                opponent_int = 1
            elif opponent == "Little Foot":
                opponent_int = 2
            else:
                opponent = input(f"I'm sorry, I didn't understand that request. Choose an opponent {result_dino}")

                if opponent == "K-T":
                    opponent_int = 0
                elif opponent == "Rex":
                    opponent_int = 1
                elif opponent == "Little Foot":
                    opponent_int = 2

            #robot attacks
            result = ()
            result = self.fleet.robot_list[fighter_int].attack(self.herd.dinosaur_list[opponent_int])
            self.herd.dinosaur_list[opponent_int].attack_power_dict = result[0]
            self.herd.dinosaur_list[opponent_int].health = result[1]
            self.herd.dino_dict[opponent] = result[1]
            

            if self.herd.dinosaur_list[opponent_int].health <= 0:
                self.herd.dinosaur_list[opponent_int].health == 0
                self.herd.dinosaur_list_names.remove(opponent)
                del self.herd.dino_dict[opponent]


                if (self.herd.dinosaur.health > 0 or self.herd.dinosaur1.health > 0 or self.herd.dinosaur2.health > 0):                
                    if len(self.herd.dinosaur_list[opponent_int].attack_power_dict) == 0 or (len(self.herd.dinosaur_list[opponent_int].attack_power_dict) == 1 and self.herd.dinosaur_list[opponent_int].attack_power_dict.get("Recover Attack Strength") != None):
                        self.herd.dinosaur_list[opponent_int].attack_power_dict["Recover Attack"] = 0
                        print(f"{self.herd.dinosaur_list[opponent_int].name} has unlocked 'Recover Attack!' If used, it will have a 1 in 3 chance of recovering one of their missing attacks!")
                    
                if (all(value == 0 for value in self.herd.dinosaur_list[opponent_int].attack_power_dict.values())) or (all(value == 0 for value in self.herd.dinosaur_list[opponent_int].attack_power_dict.values()) and self.herd.dinosaur_list[opponent_int].attack_power_dict.get("Recover Attack") != None and len(self.herd.dinosaur_list[opponent_int].attack_power_dict) > 1):
                    self.herd.dinosaur_list[opponent_int].attack_power_dict["Recover Attack Strength"] = 0
                    print(f"{self.herd.dinosaur_list[opponent_int.name]} has unlocked 'Recover Attack Strength!' If used, it will have a 1 in 3 chance of recovering 20 damage points on one of their attacks!")


                
            result_dino1 = []
            for key, value in self.herd.dino_dict.items():    
                result_dino1 += (key, value)

            fighter_dino = input(f"Dinosaurs: Choose a fighter {result_dino1}")
            if fighter_dino == "K-T":
                fighter_int_dino = 0
            elif fighter_dino == "Rex":
                fighter_int_dino = 1
            elif fighter_dino == "Little Foot":
                fighter_int_dino = 2

            result_robo = []
            for key, value in self.fleet.robot_dict.items():
                result_robo += (key, value)

            opponent_robo = input(f"Choose an opponent {result_robo}")
            if opponent_robo == "Hal":
                opponent_robo_int = 0
            elif opponent_robo == "The Singularity":
                opponent_robo_int = 1
            elif opponent_robo == "Bender":
                opponent_robo_int = 2



            #dinosaur attacks
            result_dino_attack = ()
            result_dino_attack = self.herd.dinosaur_list[fighter_int_dino].attack(self.fleet.robot_list[opponent_robo_int])
            self.fleet.robot_list[opponent_robo_int].health = result_dino_attack[0]
            self.fleet.robot_dict[opponent_robo] = result_dino_attack[0]
        
            if self.fleet.robot_list[opponent_robo_int].health <= 0:
                self.fleet.robot_list[opponent_robo_int].health == 0
                self.fleet.robot_list_names.remove(opponent_robo)      
                del self.fleet.robot_dict[opponent_robo]


            battle_phase += 1
            print(f"Battle Round :{battle_phase}")




    def run_game(self):
        answer = self.display_welcome()

        if answer == "single":
            self.battle_phase_individual()
            if self.robot.health <= 0:
                self.robot.health = 0
                self.display_winner(self.dinosaur.name)
            elif self.dinosaur.health <= 0:
                self.dinosaur.health = 0
                self.display_winner(self.robot.name)

        elif answer == "group":
            self.battle_phase_group()
            if self.fleet.robot.health <= 0 and self.fleet.robot1.health <= 0 and self.fleet.robot2.health<= 0:
                # self.fleet.fleet_health = 0
                self.display_winner(self.herd.name)
            elif self.herd.dinosaur.health <= 0 and self.herd.dinosaur1.health <= 0 and self.herd.dinosaur2.health<= 0:
                # self.herd.herd_health = 0
                self.display_winner(self.fleet.name)

        else:
            print("I'm sorry, I didn't understand that request.")
            self.run_game(self)
        
       


          