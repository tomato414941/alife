import matplotlib.pyplot as plt
import numpy as np

from alife.models.discrete_systems.cellular_automata.game_of_life import (
    GameOfLifeSimulation,
)


def run_game_of_life():
    # Initialize the simulation
    width, height = 50, 50
    sim = GameOfLifeSimulation(width, height)
    sim.initialize()

    # Set up the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    im = ax1.imshow(sim.get_state()["grid"], cmap="binary", interpolation="nearest")
    ax1.set_title("Game of Life")
    ax1.axis("off")

    generations = []
    live_cells = []

    # Run the simulation
    for step in range(200):  # Increased to 200 steps for a longer simulation
        sim.run_step()
        state = sim.get_state()

        # Update the grid visualization
        im.set_array(state["grid"])
        ax1.set_title(f"Generation: {state['generation']}")

        # Count and record the number of live cells
        num_live_cells = np.sum(state["grid"])
        generations.append(state["generation"])
        live_cells.append(num_live_cells)

        # Update the plot of live cells
        ax2.clear()
        ax2.plot(generations, live_cells)
        ax2.set_title("Number of Live Cells")
        ax2.set_xlabel("Generation")
        ax2.set_ylabel("Live Cells")

        plt.tight_layout()
        plt.pause(0.1)  # Pause to create animation effect

        if step % 10 == 0:
            print(f"Generation {state['generation']}: {num_live_cells} live cells")

    plt.show()


if __name__ == "__main__":
    run_game_of_life()
