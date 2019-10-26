# from directions import random_direction, north, south, east, west, turn
from communication import build_move_command, build_gather_command
from random import randint

import directions
# from  mapping import neighbors_with_enemies

from state import Unit, Tile



class FindBase:
    def __init__(self, game_map, unit, unit_manager):
        self.game_map = game_map
        self.unit = unit
        self.unit_manager = unit_manager


    def build_command(self, unit):
        cords = unit.location()
        # direction = directions.random_direction()

        # if mapping.has_resource_adjacent_to(unit.location()):
        #     communication.build_gather_command(unit, unit.location())
        #     while cords.y >0:
        #         cords.y = cords.y -1
        #         while cords.x > 0: 
        #             cords.x = cords.x - 1
        # go in ceratin direction perm.


        if cords.y == 0 and cords.x == 0:
            direction = directions.random_direction()

        # elif self.game_map.can_move(unit.location(), direction) == False:
        #     direction = directions.turn(directions.north())
                
        # elif self.game_map.can_move(unit.location(), direction) == False:
        #     direction = directions.turn(directions.south())

        # elif self.game_map.can_move(unit.location(), direction) == False:
        #     direction = directions.turn(directions.east())

        # elif self.game_map.can_move(unit.location(), direction) == False:
        #     direction = directions.turn(directions.west())
            
 
          
        elif cords.y < 0:
            direction = directions.north()
            if self.game_map.can_move(unit.location(), direction.NORTH) == False:
                direction = directions.east()
                if self.game_map.can_move(unit.location(), direction.EAST) == False:
                    direction = directions.south()
                    if self.game_map.can_move(unit.location(), direction.SOUTH) == False:
                        direction = directions.west()
                        if self.game_map.can_move(unit.location(), direction.WEST) == False:
                            direction = directions.north()

        elif cords.y > 0:
            direction = directions.south()
            if self.game_map.can_move(unit.location(), direction.SOUTH) == False:
                direction = directions.west()
                if self.game_map.can_move(unit.location(), direction.WEST) == False:
                    direction = directions.north()
                    if self.game_map.can_move(unit.location(), direction.NORTH) == False:
                        direction = directions.east()
                        if self.game_map.can_move(unit.location(), direction.EAST) == False:
                            direction = directions.south()

        elif cords.x > 0:
            direction = directions.east()
            if self.game_map.can_move(unit.location(), direction.EAST) == False:
                direction = directions.south()
                if self.game_map.can_move(unit.location(), direction.SOUTH) == False:
                    direction = directions.west()
                    if self.game_map.can_move(unit.location(), direction.WEST) == False:
                        direction = directions.north()
                        if self.game_map.can_move(unit.location(), direction.NORTH) == False:
                            direction = directions.east()

        elif cords.x < 0:
            direction = directions.west()
            if self.game_map.can_move(unit.location(), direction.WEST) == False:
                direction = directions.north()
                if self.game_map.can_move(unit.location(), direction.NORTH) == False:
                    direction = directions.east()
                    if self.game_map.can_move(unit.location(), direction.EAST) == False:
                        direction = directions.south()
                        if self.game_map.can_move(unit.location(), direction.SOUTH) == False:
                            direction = directions.west()


               
        return build_move_command(unit, direction)

        