class Rectangle:
    """ Docstring to describe the class"""
    def __init__(self):
        self.length=0.0
        self.breadth=0.0
    #setter and getter length
    def getLength(self):
        return self.length
    def setLength(self,len1):
        self.length=len1
    #setter and getter breadth
    def getBreadth(self):
        return self.breadth
    def setBreadth(self,brd):
        self.breadth=brd
    def areaRectangle(self):
        area=self.length*self.breadth
        return area
        #return self.length*self.breadth
#Instance object named RedRectangle which is instance of the class Rectangle
RedRectangle=Rectangle()
RedRectangle.setBreadth(3.0)
RedRectangle.setLength(4)
print(RedRectangle.getBreadth())
RedBreadth=RedRectangle.getBreadth()
print("The breadth of the red rectangle is",RedBreadth)