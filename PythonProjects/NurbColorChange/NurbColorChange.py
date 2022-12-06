import maya.cmds as cmds

def ChangeOutlineColor():

    sel = cmds.ls(sl=True)[0]
    shape = cmds.listRelatives(sel)

    cmds.setAttr(shape[0] + ".overrideEnabled", 1)
    cmds.setAttr(shape[0] + ".overrideColor", 15)

#"color" must be between either 1 or 0 and 32
ChangeOutlineColor()

