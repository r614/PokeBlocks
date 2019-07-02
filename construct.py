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

    def updateTier(self, player):
        if(player.getLevel() > 20 ):
            second = self.tier1
            second.append(self.tier2)
            self.playerList[player] = second

    def join(self, player):
        self.playerList[player] = self.tier1

    def travel(self, player):
        data = {
            'name': str(random.choice(self.playerList[player])),
            'level': random.randint(0, int(player.getLevel()) + self.diff)
        }
        player.receivePokemon(self.worldChain.mine(Block(data), self.getDiff()))
        self.updateTier(player)

    def getDiff(self):
        avglevel = 0
        for players in self.playerList.keys():
            avglevel += players.getLevel()
        avglevel = avglevel/len(self.playerList.keys())
        return avglevel + self.diff
