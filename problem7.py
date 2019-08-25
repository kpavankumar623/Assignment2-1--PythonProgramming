#checking valid floating point number or not.

def is_float(num):
    if type(num) == float:
        return True
    return False


if is_float(14.55):
   print("The Floating point num")
else:
    print("Not Floating point number")
