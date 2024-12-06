from abc import ABC,abstractmethod
class PC(ABC):
    def __init__(self):
        print("PC is initialized")
    @staticmethod
    def loadOs():
        print("Loading OS")

    def start_mouse(self):
        print("starting the mouse")

    def useheadphone(self):
        print("Using the headphones")

class MotherBoard(PC):
    @abstractmethod
    def start_motherboard(self):
        pass

class Ram(PC):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(PC):
    @abstractmethod
    def start_processor(self):
        pass

class storage(PC):
    @abstractmethod
    def store_data(self):
        pass
pc=PC()
pc.start_mouse()
pc.useheadphone()
PC.loadOs()