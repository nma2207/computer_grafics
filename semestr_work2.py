import Blender as B
import time
from Blender import Draw
from Blender.BGL import *
ob1=B.Object.Get('Sphere')
msh1=ob1.getData(False,True)
ob2=B.Object.Get('Sphere.001')
fs1=msh1.faces
msh2=ob2.getData(False,True)
fs2=msh2.faces

a=0
r1=2
r2=2
buffP=Buffer(GL_FLOAT,4,[0.,0.,20,1.]) #initial position of LIGHT0 (proj coords)
def changeA():
	global a
	if(a<r1+r2):
		a+=0.01
		time.sleep(0.01)
		Draw.Redraw(1)
def key(evt,val):
	if evt==Draw.ESCKEY: Draw.Exit()
def plane():
	glBegin(GL_QUADS)
	glVertex3f(-20,-20,-1)
	glVertex3f(20,-20,-1)
	glVertex3f(20,20,-1)
	glVertex3f(-20,20,-1) #  plane where we see  shadow
	glEnd()
def createMatr():	# creates shadow matrix that transforms the original triangles into its shadow
	glLightfv(GL_LIGHT0,GL_POSITION,buffP)
	glEnable(GL_LIGHT0)
	mmat=Buffer(GL_FLOAT,16,[buffP[2],0, 0,0 , 0,buffP[2],0,0, -buffP[0],-buffP[1],0, -1,  0,0,0, buffP[2]])
	glMultMatrixf(mmat)
def gui():
	glClearColor(0,0,0,1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glViewport(0,0,1000,1000)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
#	glFrustum(-100,100,-100,100,30,500)
	glOrtho(-10,10,-10,10,-500,500)
	glEnable(GL_LIGHTING)
	pos=Buffer(GL_FLOAT,4,(-2,2,7,1))
	glLightfv(GL_LIGHT0,GL_POSITION,pos)
	dif=Buffer(GL_FLOAT,4,(0.5,0.,0.,1.))
	glLightfv(GL_LIGHT0,GL_DIFFUSE,dif)
	spec=Buffer(GL_FLOAT,4,(0.5,.5,0.5 ,1))
	glLightfv(GL_LIGHT0,GL_SPECULAR,spec)
	#amb=Buffer(GL_FLOAT,4,(0,0,1,1.))
	#glLightfv(GL_LIGHT0,GL_AMBIENT,amb)
	circle1()
	circle2()
	#createMatr()
	#glColor3f(0,0,0)
	#circle1()
	#circle2()
	#glColor3f(0,0,0)

	changeA()
def createMatr():	# creates shadow matrix that transforms the original triangles into its shadow
	glLightfv(GL_LIGHT0,GL_POSITION,buffP)

	glEnable(GL_LIGHT0)
	mmat=Buffer(GL_FLOAT,16,[buffP[2],0, 0,0 , 0,buffP[2],0,0, -buffP[0],-buffP[1],0, -1,  0,0,0, buffP[2]])
	glMultMatrixf(mmat)
def plane():
	glBegin(GL_QUADS)
	glVertex3f(-20,-20,-5)
	glVertex3f(20,-20,-5)
	glVertex3f(20,20,-5)
	glVertex3f(-20,20,-5) #  plane where we see  shadow
	glEnd()

def circle1():
	glPushMatrix()
	glTranslatef(-5-a/2,0,0)
	#glRotatef(20,1,1,1)
	glColor3f(0,1,0)
	for ff in fs1:

		if len(ff.verts)==4:

			glBegin(GL_QUADS)
			for pt in ff.verts:
				glVertex3f(pt.co.x,pt.co.y,pt.co.z)
			glEnd()
		if len(ff.verts)==3:

			glBegin(GL_TRIANGLES)
			for pt in ff.verts:
				glVertex3f(pt.co.x,pt.co.y,pt.co.z)
			glEnd()
	glPopMatrix()

def circle2():
	glPushMatrix()
	glTranslatef(-5+a/2,0,0)
	glColor3f(1,0,0)
	for ff in fs2:
		if len(ff.verts)==4:

			glBegin(GL_QUADS)
			for pt in ff.verts:
				glVertex3f(pt.co.x,pt.co.y,pt.co.z)
			glEnd()
		if len(ff.verts)==3:
			glBegin(GL_TRIANGLES)
			for pt in ff.verts:
				glVertex3f(pt.co.x,pt.co.y,pt.co.z)
			glEnd()
	glPopMatrix()

Draw.Register(gui,key,None)
