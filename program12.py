# variable length keyword arguments example.

def bill_amount(**items):
    input = {"A": 2500, "B": 1000, "C": 500, "D": 450}
    tax = 18
    total_amount = 0.0
    for item,qunti in items.items():
        if item in input:
            cost = ((input[item] / 100)*tax) * qunti
        else:
            continue
        total_amount += cost
    return total_amount

cost = bill_amount(A=3,B=4,C=2,E=1)
print(cost)