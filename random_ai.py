from ants import PlayerAI

import random


class Player(PlayerAI):
    targetFood = None

    def __init__(self):
        super(Player, self).__init__('Laur')

    def update(self, player_positions, food_positions):
        if targetFood != None:
            food = random.choice(food_positions)

        return targetFood[0] - self.position[0], targetFood[1] - self.position[1]
