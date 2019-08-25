# calculate sum of two numbers if numbers are equal double their sum
def sum_gen(num1, num2):
    sum = num1 + num2
    if(num1 == num2):
        return sum *2
    return sum

print(sum_gen(10,10))
print(sum_gen(5,10))