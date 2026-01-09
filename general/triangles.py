angle1 = input("enter angle 1:")
angle1 = int(angle1)
angle2 = input("enter angle 2:")
angle2 = int(angle2)
angle3 = input("enter angle 3:")
angle3 = int(angle3)
if (angle1 == 90 and angle2 + angle3 == 90) or (angle2 == 90 and angle1 + angle3 == 90):
    print("this is a triangle")