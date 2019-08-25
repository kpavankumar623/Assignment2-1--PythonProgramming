# program to convert values in to kays and keys into values in dic.(emp,manger)

emp_manage ={  "A": "C" , "B": "C" ,  "C": "F" , "D": "E" ,  "E": "F" , "F": "F" }
report_manager = {}
for key,value in emp_manage.items():
    if value in report_manager:
        report_manager[value] = [report_manager[value],key]
    else:
        report_manager[value] = key

print(report_manager)