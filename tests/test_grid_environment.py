# tests/test_game_of_life.py

import pytest

from alife.core import Entity
from alife.environments.grid import GridEnvironment


class DummyEntity(Entity):
    def interact(self, environment):
        pass


def test_grid_environment_initialization():
    env = GridEnvironment(10, 10)
    assert env.width == 10
    assert env.height == 10
    assert len(env.grid) == 10
    assert len(env.grid[0]) == 10
    assert len(env.entities) == 0


def test_add_and_remove_entity():
    env = GridEnvironment(5, 5)
    entity = DummyEntity()

    env.add_entity(entity, 2, 3)
    assert env.grid[3][2] == entity
    assert entity in env.entities

    env.remove_entity(entity)
    assert env.grid[3][2] is None
    assert entity not in env.entities


def test_move_entity():
    env = GridEnvironment(5, 5)
    entity = DummyEntity()

    env.add_entity(entity, 2, 2)
    result = env.interact(entity, "move", x=1, y=1)

    assert result["success"] is True
    assert result["new_position"] == (3, 3)
    assert env.grid[3][3] == entity
    assert env.grid[2][2] is None


def test_get_neighbors():
    env = GridEnvironment(5, 5)
    entity1 = DummyEntity()
    entity2 = DummyEntity()

    env.add_entity(entity1, 1, 1)
    env.add_entity(entity2, 2, 2)

    result = env.interact(entity1, "get_neighbors", x=1, y=1)
    neighbors = result["neighbors"]

    assert len(neighbors) == 8
    assert neighbors[7] == entity2  # entity2 is at the bottom-right of entity1


def test_wrap_around():
    env = GridEnvironment(5, 5)
    entity = DummyEntity()

    env.add_entity(entity, 4, 4)
    result = env.interact(entity, "move", x=1, y=1)

    assert result["success"] is True
    assert result["new_position"] == (0, 0)
    assert env.grid[0][0] == entity
    assert env.grid[4][4] is None


if __name__ == "__main__":
    pytest.main()
