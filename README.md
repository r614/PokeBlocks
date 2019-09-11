# PokeBlocks
MVP For a Blockchain Collector Game 

First iteration based on [Simple Python Blockchain](https://github.com/howCodeORG/Simple-Python-Blockchain/blob/master/blockchain.py).

* Players are able to join a world (construct) and start exploring (mining) for Pokemon (Blocks).
* Each Pokemon comes with a specific level (which is a random drop between 5 levels from the player's current level) and the player level is calculated by the average of all Pokemon in the party. 
* Difficulty scales according to the average global level of all players in a construct - it's much easier for a new player to scale upwards to the average, but the progression slows down once the average is reached.
* New Pokemon are unlocked as player level goes up, but the loot pool includes all previously attained Pokemon. 

# To-Do

* Add a flask backend and API.
* Simple Frontend for easier navigation.
