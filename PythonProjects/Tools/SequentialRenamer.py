import maya.cmds as cmds

txt = "Leg_##_Int"

count = txt.count("#")
nums = "#" * count

x = txt.find(nums)
if x == -1:
    print("# should only be used in between the Name and NodeType.  Ensure all arguments are named appropriately")
else:
    parts = txt.partition(nums)
    print(parts)
    print(parts[1])

    sels = cmds.ls(sl=True)
    for sel in sels:
        i = sels.index(sel)
        print(i)
        nums = nums.replace(nums, str(i))
        nums = nums.zfill(count)

        cmds.rename([sel], parts[0] + nums + parts[2])
        print(sel)


##def RenameSequentially(Leg_###_Jnt)
