from abc import ABC, abstractmethod
class StackInterface(ABC):
    @abstractmethod
    def push(s, d):
        pass
    @abstractmethod
    def pop(s):
        pass
    @abstractmethod
    def peek(s):
        pass
    @abstractmethod
    def is_empty(s):
        pass
