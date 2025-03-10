from abc import ABC, abstractmethod

class LinkedListInterface(ABC):
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def search(self, data):
        pass
