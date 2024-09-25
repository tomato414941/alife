# alife/resources/base.py

from typing import Union

from alife.core import Resource


class FiniteResource(Resource):
    """A resource with a finite amount that cannot go below zero."""

    def __init__(self, initial_amount: float = 0):
        self._amount = max(0, initial_amount)

    def consume(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot consume negative amount of resource.")
        if self._amount < amount:
            raise ValueError("Insufficient resource.")
        self._amount -= amount

    def produce(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot produce negative amount of resource.")
        self._amount += amount

    def get_level(self) -> float:
        return self._amount


class InfiniteResource(Resource):
    """A resource with an infinite amount."""

    def consume(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot consume negative amount of resource.")

    def produce(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot produce negative amount of resource.")

    def get_level(self) -> float:
        return float("inf")


class RegeneratingResource(FiniteResource):
    """A finite resource that regenerates over time."""

    def __init__(self, initial_amount: float = 0, regeneration_rate: float = 0):
        super().__init__(initial_amount)
        self.regeneration_rate = max(0, regeneration_rate)

    def regenerate(self) -> None:
        """Regenerate the resource based on its regeneration rate."""
        self.produce(self.regeneration_rate)


class ResourceContainer:
    """A container for multiple resources."""

    def __init__(self):
        self._resources = {}

    def add_resource(self, name: str, resource: Resource) -> None:
        """Add a resource to the container."""
        self._resources[name] = resource

    def get_resource(self, name: str) -> Union[Resource, None]:
        """Get a resource from the container by name."""
        return self._resources.get(name)

    def has_resource(self, name: str) -> bool:
        """Check if a resource exists in the container."""
        return name in self._resources

    def list_resources(self) -> list:
        """List all resource names in the container."""
        return list(self._resources.keys())
