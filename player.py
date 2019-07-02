class Player:
    name = None
    level = 0
    pokemonList = []
    location = "Pallet Town"

    def __init__(self, nickname):
        self.name = nickname

    def getPokemon(self):
        return pokemonList

    def getLevel(self):
        return self.level

    def updateLevel(self):
        sum = 0
        for block in pokemonList:
            data = block.data
            sum += data['level']
        self.level = sum/len(pokemonList)


    def receivePokemon(self, block):
        self.pokemonList.append(block)
        updateLevel()
