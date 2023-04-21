products = {
    'milk': 2,
    'fish': 5,
    'beer': 3
    }

# ------------------- ADD_PRODUCT -----------------------------
# Funkcija pridėjimo į sąrašą. Jei toks produktas egzistuoja
# prie jo prideda count reikšmę
def add_product(product_dict, product_name, count):
    # add products, 
    # if product is solid unit == kg
    # if product is solid unit == litres (l)
    if product_name in product_dict:
        product_dict[product_name] += count
        print(f"{product_name} count changed successfully)")
    else:
        product_dict[product_name] = count
        print(f"{product_name} added successfully")
    return product_dict

    # Pavyzdys patikrinimui su user input'ais.
added_product = input("Enter product name you wish to add: ")
product_count = float(input("Enter the amount you are adding: "))
add_product(products, added_product, product_count)
print(products)


# Pavyzdys patikrinimui su user input'ais.
# added_product = input("Enter product name you wish to add: ")
# product_count = input("Enter the amount you are adding: ")
# add_product(products, added_product, product_count)
# print(products)

# ------------------- REMOVE_PRODUCT --------------------------
# Funkcija produkto išėmimui iš sąrašo
# Count_reduce naudojame, kaip kintamąjį su kurio atemame produkto kiekį,
# jeigu paliekame 0, produktas istrinamas
def remove_product(product_dict, product_name, count_reduce=0):
    if product_name in product_dict:
        if count_reduce == 0:
            del product_dict[product_name]
            print(f"{product_name} removed successfully")
        else:
            product_dict[product_name] -= count_reduce
            print(f"{product_name} count successfully changed by {count_reduce}")
    else:
        print(f"{product_name} is not in the fridge")
    return product_dict

# Produkto panaikinimas/redagavimas kiekio iš sąrašo produktų
print(products)
remove_product_name = input("Enter the name of the product to update: ")
if remove_product_name in products:
    reduction = input("Enter the amount you want to reduce (leave blank for complete removal): ")
    if len(reduction) == 0: # Patikriname ką iveda vartotojas/ar paliko tuščią
        reduction = 0.0
    else:
        reduction = float(reduction) # Konvertuojame įvestą string
    products = remove_product(products, remove_product_name, count_reduce=reduction)
    print("Updated product list:", products)
else:
    print(f"{remove_product} is not in the product list.")


    # def remove_product_check(product_dict, remove_product_name):
    # if remove_product_name in product_dict:
    #     reduction = input("Enter the amount you want to reduce (leave blank for complete removal): ")
    #     if len(reduction) == 0: # Patikriname ką iveda vartotojas/ar paliko tuščią
    #         reduction = 0.0
    #     else:
    #         reduction = float(reduction) # Konvertuojame įvestą string
    #         if remove_product_name in product_dict:
    #             products = remove_product(products, remove_product_name, count_reduce=reduction)
    #             print("Updated product list:", products)
    # else:
    #     print(f"{remove_product} is not in the product list.")