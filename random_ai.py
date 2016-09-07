from ants import PlayerAI

import random


class Player(PlayerAI):
    def __init__(self):
        super(Player, self).__init__('Laur')

    def update(self, player_positions, food_positions):
        food = random.choice(food_positions)
        return food[0] - self.position[0], food[1] - self.position[1]
