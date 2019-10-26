from directions import random_direction,north
from communication import build_move_command


class ExploreStrategy:
    def __init__(self, game_map, unit, unit_manager):
        self.game_map = game_map
        self.unit = unit
        self.unit_manager = unit_manager


    def build_command(self, unit):
        direction = north()
        return build_move_command(unit, direction)