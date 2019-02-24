from player import Player
from village import Village
import random

# Spawn... move to seperate file
def spawn(width):
    for i in range(width):
        for j in range(width):
            new_player = Player(i * width + j, 'Jake' + str(i + 1))
            new_village = Village(new_player.name, i, j)
            new_player.villages += [new_village]
            players[new_player.id] = new_player

def get_village(x, y):
    for k in players:
        for village in players[k].villages:
            if village.x == x and village.y == y:
                return village

def attack()

# Initialize
players = {}
width = 3
spawn(width)

while True:
    # Get input
    task = input('Grow villages? Y/n: ')
    if task.lower() != 'n':

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

    # Get input
    task = input('Start combat? Y/n: ')
    if task.lower() != 'n':
        for k in players:
            player = players[k]

            for village in player.villages:

                if village.axemen + village.swordsmen > 0:

                    defenders = []
                    if village.x > 0:
                        defenders += ['l']
                    if village.x < width - 1:
                        defenders += ['r']
                    if village.y > 0:
                        defenders += ['t']
                    if village.y < width - 1:
                        defenders += ['b']

                    defender = defenders[random.randrange(0, len(defenders))]
                    
                    if defender == 'l':
                        defender = get_village(village.x - 1, village.y)
                    elif defender == 'r':
                        defender = get_village(village.x + 1, village.y)
                    elif defender == 't':
                        defender = get_village(village.x, village.y - 1)
                    elif defender == 'b':
                        defender = get_village(village.x, village.y + 1)

                    attack_odds = .5 + player.tendencies['offense']
                    attack_odds -= player.tendencies['defense'] + defender.points / 100

                    if attack_odds > random.random():
                        # attack(player.village, defender)
                        print('')
                        village.display()
                        print('attacks')
                        defender.display()
                        print('')


