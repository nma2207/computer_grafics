'''
Color cube on base of plane
Implement MultMatrix
Camera looks at vertex
'''
import Blender
from Blender import Draw, BGL
from Blender.BGL import *
import time
import math
from math import sqrt
a=0
d=1
def changeA():
	global a
	global d
	a +=10
	d+=.8
	time.sleep(0.1)
	Draw.Redraw(1)
def key(evt,val):
	if evt==Draw.ESCKEY: Draw.Exit()
def a_cube():
	glBegin(GL_QUADS)
	glVertex3f(-5,-5,0)
	glVertex3f(5,-5,0)
	glVertex3f(5,5,0)
	glVertex3f(-5,5,0)
	glEnd()
def myCube():
	glPushMatrix()
	glTranslatef(0,0,5)
	glColor3f(1,0,0)
	a_cube()
	glTranslatef(0,0,-10)
	glRotatef(180,0,1,0)
	glColor3f(0,1,0)
	a_cube()
	glPopMatrix()
	glPushMatrix()
	glRotatef(90,0,1,0)
	glTranslatef(0,0,5)
	glColor3f(0,0,1)
	a_cube()
	glTranslatef(0,0,-10)
	glRotatef(180,0,1,0)
	glColor3f(1,1,0)
	a_cube()
	glPopMatrix()
	glPushMatrix()
	glRotatef(90,1,0,0)
	glTranslatef(0,0,5)
	glColor3f(1,0,1)
	a_cube()
	glTranslatef(0,0,-10)
	glRotatef(180,1,0,0)
	glColor3f(0,1,1)
	a_cube()
	glPopMatrix()
def a_prizma():
	z=(3**0.5)*5
	glBegin(GL_POLYGON)
	glVertex3f(-10,0,0)
	glVertex3f(-5,z,0)
	glVertex3f(5,z,0)
	glVertex3f(10,0,0)
	glVertex3f(5,-z,0)
	glVertex3f(-5,-z,0)
	glEnd()
def myPrizma():
	z=(3**0.5)*5
	glPushMatrix()
	glTranslatef(0,0,5)
	glColor3f(0,1,0)
	a_prizma()
	glTranslatef(0,0,-10)
	glRotatef(180,0,1,0)
	glColor3f(0,1,0)
	a_prizma()
	glPopMatrix()

	glPushMatrix()
	glTranslatef(0,z,0)
	glRotatef(90,1,0,0)
	#glRotatef(90,0,0,1)

	glColor3f(1,0,0)
	a_cube()
	glRotatef(180,1,0,0)
	glTranslatef(0,0,-2*z)
	a_cube()


	glPopMatrix()

	glPushMatrix()
	glColor3f(1,1,1)
	glRotatef(90,1,0,0)
	glRotatef(60,0,1,0)
	glTranslatef(0,0,z)

	a_cube()
	glRotatef(180,0,0,1)
	glTranslatef(0,0,-2*z)
	a_cube()
	glColor3f(0,0,1)
	glPopMatrix()
	glPushMatrix()

	glRotatef(90,1,0,0)
	glRotatef(-60,0,1,0)
	glTranslatef(0,0,z)

	a_cube()
	glRotatef(180,0,0,1)
	glTranslatef(0,0,-2*z)
	a_cube()
	glPopMatrix()
def createMyCubeScene():
	glPushMatrix()
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	#glPushMatrix()
	glRotatef(a,1,1,0)
	myPrizma()
	glPopMatrix()

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glRotatef(a,0,0,1)

	glTranslatef(30,15,0)

	glRotatef(2*d,1,0,1)
	myCube()
	glPopMatrix()


def gui():
	glClearColor(0,0,0,1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glViewport(0,0,1000,1000)
	glPushMatrix()
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
#	glFrustum(-100,100,-100,100,30,500)
	glOrtho(-20,100,-20,100,-200,200)
	v1=1/sqrt(2)
	v2=1/sqrt(2)
	v3=v1*v2
	v4=v1/v2
	buf=Buffer(GL_FLOAT,16,[v3,v2,v1,0,v3,-v2,v1,0,-v4,0,v1,0,0,0,0,1])
	#glMultMatrixf(buf)
	glTranslatef(50,50,50)

	glMultMatrixf(buf)

	createMyCubeScene()
	#glMatrixMode(GL_MODELVIEW)
	#glTranslatef(50*math.cos(d),50*math.sin(d),0)

	#glRotatef(2*a,0,1,0)

	changeA()
Draw.Register(gui,key,None)
