"""
This is python homework for classes
"""

class Vehicle:

    def __init__(self, Make, Model, Year, Weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    # setter

    def setMake(self, Make):
        self.Make = Make

    def setModel(self, Model):
        self.Model = Model

    def setYear(self, Year):
        self.Year = Year

    def setWeight(self, Weight):
        self.Weight = Weight

        # getters

    def getMake(self):
        return self.Make

    def getModel(self):
        return self.Model

    def getYear(self):
        return self.Year

    def getWeight(self):
        return self.Weight

    def repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

# Checking for class inheritance functions

class Cars(Vehicle):
    def __init__(self,Make,Model,Year,Weight, isDriving = True):
        Vehicle.__init__(self,Make,Model,Year,Weight)
        self.isDriving = isDriving

    def drive(self):
        self.isDriving = True

    def stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance += 1

            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isDriving = False


# define plane class - inherited from vehicle class

class Plane(Vehicle):
    def __init__(self, make, model, year, weight, isFlying=False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = isFlying

    def flying(self):
        if self.needsMaintenance == True:
            return False
        self.isFlying = True
        return True

    def landing(self):
        if self.isFlying:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isFlying = False


# helpers functions

# drive and stop car random no of times
def randomly_drive_car(car):
    drive_times = random.randint(1, 101)
    for i in range(drive_times):
        car.drive()
        car.stop()


# fly and land plane random no of times
def randomly_fly_plane(plane, fly_times=None):
    fly_times = random.randint(1, 101) if fly_times is None else fly_times
    for i in range(fly_times):
        is_flying = plane.flying()
        if is_flying:
            plane.landing()
        else:
            print("plane " + plane.model + " can't fly until it's repair", 'red', attrs=['bold'])
            print("Repairing... " + plane.model, 'red_White')
            plane.repair()

CarA = Cars("Toyota", "Camry_2017", 2019, "4000Kg")
CarB = Cars("Lexus", "Rx_450", 2018, "3500kg")
CarC = Cars("Mecediz", "GL_450", 2018, "5000KG")

Plane1 = Plane("Aeronica", "15 AC Sedan",1992, 2050)

print(CarA.Make)
print(CarA.Model)
print(CarA.Year)
print(CarA.Weight)
print(CarB.Weight)
print(Plane1.Make)
print(Plane1.Model)

