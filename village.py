import random

class Village:
    def __init__(self, owner):
        self.owner = owner
        self.points = 0
        self.resources = 0
        self.axemen = 0
        self.swordsmen = 0
        self.x = 0
        self.y = 0

    def display(self):
        print('')
        print('%s (%s, %s)' % (self.owner, self.x, self.y))
        print('%s points' % (self.points))
        print('%s axemen' % (self.axemen))
        print('%s swordsmen' % (self.swordsmen))
    
    def gather(self):
        self.resources += random.randrange(0, 11)