from abc import ABC, abstractmethod

class Figure(ABC):

    @classmethod
    @abstractmethod
    def get_figure_type(cls):
        pass

    @abstractmethod
    def area(self):
        pass
