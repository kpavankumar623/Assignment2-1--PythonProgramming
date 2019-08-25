#power bill generator

def gen_bill(units):
    bill_amount = 0
    if units > 250:
        bill_amount += (units - 250) * 1.50
        units = 250
    if units <= 250 and units > 150:
        bill_amount += (units - 150) * 1.20
        units = 150
    if units <= 150 and units > 50:
        bill_amount += (units - 50) * 0.75
        units = 50
    if units <= 50:
        bill_amount += units * 0.50
    bill_amount += (bill_amount/100) * 20
    return bill_amount

units = int(input("Enter the units of power: "))
print(gen_bill(units))