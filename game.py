# game.py
# Authors:
#
# This file should run your game.
#
######################################################################

from quest.game import QuestGame
from quest.map import TiledMap
from quest.dialogue import Dialogue
from quest.modal import Modal, DialogueModal
from quest.sprite import QuestSprite, Player, Wall, NPC
from quest.helpers import scale, resolve_resource_path
from quest.strategy import RandomWalk
import arcade
import os
from pathlib import Path

class Game(QuestGame):
    # 💻 YOUR CODE GOES HERE 💻 #
    # Hint: You may want to look at how the example games are set up #
    
    


if __name__ == '__main__':
    game = Game()
    game.run()