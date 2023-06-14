
from utils import move_and_click

class HundlerPoke:
    def __init__(self):
        self.count = 0  
        self.list_poke = [(21, 484), (21,531), (21,570), (21, 613), (21, 658), (21,702)]


    def check_poke_lenght(self):
        self.count = self.count % len (self.list_poke)

    def next(self):
        self.count += 1  
        self.check_poke_lenght()
        move_and_click(self.list_poke[self.count], 'right')

    def previues(self):
        self.count -=1   
        self.check_poke_lenght()
        move_and_click(self.list_poke[self.count], 'right')

poke = HundlerPoke()
     