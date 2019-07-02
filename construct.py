from core import Block
from core import Blockchain
from player import Player
import random

class Construct:
    playerList = []
    diff = 5
    tier1 = ['Magikarp', 'Poliwag', 'Goldeen', 'Tentacool', 'Staryu', 'Kingler', 'Slowpoke', 'Krabby', 'Horsea','Gyrados']
    tier2 =['Rapidash', 'Xatu', 'Pidgey', 'Wurmple', 'Starly', 'Hoothoot', 'Pineco']

    worldChain = Blockchain()

    def updateTier(player):
        if(player.getLevel() > 20 ):
            second = tier1
            second.append(tier2)
            self.playerList[player] = second

    def join(self, player):
        playerList.append(player, tier1)

    def travel(self, player):
        data = {
            'name': str(random.choice(playerList[player])),
            'level': random.randint(player.getLevel - self.adiff + 2, player.getLevel + self.diff)
        }
        player.receivePokemon(worldChain.mine(Block(data, player.getLevel())))
        updateTier(player)
