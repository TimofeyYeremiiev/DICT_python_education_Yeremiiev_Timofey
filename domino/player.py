"""Player - abstraction for player"""
from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract player"""

    def __init__(self, player_name: str, caller):
        self.game = caller
        self.name = player_name

    @abstractmethod
    def is_ready(self) -> bool:
        """Player must return TRUE to next game iteration
            Returns:
                bool: - ready or not
        """

    @abstractmethod
    def make_step(self):
        """Player must make step
        """
