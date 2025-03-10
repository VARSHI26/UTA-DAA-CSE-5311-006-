from abc import ABC, abstractmethod
class LinkedListInterface(ABC):
    @abstractmethod
    def insert(s, d):
        pass
    @abstractmethod
    def delete(s, d):
        pass
    @abstractmethod
    def display(s):
        pass
    @abstractmethod
    def search(s, d):
        pass
