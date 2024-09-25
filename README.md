# Alife: A Python Library for Artificial Life Simulations

[![Build Status](https://img.shields.io/travis/tomato414941/alife/master.svg)](https://travis-ci.org/tomato414941/alife)
[![Coverage Status](https://img.shields.io/codecov/c/github/tomato414941/alife/master.svg)](https://codecov.io/github/tomato414941/alife)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/alife.svg)](https://pypi.org/project/alife/)

Alife is a flexible and extensible Python library designed for creating and studying artificial life simulations. It provides a set of tools and abstractions to model various artificial life phenomena, from simple cellular automata to complex evolutionary systems.

## Features

- Modular design for easy extension and customization
- Implementation of fundamental Alife concepts (Entity, Environment, Simulation)
- Ready-to-use models, including Conway's Game of Life and Langton's Ant
- Utilities for visualization and analysis

## Requirements

- Python 3.7+
- NumPy
- Matplotlib (for visualization)
- pytest

## Installation

You can install Alife using pip:

```bash
pip install alife
```

Or clone the repository and install it locally:

```bash
git clone https://github.com/tomato414941/alife.git
cd alife
pip install -e .
```

For development, we recommend setting up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Quick Start

Here's a simple example of how to use the Game of Life model:

```python
from alife.models.discrete_systems.cellular_automata.game_of_life import GameOfLifeSimulation

# Create a Game of Life simulation
sim = GameOfLifeSimulation(width=50, height=50)

# Initialize the simulation
sim.initialize()

# Run the simulation for 100 steps
for _ in range(100):
    sim.run_step()
    state = sim.get_state()
    # Process or visualize the state as needed
```

For more detailed examples, check out the `examples/` directory.

## Project Structure

```
alife/
├── LICENSE
├── README.md
├── setup.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── docs/
│   ├── conf.py
│   ├── index.rst
│   ├── quickstart.md
│   ├── api/
│   │   └── index.rst
│   └── examples/
│       └── game_of_life.md
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_resources.py
│   ├── test_environments.py
│   ├── test_grid_environment.py
│   ├── test_organisms.py
│   ├── test_game_of_life.py
│   └── test_langtons_ant.py
├── examples/
│   ├── grid_based_alife.py
│   ├── game_of_life_example.py
│   ├── langtons_ant_example.py
│   └── simple_web_alife.py
├── alife/
│   ├── __init__.py
│   ├── core.py
│   ├── resources/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── computational.py
│   ├── environments/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── grid.py
│   │   └── web.py
│   ├── organisms/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── web_organism.py
│   ├── models/
│   │   └── discrete_systems/
│   │       ├── __init__.py
│   │       ├── langtons_ant.py
│   │       └── cellular_automata/
│   │           ├── __init__.py
│   │           └── game_of_life.py
│   └── utils/
│       ├── __init__.py
│       └── visualization.py
```

## Documentation

For full documentation, please visit [Read the Docs](https://alife.readthedocs.io/).

## Running Tests

To run the tests, execute the following command from the project root:

```bash
pytest tests/
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please open an issue on GitHub.