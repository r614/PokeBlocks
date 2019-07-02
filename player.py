import random
from core import Block
class Player:
    name = None
    level = 0
    pokemonList = []
    location = "Pallet Town"

    def __init__(self, nickname):
        self.name = nickname
        starters = ['Charmander', 'Bulbasaur', 'Squirtle']
        genesisPokemon = {
            'name': str(random.choice(starters)),
            'level': 1
        }
        self.receivePokemon(Block(genesisPokemon))

    def getPokemon(self):
        return self.pokemonList

    def getLevel(self):
        return self.level

    def updateLevel(self):
        sum = 0
        for block in self.pokemonList:
            data = block.getdata()
            sum += data['level']
        self.level = sum/len(self.pokemonList)


    def receivePokemon(self, block):
        self.pokemonList.append(block)
        print(self.pokemonList)
        self.updateLevel()
