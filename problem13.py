
def adjust_dic(dic):
    result={}
    for i in dic:
        if type(dic[i]) is dict:
            for j in dic[i]:
                result[j] = dic[i][j]
        else:
            result[i] = dic[i]
    return result

dic = { 'username': 'ABC','channel' : { 'Id' : 101, 'name': 'XYZ'}}

result = adjust_dic(dic)
print(result)