from alife.core import Resource


class ComputationalResource(Resource):
    def __init__(self, initial_level: float):
        self._level = initial_level

    def consume(self, amount: float) -> None:
        self._level -= amount
        if self._level < 0:
            self._level = 0

    def produce(self, amount: float) -> None:
        self._level += amount

    def get_level(self) -> float:
        return self._level
