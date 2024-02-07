numberofsharespurchased = 0
pricepaidpershare = 0
purchasecommissionrate = 0

numberofsharessold = 0
pricesoldpershare = 0
salecommisionrate = 0

amountpaid = 0
amountsold = 0
profit = 0

purchasecommissionrate = float(input("Enter commision rate on purchase (ex 0.03) on stock purchase: "))
salecommissionrate = float(input("Enter commision rate on sale (ex 0.03) on stock sale: "))
numberofsharespurchased = float(input("Enter number of shares purchased: "))
numberofsharessold = float(input("Enter number of sales sold: "))
pricepaidpershare = float(input("Enter commision rate on sale: "))
pricesoldpershare = float(input("Enter sell price per share: "))

amountpaid = numberofsharespurchased*pricepaidpershare
amountsold = numberofsharessold*pricesoldpershare
profit = (amountpaid*purchasecommissionrate)-(amountsold*salecommisionrate)

print(' ')
print('Amount paid for stock:','$',(f'{amountpaid:.2f}'))
print('Commission paid on purchase:','$',(f'{amountpaid*purchasecommissionrate:.2f}'))
print('Amount stock sold for:','$',(f'{amountsold:.2f}'))
print('Commission paid on sale:','$',(f'{amountsold*salecommissionrate:.2f}'))
print('Profit (or loss if negative):','$',(f'{profit:.2f}'))
