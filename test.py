from construct import Construct
from player import Player

player = Player("Ash")
world = Construct()
world.join(player)
for i in range(0,10):
    world.travel(player)
