# calculate maximum of the list and its index

def max_num(list_num):
    max = 0
    for i in list_num:
        if max < i:
            max = i
    return max

l = [10,56,98,67,89,64]

max = max_num(l) # user defined function
index = l.index(max)    # builtin method

print("Maximum => {}, index is {}".format(max,index) )