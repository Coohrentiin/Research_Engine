
class Vehicle:
    def __init__(self,nb_seat,nb_wheel,hoursepower,weight,fuel):
        self.nb_seat=nb_seat
        self.nb_wheel=nb_wheel
        self.hoursepower=horsepower
        self.__weight=weight
        self.__fuel=fuel
    def getWheight(self):
        return self.__weight
    def getFuel(self):
        return self.__fuel
    
class Bicycle(Vehicle):
    def __str__(self):
        return("I'm bicycle, I have"+str(self.nb_wheel)+" my horsepower should be:"+str(self.horsepower)+" but it depand on my Rider mainly ;)")
    def ride(self):
        return("I ride my bicycle!")
    def GoodToKnow(self):
        return(" Bicycle is a famous song of Queen's !")

class Car(Vehicle):
    def __str__(self):
        return("I'm a car, I have"+str(self.nb_wheel)+ "my horsepower is:"+str(self.horsepower))
    def drive(self):
        return("Do not drive if you're drunk.")
    def park(self):
        return("Nop, I'm not an autonomus car yet!")  
            
class Avion(Vehicle):
    def __str__(self):
        return("I'm Avion, I have"+str(self.nb_wheel)+"but obviously, I'm not always on my wheels!  My horsepower is:"+str(self.horsepower)+" not bad isn't it ? ;)")
    def fly(self):
        return("I want to fly away!")
    def GoodToKnow(self):
        return(" Avion is a famous theme of the current ENSTA Student Union, called TangoAlpha !")