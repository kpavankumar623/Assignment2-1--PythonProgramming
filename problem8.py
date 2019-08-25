# matrix ADDITION

def mattrix_add(mat1,mat2):
    add_list = []
    count = 0
    for a,b in zip(mat1,mat2):
        add_list.append([])
        for i,j in zip(a,b):
            add_list[count].append(i+j)
        count += 1
    return add_list

mat1 = [[10,20,30], [40,50,60], [70,80,90]]
mat2 = [[1,2,3], [4,5,6], [7,8,9]]

result = mattrix_add(mat1,mat2)
print(result)
