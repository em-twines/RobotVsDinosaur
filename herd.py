
class Herd:
    def __init__(self, dinosaur, dinosaur1, dinosaur2):
        self.name = "The Herd"
        self.dinosaur = dinosaur
        self.dinosaur1= dinosaur1
        self.dinosaur2 = dinosaur2
        self.health = self.dinosaur.health + self.dinosaur1.health + self.dinosaur2.health
        self.dinosaur_list_names = [self.dinosaur.name, self.dinosaur1.name, self.dinosaur2.name]
        self.dinosaur_list = [self.dinosaur, self.dinosaur1, self.dinosaur2]
        self.dino_dict = {
            self.dinosaur.name: self.dinosaur.health,
            self.dinosaur1.name: self.dinosaur1.health,
            self.dinosaur2.name: self.dinosaur2.health
        }
    #     self.herd_health = 0
    #     self.health = self.get_health_herd()

    # def get_health_herd(self):
    #     for value in self.dino_dict.values():
    #         self.herd_health += value
    #         print(self.herd_health)
            