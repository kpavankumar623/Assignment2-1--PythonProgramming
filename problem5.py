# find given number of fibbonacci numbers

def fibbo(num):
    num1 = 0
    num2 = 1
    result=[]
    while(num != 0):
        result.append(num1)
        num1 , num2 = num2, num1+num2
        num -=1
    return result

print(fibbo(20))