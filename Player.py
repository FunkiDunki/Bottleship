from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(size: int):
        pass

    @abstractmethod
    def PlaceShips(sizes: list[int]):
        pass

    @abstractmethod
    def MakePlay():
        pass

    @abstractmethod
    def OpponentPlay(play: tuple[int, int]):
        pass

    @abstractmethod
    def TurnFeedback(play: tuple[int, int], hit: bool, sink: bool):
        pass