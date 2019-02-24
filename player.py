import random

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tendencies = generate_tendencies()
        self.villages = []


def generate_tendencies():
    # Generate random tendencies totalling from 0 - 300
    tendencies = {
        'points': random.randint(0, 100),
        'offense': random.randint(0, 100),
        'defense': random.randint(0, 100)
    }

    # Attempt to balance tendencies so that total == 100
    total = sum(tendencies.values())
    ratio = 100 / total
    for tendency in tendencies:
        tendencies[tendency] = round(tendencies[tendency] * ratio)
    
    # Balance the remaining difference by changing points
    total = sum(tendencies.values())
    if total != 100:
        difference = 100 - total
        tendencies['points'] += difference

    # Convert tendencies from int to float with two decimal places
    for tendency in tendencies:
        tendencies[tendency] = round(tendencies[tendency] * .01, 2)

    # Return
    return tendencies
