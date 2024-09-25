from typing import Any, Dict, List, Tuple

from alife.core import Entity, Environment


class GridEnvironment(Environment):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: List[List[Entity]] = [
            [None for _ in range(width)] for _ in range(height)
        ]
        self.entities: List[Entity] = []

    def get_state(self) -> List[List[Any]]:
        return [
            [cell.__class__.__name__ if cell else None for cell in row]
            for row in self.grid
        ]

    def update(self) -> None:
        # In this simple implementation, the environment doesn't change on its own
        pass

    def interact(self, entity: Entity, action: str, **kwargs) -> Dict[str, Any]:
        if action == "move":
            return self._move_entity(entity, kwargs.get("x", 0), kwargs.get("y", 0))
        elif action == "get_neighbors":
            return self._get_neighbors(kwargs.get("x", 0), kwargs.get("y", 0))
        else:
            raise ValueError(f"Invalid action: {action}")

    def add_entity(self, entity: Entity, x: int, y: int) -> None:
        if self.grid[y][x] is not None:
            raise ValueError(f"Cell ({x}, {y}) is already occupied")
        self.grid[y][x] = entity
        self.entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        if entity not in self.entities:
            raise ValueError("Entity not found in the environment")
        self.entities.remove(entity)
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == entity:
                    self.grid[y][x] = None
                    return

    def get_entities(self) -> List[Entity]:
        return self.entities

    def _move_entity(self, entity: Entity, dx: int, dy: int) -> Dict[str, Any]:
        old_x, old_y = self._find_entity(entity)
        new_x, new_y = (old_x + dx) % self.width, (old_y + dy) % self.height

        if self.grid[new_y][new_x] is not None:
            return {"success": False, "message": "Target cell is occupied"}

        self.grid[old_y][old_x] = None
        self.grid[new_y][new_x] = entity
        return {"success": True, "new_position": (new_x, new_y)}

    def _get_neighbors(self, x: int, y: int) -> Dict[str, Any]:
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = (x + dx) % self.width, (y + dy) % self.height
                neighbors.append(self.grid[ny][nx])
        return {"neighbors": neighbors}

    def _find_entity(self, entity: Entity) -> Tuple[int, int]:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == entity:
                    return x, y
        raise ValueError("Entity not found in the grid")
