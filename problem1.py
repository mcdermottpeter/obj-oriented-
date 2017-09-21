class Point:
    '''The constructor sets the values of the x and y coordinates of the point. The default values for the point is (0,0)'''
    def __init__(self, x = 0, y = 0):
        self.y = y
        self.x = x

    def translate(self, s, t):
        '''Translates the point by (s, t). The instance is modified after this method is called'''
        return (self.x+s, self.y+t)

    def rotate(self, degree):
        '''Rotates the point by an angle Î¸. The instance is modified after this method is called.'''
        import math
        degree = math.radians(degree) 
        return(self.x * math.cos(degree) - self.y * math.sin(degree), self.x * math.sin(degree) - self.y * math.cos(degree))

    def distance(self, p):
        '''Returns the distance between the point and another point p. Hence this method has one parameter, namely a point p'''
        return (((self.x - p.x)**2) + ((self.y - p.y)**2)) **.5

    def left_of(self, q, r):
        '''This method has two parameters q and r. It returns True if the point lies to the left of qr, and False otherwise'''
        if ((r.x*self.y - self.x*r.y) + (q.x*r.y - q.x*self.y) + (q.y*self.x - q.y*r.x)) > 0:
            return True
        return False

    def right_of(self, q, r):
        '''It returns True if the point lies to the right of qr, and False otherwise'''
        if ((r.x*self.y - self.x*r.y) + (q.x*r.y - q.x*self.y) + (q.y*self.x - q.y*r.x)) < 0:
            return True
        return False

    def __str__(self):
        '''Returns a string representation of the point. The usual notation to
represent a point as its x and y coordinates surrounded by parentheses'''
        return ("(" + str(self.x) + "," + " " + str(self.y) + ")")
    
    def __repr__(self):
        '''Returns a string representation of the point'''
        return str(self)
        
class SimplePoly:
    def __init__(self, *vertices):
        '''The constructor takes an arbitrary number of points as parameters, where the points are listed in counter-clockwise order about the boundary. The parameter to the constructor should be of the form *vertices'''
        self.vertices = list(vertices)
        self.__count = 0
        self.__length = len(self.vertices)

    def translate(self,s,t):
        '''Translates the simple polygon by (s, t). This is equivalent to translating every vertex of the polygon by (s,t)'''
        for i in self.vertices:
            i.translate(s,t)

    def rotate(self,degree):
        '''Rotates the simple polygon by angle Î¸. This is equivalent to rotating every vertex of the polygon by Î¸'''
        import math
        degree = math.radians(degree)
        for i in self.vertices:
            i.rotate(degree)
            
    def __iter__(self):
        '''Return an iterator object'''
        return self

    def __next__(self):
        '''Return the next vertex from the simple polygon. If there are no further vertices, raise the StopIteration exception'''
        if self.__count > self.__length - 1:
            raise StopIteration
        else:
            answer = self.vertices[self.__count]
            self.__count += 1
        return answer                  

    def __len__(self):
        '''This method allows us to use the built-in function len with simple polygon instances (just as str allows us to use the built-in function str). It returns the number of vertices in the polygon'''
        count = 0
        for i in self.vertices:
            count += 1
        return count

    def __getitem__(self, index):
        '''Overload the index operator. If the parameters of this method are self and i, it returns the i-th vertex of the convex polygon. If the index is out of range (less than zero or greater than or equal to the number of vertices of the polygon), raise the IndexError exception'''
        if index < 0 or index > len(self.vertices):
            raise IndexError
        return self.vertices[index - 1]

    def __str__(self):
        '''returns string of points counter clock-wise'''
        points = []
        for i in self.vertices:
            points.append(str(i))
        return ','.join(points)

    def __repr__(self):
        '''return string of vertices'''
        return str(self)
                   
    def perimeter(self):
        ''' Return the perimeter of the polygon'''
        distance = 0
        for i in range(len(self.vertices) - 1):
            distance += self.vertices[i].distance(self.vertices[i +1])

        return distance + self.vertices[0].distance(self.vertices[-1])

class ConvPoly(SimplePoly):
    def __init__(self, *vertices):

        '''check that the vertices indeed form a convex polygon. If they do not, raise an exception.'''
        for i in range(len(vertices)-2):
            
            if vertices[i].right_of(vertices[i+1],vertices[i+2]) == True:
                raise Exception("Not a polygon")

        if ((vertices[-2].right_of(vertices[-1], vertices[0])) or (vertices[-1].right_of(vertices[0], vertices[1]))):
            raise Exception("Not a polygon")
                    
        SimplePoly.__init__(self,*vertices)
               
class EquiTriangle(ConvPoly):
    '''An equilateral triangle of that edge length, with one vertex at the origin is created.'''
    def __init__(self, length):
        self.length = length
        ConvPoly.__init__(self,Point(0,0),Point(self.length,0),Point(self.length/2,((self.length**2)-((self.length/2)**2))**.5))
        
    def area(self):
        '''area of equilateral triangle'''
        return ((3**.5)/4) * self.length**2 

class Rectangle(ConvPoly):
    '''The constructor takes two parameters (in addition to self), which are the length and width of the rectangle'''
    def __init__(self, length, width):
        self.length = length
        self.width = width
        ConvPoly.__init__(self,Point(0,0),Point(self.length,0),Point(self.length,self.width),Point(0, self.width))
        
    def area(self):
        '''area of rectangle'''
        return self.length * self.width

class Square(Rectangle):
    '''The constructor takes a single parameter (in addition to self), which is
the length of the square.'''
    def __init__(self, length):
        Rectangle.__init__(self, length, length)
                
        
        
    