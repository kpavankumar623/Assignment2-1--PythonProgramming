# program find number of occurences of numbers in list

def num_count(num_list):
    num_set = set(num_list)
    count = {}
    for i in num_set:
        count[i] = num_list.count(i)
    return count

num_list = [10,10,20,10,30,20]
num_count = num_count(num_list)
print(num_count)