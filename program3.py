raw_amount=input("Enter your amount of money: ")
amount =int(raw_amount)
priceApple=input("Enter the price of apple: ")
price_apple= int(priceApple)

quantity= int(amount/price_apple)
payment=int(price_apple*quantity)
change=amount%payment


print(f"You can buy {quantity} apples and your change is {change} pesos.")
