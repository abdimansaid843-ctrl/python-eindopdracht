shopping_list = ["milk", "eggs", "bread", "butter", "cheese"]
print(shopping_list)

shopping_list.append("apples")   
shopping_list.append("cake")
print(shopping_list)  

if "butter" in shopping_list:
    print("butter is in this shopping list")
else:
    print("butter is not in this shopping list")
shopping_list.remove("butter")


print(shopping_list)


if "butter" in shopping_list:
    print("butter is in this shopping list")
else:
    print("butter is not in this shopping list")


print("what youve bought:", shopping_list)

print ("amount of items in the shopping list: ", len(shopping_list))
print("what youve bought:", shopping_list)