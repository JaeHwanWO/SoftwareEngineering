from abc import *


# 추상 클래스
class Publisher(metaclass=ABCMeta):
    @abstractmethod
    def subscribe(self):
        pass

    @abstractmethod
    def unsubscribe(self):
        pass


# 추상 클래스
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def receive(self):
        pass


# 추상 클래스
class Decorator(metaclass=ABCMeta):
    @abstractmethod
    def activate(self):
        pass