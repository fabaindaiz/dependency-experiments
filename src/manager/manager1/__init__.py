from abc import ABC, abstractmethod

class Manager1(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def work(self):
        pass