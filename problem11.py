#converting seconds time to HH:MM:SS format using positinal argumets passing technique in functions

def time_converter(input):#seconds format int
    hours, minutes = 0, 0
    if input % 3600 != input:
        hours = input // 3600
        input %= 3600
    if input % 60:
        minutes = input // 60
        input %= 60
    return hours,minutes,input

time = int(input("Enter the time in seconds: "))
hours, minutes ,seconds = time_converter(time)
print("{}:{}:{}".format(hours,minutes,seconds))