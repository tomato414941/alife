import numpy as np
import pytest

from alife.models.discrete_systems.langtons_ant import (
    LangtonAnt,
    LangtonAntEnvironment,
    LangtonAntSimulation,
)


def test_langton_ant():
    """
    Test the basic functionality of the LangtonAnt class:
    - Correct initialization
    - Movement
    - Turning
    """
    ant = LangtonAnt(0, 0)
    assert ant.x == 0 and ant.y == 0 and ant.direction == 0

    ant.move()
    assert ant.x == 0 and ant.y == -1

    ant.turn_right()
    ant.move()
    assert ant.x == 1 and ant.y == -1 and ant.direction == 1


def test_langton_ant_environment():
    """
    Test the LangtonAntEnvironment class:
    - Correct initialization
    - Initial state
    - State update after one step
    """
    env = LangtonAntEnvironment(10, 10)
    assert env.width == 10 and env.height == 10
    assert env.ant.x == 5 and env.ant.y == 5

    initial_state = env.get_state()
    assert np.all(initial_state["grid"] == False)

    env.update()
    new_state = env.get_state()
    assert new_state["grid"][5, 5] == True
    assert new_state["ant"] != initial_state["ant"]


def test_langton_ant_simulation():
    """
    Test the LangtonAntSimulation class:
    - Correct initialization
    - State change after one step
    """
    sim = LangtonAntSimulation(10, 10)
    sim.initialize()
    assert sim.steps == 0

    initial_state = sim.get_state()
    sim.run_step()
    new_state = sim.get_state()

    assert sim.steps == 1
    assert np.any(new_state["grid"] != initial_state["grid"])
    assert new_state["ant"] != initial_state["ant"]


def test_langton_ant_simulation_reset():
    """
    Test the reset functionality of LangtonAntSimulation:
    - Run for several steps
    - Reset
    - Check if the state is back to initial
    """
    sim = LangtonAntSimulation(10, 10)
    sim.initialize()

    for _ in range(10):
        sim.run_step()

    assert sim.steps == 10

    sim.reset()
    assert sim.steps == 0
    assert np.all(sim.get_state()["grid"] == False)


def test_langton_ant_simulation_black_cells_increase():
    """
    Test the long-term behavior of Langton's Ant:
    - Run for 1000 steps
    - Check if the number of black cells generally increases
    - Verify that the increase is not strictly monotonic but shows an overall upward trend
    """
    sim = LangtonAntSimulation(50, 50)
    sim.initialize()

    initial_black_cells = np.sum(sim.get_state()["grid"])
    assert initial_black_cells == 0  # No black cells in the initial state

    black_cells_count = []
    for _ in range(1000):  # Run for 1000 steps
        sim.run_step()
        current_black_cells = np.sum(sim.get_state()["grid"])
        black_cells_count.append(current_black_cells)

    # Check if the number of black cells has increased
    assert black_cells_count[-1] > initial_black_cells
    assert black_cells_count[-1] > black_cells_count[0]

    # Check if there's an overall increasing trend, even if not strictly monotonic
    chunks = np.array_split(black_cells_count, 10)
    chunk_means = [chunk.mean() for chunk in chunks]
    assert chunk_means[-1] > chunk_means[0]


def test_langton_ant_simulation_long_run():
    """
    Test the long-term behavior of Langton's Ant over an extended period:
    - Run the simulation for 10,000 steps on a 100x100 grid
    - Verify that the number of black cells increases over time
    - Check if the final number of black cells exceeds a predefined threshold

    This test ensures that the Langton's Ant simulation exhibits the expected
    long-term behavior of creating more black cells and potentially forming
    complex patterns over an extended number of steps.
    """
    sim = LangtonAntSimulation(100, 100)
    sim.initialize()

    initial_black_cells = np.sum(sim.get_state()["grid"])

    for _ in range(10000):  # Run for 10,000 steps
        sim.run_step()

    final_black_cells = np.sum(sim.get_state()["grid"])

    # Verify that the number of black cells has increased
    assert (
        final_black_cells > initial_black_cells
    ), "The number of black cells should increase over time"

    # Check if the final number of black cells exceeds a threshold
    # Note: The threshold of 500 is based on observed behavior and may need adjustment
    assert (
        final_black_cells > 500
    ), f"Expected more than 500 black cells after 10,000 steps, but got {final_black_cells}"

    print(f"Final number of black cells: {final_black_cells}")


if __name__ == "__main__":
    pytest.main()
