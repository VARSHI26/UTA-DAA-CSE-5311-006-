from abc import ABC, abstractmethod
class QueueInterface(ABC):
    @abstractmethod
    def enqueue(s, d):
        pass
    @abstractmethod
    def dequeue(s):
        pass
    @abstractmethod
    def peek(s):
        pass
    @abstractmethod
    def is_empty(s):
        pass
