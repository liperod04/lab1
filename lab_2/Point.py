class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        """Compares x- and y- from two different Points"""
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def equidistant(self, other):
        """Compares if two points have the same distance from origin"""
        x1 = ((self.x**2 + self.y**2)**(1/2))
        x2 = ((other.x**2 + other.y**2)**(1/2))
        if x1 == x2:
            return True
        else:
            return False
        
    def within(self, distance, other):
        """Compares if two points are within a certain distance"""
        distance_between = ((other.x - self.x)**2 + (other.y - self.y)**2)**(1/2)
        if distance_between <= distance:
            return True
        else:
            return False
        

