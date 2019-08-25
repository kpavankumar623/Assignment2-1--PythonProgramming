#find valid shuffle or not

def isvalid_suffle(str1,str2,suffle):
    combinate_str = ''.join([str1,str2])
    if len(combinate_str) != len(suffle):
        return False
    else:
        for i in suffle:
            if i not in combinate_str:
                break
        else:
            return True
    return False

str1 ="abc"
str2 = "def"
shuffle = "febcda"
print(isvalid_suffle(str1,str2,shuffle))