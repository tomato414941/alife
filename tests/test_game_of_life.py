import numpy as np
import pytest

from alife.models.discrete_systems.cellular_automata.game_of_life import (
    GameOfLifeEnvironment,
    GameOfLifeSimulation,
)


def test_environment_initialization():
    env = GameOfLifeEnvironment(10, 10)
    assert env.width == 10
    assert env.height == 10
    assert np.array(env.grid).shape == (10, 10)


def test_count_live_neighbors():
    env = GameOfLifeEnvironment(3, 3)
    env.grid = [[True, False, True], [False, True, False], [True, False, True]]
    assert env._count_live_neighbors(1, 1) == 4
    assert env._count_live_neighbors(0, 0) == 4
    assert env._count_live_neighbors(1, 0) == 5


def test_update_rules():
    env = GameOfLifeEnvironment(3, 3)
    env.grid = [[True, True, False], [True, True, False], [False, False, False]]
    env.update()
    expected_grid = [
        [True, True, False],
        [True, True, False],
        [False, False, False],
    ]
    assert env.grid == expected_grid


def test_simulation_initialization():
    sim = GameOfLifeSimulation(10, 10)
    sim.initialize()
    assert sim.generation == 0
    assert sim.environment is not None


def test_simulation_run():
    sim = GameOfLifeSimulation(10, 10)
    sim.initialize()
    initial_state = sim.get_state()
    sim.run_step()
    next_state = sim.get_state()
    assert next_state["generation"] == 1
    assert initial_state["grid"] != next_state["grid"]


def test_simulation_reset():
    sim = GameOfLifeSimulation(10, 10)
    sim.initialize()
    for _ in range(10):
        sim.run_step()
    assert sim.generation == 10
    sim.reset()
    assert sim.generation == 0


if __name__ == "__main__":
    pytest.main()
