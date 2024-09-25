# alife/models/cellular_automata/game_of_life.py

from typing import List, Tuple

from alife.core import Environment, Simulation


class GameOfLifeEnvironment(Environment):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]

    def get_state(self) -> List[List[bool]]:
        return self.grid

    def update(self) -> None:
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = self._count_live_neighbors(x, y)
                if self.grid[y][x]:
                    new_grid[y][x] = live_neighbors in [2, 3]
                else:
                    new_grid[y][x] = live_neighbors == 3
        self.grid = new_grid

    def _count_live_neighbors(self, x: int, y: int) -> int:
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = (x + dx) % self.width, (y + dy) % self.height
                if self.grid[ny][nx]:
                    count += 1
        return count

    def interact(self, entity, action: str, **kwargs) -> dict:
        # Not used in Game of Life
        pass

    def add_entity(self, entity) -> None:
        # Not used in Game of Life
        pass

    def remove_entity(self, entity) -> None:
        # Not used in Game of Life
        pass

    def get_entities(self) -> List:
        # Not used in Game of Life
        return []


class GameOfLifeSimulation(Simulation):
    def __init__(self, width: int, height: int):
        super().__init__(GameOfLifeEnvironment(width, height))
        self.generation = 0

    def initialize(self) -> None:
        # Initialize with a random pattern
        import random

        for y in range(self.environment.height):
            for x in range(self.environment.width):
                self.environment.grid[y][x] = random.random() < 0.2

    def run_step(self) -> None:
        self.environment.update()
        self.generation += 1

    def is_complete(self) -> bool:
        # Run for a fixed number of generations
        return self.generation >= 100

    def get_state(self) -> dict:
        return {"generation": self.generation, "grid": self.environment.get_state()}

    def reset(self) -> None:
        self.generation = 0
        self.initialize()
