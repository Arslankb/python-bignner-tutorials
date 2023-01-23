#Class

# class person:
#
#     def __init__(self):
#         self.name = "Arslan"
#         self.gender = "Male"
#         self.age = 22
#
#     def talk(self):
#         print("Hi I'm ", self.name)
#
#     def vote(self):
#         if self.age<18:
#             print("I am not eligible to vote.")
#         else:
#             print("I am eligible to vote.")
# obj = person()
# obj.talk()
# obj.vote()



#Another Way if two or more object


# class person:
#
#     def __init__(self, n, g, a):
#         self.name = n
#         self.gender = g
#         self.age = a
#
#     def talk(self):
#         print("Hi I'm ", self.name)
#
#     def vote(self):
#         if self.age<18:
#             print("I am not eligible to vote.")
#         else:
#             print("I am eligible to vote.")
# obj1 = person("Arslan", "Male", 22)
# obj2 = person("Ayesha", "Female", 22)
# obj1.talk()
# obj1.vote()
#
# obj2.talk()
# obj2.vote()



#Car Example...


class car:
    def __init__(self, year, speed):
        self.year = year
        self.speed= speed

    def getSpeed(self):
        print("Maximum Speed is: ", self.speed)

    def setSpeed(self, speed):
        self.speed = speed

BMW = car(2018, 145)


BMW.getSpeed()
BMW.setSpeed(123)
BMW.getSpeed()


#INHERITANCE....


class car:
    def __init__(self, year, speed):
        self.year = year
        self.speed= speed

    def getSpeed(self):
        print("Maximum Speed is: ", self.speed)

    def setSpeed(self, speed):
        self.speed = speed

BMW = car(2018, 145)




class Sedan(car):       #Child Class
    def accelerate(self):
        print("133 mph")
    def openTrunk(self):
        print("trunk has been opened")

class SUV(car):        #Child Class
    def accelerate(self):
        print("180 mph")

Honda = Sedan(2018, 150)
BMW.getSpeed()
Honda.getSpeed()
