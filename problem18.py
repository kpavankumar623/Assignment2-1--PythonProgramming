#find the data dic value set and place theat one set.

dic = {"ABC":("A","B","C"),"CDF":("C","D","F"),"XYZ":("X",'Y','Z')}
set_ofid = set()
for i in dic:
    for j in dic[i]:
        set_ofid.add(j)
print(set_ofid)