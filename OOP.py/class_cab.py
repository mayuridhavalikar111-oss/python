from abc import ABC, abstractmethod
class CabRide(ABC):
    @abstractmethod
    def fare(self):
        pass
class MiniCab(CabRide):
    def fare(self):
        print("Mini Cab Fare:", 10 * 5)
class LuxuryCab(CabRide):
    def fare(self):
        print("Luxury Cab Fare:", 10 * 15)
m = MiniCab()
l = LuxuryCab()
m.fare()
l.fare()
