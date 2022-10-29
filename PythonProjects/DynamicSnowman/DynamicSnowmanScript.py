import maya.cmds as cmds

size = 2.0

base = cmds.polySphere(radius=size, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.move(0, size, 0, base, relative=True)

middle = cmds.polySphere(radius=size * 2/3, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.move(0, ((size * 2) + (size * 2/3) - ((size * 2/3) * 1/3)) , 0, middle, relative=True)

head = cmds.polySphere(radius=size*1/3, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.move(0, ((size * 2) + ((size * 2/3) * 2)), 0, head, relative=True)

nose = cmds.polyCone(radius=size * 1/10, height=size *2/3, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.rotate(90, 0, 0, nose)
cmds.move(0, ((size * 2) + ((size * 2/3) * 2)), (size * 1/4), nose, relative=True)

rightEye = cmds.polySphere(radius=size*1/20, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.move((size * -13/100), (size * 3.433), (size * .25), rightEye, relative=True)
leftEye = cmds.polySphere(radius=size*1/20, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.move((size * 13/100), (size * 3.433), (size * .25), leftEye, relative=True)

middleButton = cmds.polyTorus(radius=size * .06, sectionRadius=size * 1/50, twist=0, subdivisionsX=20, subdivisionsY=1,axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.rotate(90, 0, 0, middleButton, relative=True, objectSpace=True, forceOrderXYZ=True)
cmds.move(0, size * 2.4, size * 2/3, middleButton, relative=True)

topButton = cmds.polyTorus(radius=size * .06, sectionRadius=size * 1/50, twist=0, subdivisionsX=20, subdivisionsY=1,axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.rotate(75, 0, 0, topButton, relative=True, objectSpace=True, forceOrderXYZ=True)
cmds.move(0, size * 8/3, size * 1.9/3, topButton, relative=True)

bottomButton = cmds.polyTorus(radius=size * .06, sectionRadius=size * 1/50, twist=0, subdivisionsX=20, subdivisionsY=1,axis=[0,1,0], createUVs=2, constructionHistory=True)
cmds.rotate(115, 0, 0, bottomButton, relative=True, objectSpace=True, forceOrderXYZ=True)
cmds.move(0, size * 6.457/3, size * 1.8/3, bottomButton, relative=True)

hatBrim = cmds.polyCylinder(radius=size * 1/3, height=size / 15, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0,1,0], roundCap=False, createUVs=2, constructionHistory=True)
cmds.move(size * -.1, size* 11/3, 0, hatBrim, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.rotate(0, 0, 15, hatBrim, relative=True, objectSpace=True, forceOrderXYZ=True)

hat = cmds.polyCylinder(radius=size * .2, height=size / 3, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=[0,1,0], roundCap=False, createUVs=2, constructionHistory=True)
cmds.move((size * -.1), ((size * 11/3) + ((size / 3) / 2) + ((size / 15) / 2)),  0, hat, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.rotate(0, 0, 15, hat, relative=True, objectSpace=True, forceOrderXYZ=True)
cmds.move((size * -.05), 0, 0, hat, relative=True, objectSpace=True, worldSpaceDistance=True)





