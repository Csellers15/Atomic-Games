# from directions import random_direction, north, south, east, west, turn
from communication import build_move_command
from random import randint

import directions

from state import Unit, Tile
from mapping import Map

class FindBase:
    def __init__(self, game_map, unit, unit_manager):
        self.game_map = game_map
        self.unit = unit
        self.unit_manager = unit_manager


    def build_command(self, unit):
        cords = unit.location()

        # go in ceratin direction perm.
        if cords.y == 0 and cords.x == 0:
            direction = directions.random_direction()

        elif cords.y < 0:
            direction = directions.north()
            if self.game_map.can_move(unit.location(), direction.NORTH) == False:
                direction = directions.east()
                
        elif cords.y > 0:
            direction = directions.south()
            if self.game_map.can_move(unit.location(), direction.SOUTH) == False:
                direction = directions.west()

        elif cords.x > 0:
            direction = directions.east()
            if self.game_map.can_move(unit.location(), direction.EAST) == False:
                direction = directions.south()

        elif cords.x < 0:
            direction = directions.west()
            if self.game_map.can_move(unit.location(), direction.WEST) == False:
                direction = directions.north()

        
        # Enemy base is found, attack 
        # Gather Resources 
        # Create More workers if funds available 

        return build_move_command(unit, direction)