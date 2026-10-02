name = "food"
price = 7.2
amounts = 5
allsold = False
shopname = "Cit"
print(type(name))
print(type(price))
print(type(amounts))
print(type(allsold))
print("Todays order is: " + name)
print("Total Price", price * amounts)
print("Sale price: ", price - 0.25)
print("Double Price", amounts * 2)
print("Price under 2?", price < 2)
print("More then 5 in stock", amounts > 5)
print("The price exact 1.50", price == 1.50)
print(shopname)
print("The lenght of the shop name is", len(shopname))
print("The first letter of the shop name is", shopname[0])
