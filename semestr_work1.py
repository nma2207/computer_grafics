import Blender
from Blender import Draw, BGL
from Blender.BGL import *
import time
import math

x_circle=[]
y_circle=[]

def changeR():
	global R
	R+=1
	if R>1000:
		Draw.Exit()
	time.sleep(0.1)
	Draw.Redraw(1)
def circle_coords(R,center):
	global x_circle, y_circle
	del x_circle[0:]
	del y_circle[0:]
	n=100
	dx=2*R/n
	for i in range(n):
		x_circle.append(dx*i+center[0]-R)
		y_circle.append((R*R-(dx*i-R)**2)**0.5+center[1])
	for i in range(n):
		x_circle.append(R-dx*i+center[0])
		y_circle.append(-(R*R-(dx*i-R)**2)**0.5+center[1])


def event(evt, val):
	if evt == Draw.ESCKEY :
		Draw.Exit()
		return
def mid(x0,x1):
	return [(x0[0]+x1[0])/2, (x1[1]+x0[1])/2]

def vector(x0,x1):
	return [x1[0]-x0[0], x1[1]-x0[1]]


def dPoint(R, n,mid,x0):
	if n[1]!=0:
		if n[0]==0:
			sign=1
		else:
			sign=-(n[0]/n[1])/math.fabs(n[0]/n[1])
		len=R*R-(dist_p_to_p_sqr(mid,x0))
		dx=sign*(((len*n[1]*n[1])/(n[0]**2+n[1]**2))**0.5)
		dy=((len*n[0]*n[0])/(n[0]**2+n[1]**2))**0.5
		return [dx,dy]
	else:
		return [0,math.sqrt(R*R-(x0[0]-mid[0])**2)]

def counter(x0,x1,R,sign):
	global x_circle,y_circle
	midl=mid(x0,x1)
	norm=vector(x0,x1)
	dp=dPoint(R,norm,midl,x0)
	center=[midl[0]+sign*dp[0], midl[1]+sign*dp[1]]
	circle_coords(R,center)

def dist_p_to_p_sqr(x0,x1):
	return (x1[0]-x0[0])**2+(x1[1]-x0[1])**2
def gui():
	global x_circle,y_circle,x0,x1,R
	glClearColor(0,0,0,1)
 	glClear(GL_COLOR_BUFFER_BIT)
	glLineWidth(2)
	glColor3f(1.0,0,0)
	glBegin(GL_LINE_LOOP)
	counter(x0,x1,R,1)
	for i in range(len(x_circle)):
		glVertex2f(x_circle[i],y_circle[i])
	glEnd()
	glColor3f(0,0,2)
	glBegin(GL_LINE_LOOP)
	counter(x0,x1,R,-1)
	for i in range(len(x_circle)):
		glVertex2f(x_circle[i],y_circle[i])
	glEnd()
	glColor3f(0, 1.0, 0.5)
	glPointSize(5)
	glBegin(GL_POINTS)
	glVertex2f(x0[0],x0[1])
	glVertex2f(x1[0],x1[1])
	glEnd()
	changeR()


x0=[float(i) for i in raw_input("Write first point\n").split()]
while len(x0)!=2:
	x0=[float(i) for i in raw_input("Write for  first point 2 coords\n").split()]
x1=[int(i) for i in raw_input("Write second point\n").split()]
while len(x1)!=2:
	x1=[int(i) for i in raw_input("Write for  second point 2 coords\n").split()]
R=float(raw_input("Write radius of circle\n"))
if(dist_p_to_p_sqr(x0,x1)>4*R*R):
	print 'Your coord is wrong, it is impossible'
else:
	Draw.Register(gui, event,None)
