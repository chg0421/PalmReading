from abc import ABCMeta, abstractmethod


class Palm(metaclass=ABCMeta):
    @abstractmethod
    def sort_line(self):
        pass

    @abstractmethod
    def straight_line(self):
        pass

    @abstractmethod
    def chain_line(self):
        pass

    @abstractmethod
    def hard_line(self):
        pass

