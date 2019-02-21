from player import Player
from village import Village
import random

def spawn(count):
    for i in range(count):
        new_player = Player('Jake' + str(i + 1))

        new_village = Village(new_player.name)
        new_player.villages += [new_village]
        players[new_player.name] = new_player

players = {}
spawn(10)

while True:
    task = input('Keep going? ')

    for k in players:
        player = players[k]

        for village in player.villages:
            village.gather()

            # Random number to determine tendency
            rand = random.random()

            if village.resources > 0:
                if rand < player.tendencies['points']:
                    village.points += village.resources
                    village.resources = 0
                else:
                    rand -= player.tendencies['points']
            
            if village.resources > 0:
                if rand < player.tendencies['offense']:
                    village.axemen += village.resources
                    village.resources = 0
                else:
                    rand -= player.tendencies['offense']

            if village.resources > 0:
                village.swordsmen += village.resources
                village.resources = 0

            village.display()


