from math import *
import matplotlib.pyplot as plt



class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

class Vector:
    def __init__(self, x , y):
        self.values = (x,y)

    def magnitude(self):
        #magnitude of the vector
        (x,y)= self.values
        return math.sqrt(x*x + y*y)

    def rotate(self, theta):
        #rotate the vector theta degrees
        theta = math.radians(theta)
        dc, ds = math.cos(theta), math.sin(theta)
        (x, y) = self.values
        (x, y) = dc*x - ds*y, ds*x + dc*y
        return Vector(x, y)

point = Point(0,0)
point1 = Point(0,0)



class truck:

    def __init__(self):
        self.header_length = 23.0;
        self.trailer_length = 48.5;

        self.hl_front = 9.0
        self.tl_back = 14.0

        self.header_width = 18;
        self.trailer_width = 18;

    def calculateCorners(self, pointFront, th1, th2):

        point = self.back_middle_trailer(pointFront, th1, th2)

        # hitch joint
        x2 = point.x + (self.trailer_length + self.tl_back) *cos(th2);
        y2 = point.y + (self.trailer_length + self.tl_back) *sin(th2);

        #print x2, y2


        #left back
        x4 = point.x - cos(pi/2-th2)*self.trailer_width/2;
        y4 = point.y + sin(pi/2-th2)*self.trailer_width/2;

        #right back
        x5 = point.x + cos(pi/2-th2)*self.trailer_width/2;
        y5 = point.y - sin(pi/2-th2)*self.trailer_width/2;


        #left back axis
        x12 = x4 + self.tl_back * cos(th2)
        y12 = y4 + self.tl_back * sin(th2)

        #right back axis
        x13 = x5 + self.tl_back * cos(th2)
        y13 = y5 + self.tl_back * sin(th2)



        #left joint wheel
        x6 = x2 - cos(pi/2-th1)*self.header_width/2;
        y6 = y2 + sin(pi/2-th1)*self.header_width/2;

        #right joint wheel
        x7 = x2 + cos(pi/2-th1)*self.header_width/2;
        y7 = y2 - sin(pi/2-th1)*self.header_width/2;

        #left front axis
        x8 = x6 + self.header_length*cos(th1);
        y8 = y6 + self.header_length*sin(th1);

        #right front axis
        x9 = x7 + self.header_length*cos(th1);
        y9 = y7 + self.header_length*sin(th1);


        #left front

        x10 = x6 + (self.header_length + self.hl_front)*cos(th1);
        y10 = y6 + (self.header_length + self.hl_front)*sin(th1);

        #right front

        x11 = x7 + (self.header_length + self.hl_front)*cos(th1);
        y11 = y7 + (self.header_length + self.hl_front)*sin(th1);



        return((x8,y8), (x9,y9), (x6,y6), (x7,y7), (x12, y12), (x13, y13), (x10, y10), (x11, y11), (x4, y4), (x5, y5))

    def rightbackWheel(self):

        point = self.back_middle_trailer()

        x5 = point.x + cos(pi/2-th2)*self.trailer_width/2;
        y5 = point.y - sin(pi/2-th2)*self.trailer_width/2;

    def back_middle_trailer(self, pointFront, th1, th2):
        jpx = pointFront.x - cos(th1) * self.header_length
        jpy = pointFront.y - sin(th1) * self.header_length

        px = jpx - cos(th2) * (self.trailer_length + self.tl_back)
        py = jpy - sin(th2) * (self.trailer_length + self.tl_back)
        return Point(px,py)


#if __name__ == '__main__':
#    truck = truck()
#    lista1 =truck.calculateCorners(Point(0,0),1.57, 1.57)
#
#    plt.plot([point.x],[point.y], 'bo')
#    plt.plot([point1.x],[point1.y], 'go')
#
#    lista2 =truck.calculateCorners(Point(0,0),1.57, 0.785398)
#
#    print lista1
#
#    lx= []
#    ly=[]

#    for (x,y) in lista1:
#        lx.append(x)
#        ly.append(y)

#    plt.plot(lx, ly, 'go')


#    lx2= []
#    ly2=[]

#    for (x,y) in lista2:
#        lx2.append(x)
#        ly2.append(y)

#    plt.plot(lx, ly, 'go')
#    plt.plot(lx2, ly2, 'ro')
#    plt.plot([0],[0], 'bo')
#    plt.plot([point.x],[point.y], 'bo')
#    plt.plot([point1.x],[point1.y], 'go')
#
#    plt.axis([-100, 150, 150, -100])
#    plt.show()









#
