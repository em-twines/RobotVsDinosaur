
from urllib import robotparser
from robot import Robot
from dinosaur import Dinosaur 


class Battlefield():

    def __init__(self):
        self.robot = Robot("Hal")
        self.dinosaur = Dinosaur()
        self.dinosaur.name == "K-T"

    def display_welcome(self):
        print('''
        Welcome to Robot v Dinosaur, the simulation you've all been asking for, answering the question, 
        'Which is more resilient: nature or technology?' While history may have offered one resonse, we're here today to put history on trial. 
        Let's play: 'ROBOT! V! DINOSAUR!''')


    def display_winner(self):
        print('''
        And the winner is... {winner}! Congrtulations to both our participants today, and, as always, thanks to our amazing AUDIENCE! 
        Remember, none of this is possible without viewers like you. Thank you, and goodnight''')
    
    
    def battle_phase(self):
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)


    def run_game(self):
        self.display_welcome()
        battle_phase = 0
        while self.robot.health or self.dinosaur.health >= 0:
            self.battle_phase()
            battle_phase += 1

          