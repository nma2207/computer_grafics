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
sign=1
r1=2
r2=2
buffP=Buffer(GL_FLOAT,4,[-2.,-2.,3,1.]) #initial position of LIGHT0 (proj coords)
def changeA():
	global a,sign
	d=0.03
	if(a<0 or a>r1+r2):
		sign*=-1
	a+=sign*d
	#buffP[0] +=1 #   changes  coords after each step
	#buffP[1] +=2
	time.sleep(0.01)
	Draw.Redraw(1)

def key(evt,val):
	if evt==Draw.ESCKEY: Draw.Exit()
def plane():
	glBegin(GL_QUADS)
	glVertex3f(-1000,-1000,0)
	glVertex3f(1000,-1000,0)
	glVertex3f(1000,1000,0)
	glVertex3f(-1000,1000,0) #  plane where we see  shadow
	glEnd()

def createMatr():	# creates shadow matrix that transforms the original triangles into its shadow
	glLightfv(GL_LIGHT0,GL_POSITION,buffP)
	glEnable(GL_LIGHT0)
	spec=Buffer(GL_FLOAT,4,(0,0,0,1))
	glLightfv(GL_LIGHT0,GL_SPECULAR,spec)
	mmat=Buffer(GL_FLOAT,16,[buffP[2],0, 0,0 , 0,buffP[2],0,0, -buffP[0],-buffP[1],0, -1,  0,0,0, buffP[2]])
	glMultMatrixf(mmat)
	#amb=Buffer(GL_FLOAT,4,(0,0,1,1.))
	#glLightfv(GL_LIGHT0,GL_AMBIENT,amb)
	#dif=Buffer(GL_FLOAT,4,(0.,0.,0.,1.))
	#glLightfv(GL_LIGHT0,GL_DIFFUSE,dif)
	#spec=Buffer(GL_FLOAT,4,(0,0,0 ,1))
	#glLightfv(GL_LIGHT0,GL_SPECULAR,spec)

def gui():
	glClearColor(1,1,1,1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glViewport(0,0,1000,1000)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
#	glFrustum(-100,100,-100,100,30,500)
	glOrtho(-10,10,-10,10,-500,500)
	#glTranslatef(0,-5,5)
	glEnable(GL_LIGHTING)
	pos=Buffer(GL_FLOAT,4,(-2,2,5,1))
	glLightfv(GL_LIGHT0,GL_POSITION,buffP)
	dif=Buffer(GL_FLOAT,4,(0.5,0.,0.,1))
	glLightfv(GL_LIGHT0,GL_DIFFUSE,dif)
	spec=Buffer(GL_FLOAT,4,(1,1,1 ,1))
	glLightfv(GL_LIGHT0,GL_SPECULAR,spec)
	amb=Buffer(GL_FLOAT,4,(0.5,0.5,0.5,1))
	glLightfv(GL_LIGHT0,GL_AMBIENT,amb)
	glEnable(GL_COLOR_MATERIAL);
	glColor3f(0,1,0)
	#glTranslatef(0,0,10)
	circle1()
	glColor3f(1,0,0)
	circle2()
	glTranslatef(0,0,-10)
	#glLoadIdentity()
	glColor3f(1,1,1)
	plane()
	createMatr()
	#glTranslatef(8,2.8,0)

	glColor3f(0,0,0)
	circle1()
	circle2()

	#glColor3f(0,0,0

	changeA()

def plane():
	glBegin(GL_QUADS)
	glVertex3f(-20,-20,-5)
	glVertex3f(20,-20,-5)
	glVertex3f(20,20,-5)
	glVertex3f(-20,20,-5) #  plane where we see  shadow
	glEnd()

def circle1():
	glPushMatrix()
	glTranslatef(-a/2,0,0)
	#glRotatef(20,1,1,1)
	#glColor3f(0,1,0)
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
	glTranslatef(+a/2,0,0)
	#`glColor3f(1,0,0)
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
