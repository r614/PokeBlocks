from core import Block
from core import Blockchain
from player import Player
import random

class Construct:
    playerList = {}
    diff = 5
    tier1 = ['Magikarp', 'Poliwag', 'Goldeen', 'Tentacool', 'Staryu', 'Kingler', 'Slowpoke', 'Krabby', 'Horsea','Gyrados']
    tier2 =['Rapidash', 'Xatu', 'Pidgey', 'Wurmple', 'Starly', 'Hoothoot', 'Pineco' ]

    worldChain = Blockchain()

    def updateTier(player):
        if(player.getLevel() > 20 ):
            second = tier1
            second.append(tier2)
            self.playerList[player] = second

    def join(self, player):
        playerList[player] = tier1

    def travel(self, player):
        data = {
            'name': str(random.choice(playerList[player])),
            'level': random.randint(player.getLevel - self.diff + 2, player.getLevel + self.diff)
        }
        player.receivePokemon(worldChain.mine(Block(data, getDiff())
        updateTier(player)

    def getDiff(self):
        avglevel = 0
        for players in self.playerList.keys():
            avglevel += players.getLevel()
        avglevel = avglevel/len(self.playerList.keys())
        return avglevel + self.diff
