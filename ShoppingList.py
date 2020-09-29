"""Shopping list
        Jawad K Mohammed Hussein
            CEIS110
                09/29/2020
"""
print("Welcome to your shopping list\n")

shopping_list = []
need_item = True
add_item = (input("Add item? (y/n): "))
while add_item == "y":
    shopping_list.append(input("Enter item name: "))
    add_item = (input("Add another one? (y/n)"))
    
if add_item == "n":

    need_item = False
    print("Your Shopping list for today\n -------------\n")
    for a in shopping_list:
        print(a)
    if len(shopping_list) == 0:
        print("Empty!!!")
else:
    print("No shoppping it is...")