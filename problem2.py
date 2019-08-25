# calculation of profit.
def profit(cost_price,sell_price):
    profit = sell_price - cost_price
    if profit < 0 :
        return "Loss of {}.".format(-profit)
    return "Profit of {}.".format(profit)

print(profit(100,200))
print(profit(50,20))

