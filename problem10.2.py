# print sum of two dictionatrys  values in third dict

def sum_dic(d1,d2):
    result={}
    for i in d1:
        if i in d2:
            result[i] = d1[i]+d2[i]
        else:
            result[i] = d1[i]
    for j in d2:
        if j not in d1:
            result[j] = d2[j]
    return result


dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'a': 300, 'b': 200, 'e':400}

sum_dic = sum_dic(dic1,dic2)
print(sum_dic)