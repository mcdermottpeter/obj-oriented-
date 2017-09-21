A polygon is a closed loop made up of straight line seg- ments. 
When the loop does not intersect itself, the polygon is said to be a simple polygon. 
We can think of a simple polygon as a sequence of vertices specified in counter-clockwise order. 
Each vertex is a point with an (x,y) coordinate. 
For example, the simple polygon Q = {v0, v1, v2, v3, v4, v5, v6} in Figure 1(a) has 7 vertices and 7 edges.

A convex polygon is a simple polygon whose shape satisfies the property that as we walk around the boundary of the polygon in counter-clockwise order, we always turn left at each
vertex. (Another way to define a convex polygon is that for any two points on or within the polygon, the straight line segment connecting those points lies entirely within the polygon.)
See Figure 1(b) for an example of a convex polygon P = {v0,v1,v2,v3,v4,v5,v6,v7} with 8 vertices.
In this problem, you are asked to implement a Point class, a SimplePoly class, a ConvPoly class, an EquiTriangle class, a Rectangle class, and a Square class. 
Instances of the SimplePoly class contain a collection of Point instances. 
The ConvPoly class is a sub- class of SimplePoly, the EquiTriangle and Rectangle classes are sub-classes of ConvPoly, and the Square class is a sub-class of Rectangle.
Create a module called problem1.py to contain all these classes.

Instances of this class are points in two-dimensional space. Hence, each instance has an x coordinate and a y coordinate. 
We first state a few definitions. See Figure 2 for illustrations.
• Translation: If a point (x, y) is translated (moved) by an amount s in the x direction and an amount t in the y direction, its new coordinates are (x + s, y + t).
• Rotation: If a point (x, y) is rotated by angle θ about the origin, its new coordinates are (xcosθ−ysinθ,xsinθ+ycosθ).
• Distance: The distance between two points (x1, y1) and (x2, y2) is  (x1 − x2)2 + (y1 − y2)2.
say that p lies to the left of qr (that is, the points < q,r,p > make a left turn) if
and only if (rxpy −pxry)+(qxry −qxpy)+(qypx −qyrx) > 0. We say that p lies →
to the right of qr (that is, the points < q,r,p > make a right turn) if and only if (rxpy−pxry)+(qxry−qxpy)+(qypx−qyrx)<0. 
Finally,p,q,andrarecollinear(all lie on a straight line) if and only if (rxpy −pxry)+(qxry −qxpy)+(qypx −qyrx) = 0.

