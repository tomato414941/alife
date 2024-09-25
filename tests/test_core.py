import pytest

from alife.core import Entity, Environment, Organism, Resource, Simulation


# Mock classes for testing
class MockResource(Resource):
    def __init__(self, initial_amount: float = 0):
        self.amount = initial_amount

    def consume(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot consume negative amount")
        self.amount -= amount

    def produce(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot produce negative amount")
        self.amount += amount

    def get_level(self) -> float:
        return self.amount


class MockEntity(Entity):
    def interact(self, environment: "Environment") -> None:
        pass


class MockOrganism(Organism):
    def interact(self, environment: "Environment") -> None:
        pass

    def act(self, environment: "Environment") -> None:
        pass

    def reproduce(self):
        return None


class MockEnvironment(Environment):
    def __init__(self):
        self.entities = []

    def get_state(self):
        return {"entities": len(self.entities)}

    def update(self) -> None:
        pass

    def interact(self, entity: Entity, action: str, **kwargs):
        return {"action": action}

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        self.entities.remove(entity)

    def get_entities(self):
        return self.entities


class MockSimulation(Simulation):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        self.steps = 0

    def initialize(self) -> None:
        self.steps = 0

    def run_step(self) -> None:
        self.steps += 1

    def is_complete(self) -> bool:
        return self.steps >= 10

    def get_state(self):
        return {"steps": self.steps}

    def reset(self) -> None:
        self.steps = 0


# Tests
def test_resource():
    resource = MockResource(100)
    assert resource.get_level() == 100

    resource.consume(30)
    assert resource.get_level() == 70

    resource.produce(20)
    assert resource.get_level() == 90

    with pytest.raises(ValueError):
        resource.consume(-10)

    with pytest.raises(ValueError):
        resource.produce(-10)


def test_entity():
    entity = MockEntity()
    resource = MockResource(100)
    entity.add_resource("energy", resource)
    assert "energy" in entity.resources
    assert entity.resources["energy"].get_level() == 100


def test_organism():
    organism = MockOrganism()
    resource = MockResource(100)
    organism.add_resource("energy", resource)
    assert organism.is_alive()

    organism.resources["energy"].consume(100)
    assert not organism.is_alive()


def test_environment():
    env = MockEnvironment()
    entity1 = MockEntity()
    entity2 = MockEntity()

    env.add_entity(entity1)
    env.add_entity(entity2)
    assert len(env.get_entities()) == 2

    env.remove_entity(entity1)
    assert len(env.get_entities()) == 1

    result = env.interact(entity2, "test_action")
    assert result["action"] == "test_action"


def test_simulation():
    env = MockEnvironment()
    sim = MockSimulation(env)

    sim.initialize()
    assert sim.get_state()["steps"] == 0

    sim.run_step()
    assert sim.get_state()["steps"] == 1

    sim.run()
    assert sim.get_state()["steps"] == 10
    assert sim.is_complete()

    sim.reset()
    assert sim.get_state()["steps"] == 0


if __name__ == "__main__":
    pytest.main()
