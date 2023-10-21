#Without classes

# circle1ID = 1
# circle1radius = 8
# circle1color = "Blue"
# circle1display = True

# circle2ID = 2
# circle2radius = 10
# circle2color = "Green"
# circle1display = True

# circle3ID = 3
# circle3radius = 13
# circle3color = "Red"
# circle1display = False

# print("Circle 1 Circumfrence is " + (3.141 * 2 * circle1radius))
# print("Circle 2 Circumfrence is " + (3.141 * 2 * circle2radius))
# print("Circle 3 Circumfrence is " + (3.141 * 2 * circle3radius))


# #With Classes

class circle:
    ID = 0
    radius = 0
    color = ""
    display = True

    def __init__(self,id,r,c,d):
        self.id = id
        self.radius = r
        self.color = c 
        self.display = d 

    def circumfrence(self):
        return 3.141 * 2 * self.radius
    
circle1 = circle(1,8,"Blue",True)
circle2 = circle(2,10,"Green",True)
circle3 = circle(3,13,"Red",False)

print("Circle 1 circumfrence is " + circle1.circumfrence())

print("Circle 2 circumfrence is " + circle2.circumfrence())

print("Circle 3 circumfrence is " + circle3.circumfrence())


    