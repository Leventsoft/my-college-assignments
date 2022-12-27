supermarketList = list(("milk", "eggs", "flour", "rice", "oranges", "apples"))
basket = list(())

while len(supermarketList) != 0:

    order = input("Enter item name: ")
    for i in supermarketList:
        if i == order:
            basket.append(i)
            length = len(basket)
            print(f"{i} is in the list, added to the basket ({basket})")
            supermarketList.remove(i)

            