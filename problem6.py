# program capitalize vowels from given string

def cap_vow(string):
    vowels = ['a','e','i','o','u']
    result =[]
    for char in string:
        if char in vowels:
            char = char.upper()
        result.append(char)
    return result

output = cap_vow("Python sample input string")

for i in output:
    print(i,end='')