import pytest

from alife.resources.base import (
    FiniteResource,
    InfiniteResource,
    RegeneratingResource,
    ResourceContainer,
)


def test_finite_resource():
    resource = FiniteResource(100)
    assert resource.get_level() == 100

    resource.consume(30)
    assert resource.get_level() == 70

    resource.produce(20)
    assert resource.get_level() == 90

    with pytest.raises(ValueError):
        resource.consume(100)

    with pytest.raises(ValueError):
        resource.consume(-10)

    with pytest.raises(ValueError):
        resource.produce(-10)


def test_infinite_resource():
    resource = InfiniteResource()
    assert resource.get_level() == float("inf")

    resource.consume(1000000)
    assert resource.get_level() == float("inf")

    resource.produce(1000000)
    assert resource.get_level() == float("inf")

    with pytest.raises(ValueError):
        resource.consume(-10)

    with pytest.raises(ValueError):
        resource.produce(-10)


def test_regenerating_resource():
    resource = RegeneratingResource(100, 10)
    assert resource.get_level() == 100

    resource.consume(30)
    assert resource.get_level() == 70

    resource.regenerate()
    assert resource.get_level() == 80

    resource.regenerate()
    assert resource.get_level() == 90


def test_resource_container():
    container = ResourceContainer()

    finite = FiniteResource(100)
    infinite = InfiniteResource()
    regenerating = RegeneratingResource(50, 5)

    container.add_resource("finite", finite)
    container.add_resource("infinite", infinite)
    container.add_resource("regenerating", regenerating)

    assert container.has_resource("finite")
    assert container.has_resource("infinite")
    assert container.has_resource("regenerating")
    assert not container.has_resource("nonexistent")

    assert container.get_resource("finite") == finite
    assert container.get_resource("infinite") == infinite
    assert container.get_resource("regenerating") == regenerating
    assert container.get_resource("nonexistent") is None

    assert set(container.list_resources()) == {"finite", "infinite", "regenerating"}


def test_resource_container_operations():
    container = ResourceContainer()
    container.add_resource("energy", FiniteResource(100))

    energy = container.get_resource("energy")
    energy.consume(30)
    assert energy.get_level() == 70

    energy.produce(20)
    assert energy.get_level() == 90


if __name__ == "__main__":
    pytest.main()
