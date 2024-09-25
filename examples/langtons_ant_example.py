import matplotlib.pyplot as plt
import numpy as np

from alife.models.discrete_systems.langtons_ant import LangtonAntSimulation


def run_langtons_ant():
    sim = LangtonAntSimulation(100, 100)
    sim.initialize()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    im = ax1.imshow(
        sim.get_state()["grid"].astype(float),
        cmap="binary",
        interpolation="nearest",
        vmin=0,
        vmax=1,
    )
    ax1.set_title("Langton's Ant")
    ax1.axis("off")

    steps = []
    black_cells = []

    for step in range(11000):
        sim.run_step()
        if step % 100 == 0:
            state = sim.get_state()
            grid = state["grid"].astype(float)
            im.set_array(grid)
            ax1.set_title(f"Step: {state['steps']}")

            # Count and record the number of black cells
            num_black_cells = np.sum(grid)
            steps.append(step)
            black_cells.append(num_black_cells)

            # Update the plot of black cells
            ax2.clear()
            ax2.plot(steps, black_cells)
            ax2.set_title("Number of Black Cells")
            ax2.set_xlabel("Steps")
            ax2.set_ylabel("Black Cells")

            plt.tight_layout()
            plt.pause(0.01)

        if step % 1000 == 0:
            print(f"Step {step}: {np.sum(sim.get_state()['grid'])} black cells")

    plt.show()


if __name__ == "__main__":
    run_langtons_ant()
