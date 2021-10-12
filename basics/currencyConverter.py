def converter(currency, dollar_value):
    pesos = input("Insert the amount of " + currency + ": ")
    pesos = float(pesos)
    amount = str(round(pesos / dollar_value, 2))
    print("you have:", currency, "$",  amount)


menu = """
    Welcome to the currency converter  💵 
    1 - COP
    2 - ARP
    3 - MXP
Select and option: """

option = int(input(menu))

if option == 1:
    converter("COP", 3875)
elif option == 2:
    converter("ARP", 65)
elif option == 3:
    converter("MXP", 24)
else:
    print('please select a valid option')
