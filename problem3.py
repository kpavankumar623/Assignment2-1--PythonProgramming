# check angles represents valid triangle or not.

def istriangle(angle1,angle2,angle3):
    if angle1 > 0 and angle3 > 0 and angle3 > 0:
        if angle1+angle2+angle3 == 180:
            return True
    return False

a,b,c = 50,40,90

if istriangle(a,b,c):
    print("The given Angles represent Valid Traingle.")
else:
    print("Not a valid Traingle")