# 24) Write a Python class named Circle constructed by a radius and two 
#     methods which will compute the area and the perimeter of a circle

class circle:

    pi=3.142

    def __init__(self,radius):
            self.redius= radius

    def area(self):
          return(circle.pi * self.redius * self.redius)
    
    def pc(self):
          return(2 * circle.pi * self.redius)
    
c=circle(int(input("Enter Number :-")))
print("Area Of Circle is:-",c.area())
print("Parameter Of Circle is :-",c.pc())
        