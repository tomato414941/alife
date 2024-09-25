from typing import Any, Dict, List

import numpy as np

from alife.core import Environment, Simulation


class LangtonAnt:
    def __init__(self, x: int, y: int, direction: int = 0):
        self.x = x
        self.y = y
        self.direction = direction  # 0: Up, 1: Right, 2: Down, 3: Left

    def move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        else:
            self.x -= 1

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4


class LangtonAntEnvironment(Environment):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=bool)
        self.ant = LangtonAnt(width // 2, height // 2)

    def get_state(self) -> Dict[str, Any]:
        return {
            "grid": self.grid.copy(),
            "ant": (self.ant.x, self.ant.y, self.ant.direction),
        }

    def update(self) -> None:
        x, y = self.ant.x, self.ant.y
        if self.grid[y, x]:
            self.grid[y, x] = False
            self.ant.turn_left()
        else:
            self.grid[y, x] = True
            self.ant.turn_right()
        self.ant.move()
        self.ant.x %= self.width
        self.ant.y %= self.height

    def interact(self, entity: Any, action: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError(
            "LangtonAntEnvironment does not support entity interactions"
        )

    def add_entity(self, entity: Any) -> None:
        raise NotImplementedError(
            "LangtonAntEnvironment does not support adding entities"
        )

    def remove_entity(self, entity: Any) -> None:
        raise NotImplementedError(
            "LangtonAntEnvironment does not support removing entities"
        )

    def get_entities(self) -> List[Any]:
        return []


class LangtonAntSimulation(Simulation):
    def __init__(self, width: int, height: int):
        environment = LangtonAntEnvironment(width, height)
        super().__init__(environment)
        self.steps = 0

    def initialize(self) -> None:
        self.steps = 0

    def run_step(self) -> None:
        self.environment.update()
        self.steps += 1

    def is_complete(self) -> bool:
        return False  # The simulation runs indefinitely

    def get_state(self) -> Dict[str, Any]:
        env_state = self.environment.get_state()
        return {"steps": self.steps, "grid": env_state["grid"], "ant": env_state["ant"]}

    def reset(self) -> None:
        self.initialize()
        self.environment = LangtonAntEnvironment(
            self.environment.width, self.environment.height
        )
