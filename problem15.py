# tip calculation

def tip_calculator(amount,rating = 1):
    tip = 0
    if(rating == 1):
        tip = amount/100  * 5
    elif(rating == 2):
        tip = amount / 100 * 10
    elif (rating == 3):
        tip = amount / 100 * 15
    elif (rating == 4):
        tip = amount / 100 * 20
    else:
        tip = amount / 100 * 25
    return tip

tip = tip_calculator(1000,4)
print(tip)