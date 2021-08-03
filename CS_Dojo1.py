class Robot:                                           

    #def __init__(self, givenName, givenColor, givenWeight):            # this is a custom "constructor", what is the difference between this and a function?    note that there are default constructor
    #                                                                   givenName, givenColor, givenWeight is an "argument"
    #                                                                   its good practice to name the areguments the same as the attribute that we want to set
    #    self.name = givenName                              
    #    self.color = givenColor
    #    self.weight = givenWeight

    def __init__(self, name , color, weight):                   # this is made so that when we make an object(like r1,r2) there's less chance of error(when typing)(note that this is more effective)
        self.name = name
        self.color = color
        self.weight = weight


    def introduce_self(self):                           # this is a function
        print("My name is " + self.name)


#r1 = Robot()                # r1, r2 is an object / variable
#r1.name = "Tom"             #name, color, weight are called the "attribute" or the "instance variable"
#r1.color = "red"
#r1.weight = 30

#r2 = Robot()                # creating a new Robot "object"
#r2.name = "Jerry"
#r2.color = "blue"
#r2.weight = 40

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)



r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()    # becames  r2.introduce_self()