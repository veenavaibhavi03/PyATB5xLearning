from abc import ABC,abstractmethod

class Gearbox(ABC):
    @abstractmethod
    def set_gear(self):
        pass

class Engine(Gearbox):
    @abstractmethod
    def start(self):
        super().set_gear()
        pass

    def set_gear(self):
        pass

    def stop(self):
        pass

class car(Engine):
    def start(self):
        print("Engine is starting")

    def set_gear(self):
        print("Gear is started")

    def stop(self):
        print("Engine is stopped")

    def drive(self):
        self.start()
        self.set_gear()
        self.stop()


car_obj=car()
car_obj.drive()