# alife/core.py

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class Resource(ABC):
    """
    Abstract base class representing a resource.

    This class defines the basic interface for resources such as energy or matter.
    Specific resource types should inherit from this class and implement its methods.
    """

    @abstractmethod
    def consume(self, amount: float) -> None:
        """
        Consume the specified amount of the resource.

        Args:
            amount (float): The amount of resource to consume.

        Raises:
            ValueError: If the amount is negative.
        """
        pass

    @abstractmethod
    def produce(self, amount: float) -> None:
        """
        Produce the specified amount of the resource.

        Args:
            amount (float): The amount of resource to produce.

        Raises:
            ValueError: If the amount is negative.
        """
        pass

    @abstractmethod
    def get_level(self) -> float:
        """
        Get the current level of the resource.

        Returns:
            float: The current level of the resource.
        """
        pass


class Entity(ABC):
    """
    Abstract base class representing an entity in the simulation.

    This class defines the basic properties and behaviors of any object
    that can exist in the environment. Specific entity types should
    inherit from this class and implement its methods.
    """

    def __init__(self):
        """
        Initialize an Entity object.
        """
        self.resources: Dict[str, Resource] = {}

    @abstractmethod
    def interact(self, environment: "Environment") -> None:
        """
        Define the interaction between the entity and the environment.

        This method should implement how the entity interacts with its environment.

        Args:
            environment (Environment): The environment object to interact with.
        """
        pass

    def add_resource(self, name: str, resource: Resource) -> None:
        """
        Add a resource to the entity.

        Args:
            name (str): The name of the resource.
            resource (Resource): The resource object to add.
        """
        self.resources[name] = resource


class Organism(Entity):
    """
    Abstract base class representing a living organism.

    This class extends Entity to include behaviors specific to living organisms,
    such as acting, reproducing, and the concept of being alive. Specific organism
    types should inherit from this class and implement its methods.
    """

    def is_alive(self) -> bool:
        """
        Check if the organism is alive.

        Returns:
            bool: True if all resource levels are above 0, False otherwise.
        """
        return all(resource.get_level() > 0 for resource in self.resources.values())

    @abstractmethod
    def act(self, environment: "Environment") -> None:
        """
        Define the organism's action.

        This method should implement how the organism acts in its environment.

        Args:
            environment (Environment): The environment in which the action is performed.
        """
        pass

    @abstractmethod
    def reproduce(self) -> Optional["Organism"]:
        """
        Define the organism's reproduction process.

        Returns:
            Optional[Organism]: A new organism if reproduction is successful, None otherwise.
        """
        pass


class Environment(ABC):
    """
    Abstract base class representing the simulation environment.

    This class defines the basic properties and behaviors of the environment
    in which entities exist and interact. Specific environment types should
    inherit from this class and implement its methods.
    """

    @abstractmethod
    def get_state(self) -> Any:
        """
        Get the current state of the environment.

        Returns:
            Any: The current state of the environment, represented by any appropriate data structure.
        """
        pass

    @abstractmethod
    def update(self) -> None:
        """
        Update the state of the environment.

        This method should implement changes in the environment over time.
        """
        pass

    @abstractmethod
    def interact(self, entity: Entity, action: str, **kwargs) -> Dict[str, Any]:
        """
        Handle the interaction between an entity and the environment.

        Args:
            entity (Entity): The entity performing the interaction.
            action (str): The type of action being performed.
            **kwargs: Additional parameters related to the action.

        Returns:
            Dict[str, Any]: A dictionary representing the result of the interaction.

        Raises:
            ValueError: If an invalid action is specified.
        """
        pass

    @abstractmethod
    def add_entity(self, entity: Entity) -> None:
        """
        Add an entity to the environment.

        Args:
            entity (Entity): The entity object to add.
        """
        pass

    @abstractmethod
    def remove_entity(self, entity: Entity) -> None:
        """
        Remove an entity from the environment.

        Args:
            entity (Entity): The entity object to remove.

        Raises:
            ValueError: If the specified entity does not exist in the environment.
        """
        pass

    @abstractmethod
    def get_entities(self) -> List[Entity]:
        """
        Get a list of all entities in the environment.

        Returns:
            List[Entity]: A list of all entities in the environment.
        """
        pass


class Simulation(ABC):
    """
    Abstract base class representing a simulation.

    This class defines the basic interface for managing the interaction between
    the environment and entities, and controlling the execution of the simulation.
    """

    def __init__(self, environment: Environment):
        """
        Initialize a Simulation object.

        Args:
            environment (Environment): The environment object in which the simulation will run.
        """
        self.environment = environment

    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize the simulation.

        This method should perform any necessary setup before the simulation starts.
        """
        pass

    @abstractmethod
    def run_step(self) -> None:
        """
        Run one step of the simulation.

        This method should implement all processes that occur in one simulation cycle.
        """
        pass

    @abstractmethod
    def is_complete(self) -> bool:
        """
        Check if the simulation is complete.

        Returns:
            bool: True if the simulation is complete, False otherwise.
        """
        pass

    @abstractmethod
    def get_state(self) -> Dict[str, Any]:
        """
        Get the current state of the simulation.

        Returns:
            Dict[str, Any]: A dictionary representing the current state of the simulation.
        """
        pass

    def run(self) -> None:
        """
        Run the simulation.

        This method repeatedly calls run_step() until the simulation is complete.
        """
        self.initialize()
        while not self.is_complete():
            self.run_step()

    @abstractmethod
    def reset(self) -> None:
        """
        Reset the simulation to its initial state.

        This method should return the simulation to its initial state, ready to be run again.
        """
        pass


# Note on potential future extension:
"""
In the future, if a need arises to distinguish between general living entities
and more specific organisms, a LivingEntity class could be introduced as an
intermediate abstraction between Entity and Organism. This could be useful for
representing entities that are considered "alive" but may not have all the
characteristics of a biological organism (e.g., AI agents, virtual life forms).

The hierarchy would then be:
Entity -> LivingEntity -> Organism

LivingEntity would include the is_alive method and potentially other methods
or properties common to all living entities but not necessarily to all organisms.
"""
