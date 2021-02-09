# Volume Calculator by Ali Mohamed(251192600)

import volume  # Allows for access to volume.py module

#  Variable Declarations
inshape = ""  # Temporarily stores requested shape
involume = 0.0  # Temporarily stores requested volume
shapes = []  # List to store valid shapes
volumes = []  # List to store valid volumes

while (inshape != "q") and (inshape != "quit"):  # While the user has not quit
    inshape = str(input("Please enter shape (cube/c, pyramid/p, ellipsoid/e, q/quit):"))
    if (inshape.lower() == "cube") or (inshape.lower() == "c"):
        shapes.append("cube")
        side = float(input("Enter the length of side for the cube:"))
        involume = volume.volcube(side)
        print("The volume of the cube with side %.1f is %.2f \n" % (side, involume))
        volumes.append(involume)
    elif (inshape.lower() == "pyramid") or (inshape.lower() == "p"):
        shapes.append("pyramid")
        base = float(input("Enter the base length of the pyramid:"))
        height = float(input("Enter the height of the pyramid:"))
        involume = volume.volpyramid(base, height)
        print("The volume of the pyramid with base %.1f and height %.1f is %.2f \n" % (base, height, involume))
        volumes.append(involume)
    elif (inshape.lower() == "ellipsoid") or (inshape.lower() == "e"):
        shapes.append("ellipsoid")
        radius1 = float(input("Enter the first radius:"))
        radius2 = float(input("Enter the second radius:"))
        radius3 = float(input("Enter the third radius:"))
        involume = volume.volellipsoid(radius1, radius2, radius3)
        print("The volume of the ellipsoid with radii %.1f and %.1f and %.1f is %.2f \n" % (radius1, radius2, radius3, involume))
        volumes.append(involume)
    elif (inshape.lower() == "q") or (inshape.lower() == "quit"):
        break
    else:
        print("Invalid input detected, please try again:")

finallist = [(shapes[i], volumes[i]) for i in range(0, len(shapes))]  # Merges the 2 list together to form a tuple
finallist.sort(key=lambda finallist: finallist[1])  # Sorts the tuple from smallest to largest

if len(finallist) == 0:
    print("Output: No shapes entered.")
else:
    print("Output: Volumes of shapes entered in sorted order:")
    for x in range(len(finallist)):
        print("%s %.2f" % (finallist[x][0], finallist[x][1]))
