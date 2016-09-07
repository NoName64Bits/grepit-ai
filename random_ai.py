from ants import PlayerAI

import random


class Player(PlayerAI):
    targetFoodIndex = -1

    def __init__(self):
        super(Player, self).__init__('Laur')

    def update(self, player_positions, food_positions):
        if targetFoodIndex > (len(food_positions) - 1):
            targetFoodIndex = -1

        if targetFoodIndex == -1:
            targetFoodIndex = random.randint(0, len(food_positions) - 1)

        if food_positions[targetFoodIndex] == None:
            targetFoodIndex = random.randint(0, len(food_positions) - 1)

        targetFood = food_positions[targetFoodIndex]

        return targetFood[0] - self.position[0], targetFood[1] - self.position[1]
