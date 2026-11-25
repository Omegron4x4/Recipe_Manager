#USER STORY 6: Create a shopping list from one or multiple selected recipes
# importing functions needed from other files
#needed for combining the ingredients in the shopping list to avoid duplicates
from ingredients import combine_ingredients

#determines if a shopping list name has been taken, prevents duplicate list names
def is_shopping_list_name_taken(shopping_list, list_name):
    cleaned_shopping_list = list_name.strip().lower()
#change everything to lowercase, and strip spaces away
    for existing_list in shopping_list
        if existing_list["name"].strip().lower() == cleaned_target:
            return True
    return False

#compares if any exsisting list has the name of the iput of list name



#this function will wirte a shopping list from the seleted recipes
def create_shopping_list(selected_recipes, list_name):
    all_ingredients = []
#all_ingredients = empty list to hold results

#loops through each ingredient in each recipe from the selected recipe 
    for recipe in selected_recipes:
        for item in recipe["ingredients"]:
#Add each ingredient dictionary to the end of 'all_ingredients'
            all_ingredients.append(item)
#combine all ingredeints to avoid duplicates
    merged_list = combine_ingredients(all_ingredients)
    shopping_list = {
        "name": list_name.strip(),
        "items": merged_list
    }
    return shopping_list
#returns a shopping list with all ingredients from the recipes combined

# USER STORY 9: Add an item to the shopping list
def add_shopping_item(shopping_list, name, quantity, unit):
#parameter 1 - name of the list, then the name, quantitiy, unit - this tell python which list to work in
    if quantity <= 0:
        return False
# shopping list item must have a quantity to be valid
# units and names anything is allowed as this is for adding to the shopping list you would take with you such as soap or bin bags
    new_item = make_item(name, quantity, unit)
       shopping_list["items"].append(new_item)
# new item is a dictionary of the parameters, ready to be added to the shopping list
#combine ingredients in case user added an item already on the list
     merged_list = combine_items(shopping_list["items"])
        shopping_list["items"].clear()
#clear the shoppping list, and then rewite every item in the shoping list
# to ensure the program is refrencing the updated list
    shopping_list.clear()
    for item in merged_list:
        shopping_list.append(item)
    return True
# gives the value True to the fact that the item has been added to the shopping list




def add_recipe_to_shopping_list(shopping_list, recipe):
    for item in recipe["ingredients"]:
        new_item = make_item(item["name"], item["quantity"], item["unit"])
        shopping_list["items"].append(new_item)

    merged_list = combine_items(shopping_list["items"])
    shopping_list["items"].clear()
    for item in merged_list:
        shopping_list["items"].append(item)

    return True


def update_shopping_item(shopping_list, index, new_quantity):
    if new_quantity <= 0:
        return False
# makes sure the input is for a valid item on the list

    items = shopping_list["items"]
    if index < 0 or index >= len(items):
        return False
#updates the quantity

    items[index]["quantity"] = int(round(new_quantity))
    return True

#for removing from the quantity

def remove_shopping_item(shopping_list, index):
    items = shopping_list["items"]
    if index < 0 or index >= len(items):
        return False

    item_to_remove = items[index]
    items.remove(item_to_remove)
    return True

#looks for the index of the shopping list to delete

def delete_shopping_list(shopping_lists, index):
    if index < 0 or index >= len(shopping_lists):
        return False

    list_to_remove = shopping_lists[index]
    shopping_lists.remove(list_to_remove)
    return True


if __name__ == "__main__":
    recipe_1 = {
        "name": "Tomato Soup",
        "portions": 2,
        "ingredients": [
            {"name": "Tomato", "quantity": 300, "unit": "g"},
            {"name": "Butter", "quantity": 20, "unit": "g"}
        ]
    }
    recipe_2 = {
        "name": "Tomato Salad",
        "portions": 2,
        "ingredients": [
            {"name": "Tomato", "quantity": 100, "unit": "g"},
            {"name": "Sugar", "quantity": 10, "unit": "g"}
        ]
    }
    all_lists = []
    my_list = create_shopping_list([recipe_1, recipe_2], "Weekend Groceries")
    all_lists.append(my_list)
    print("1. Created shopping list:", my_list)
    print("Is 'weekend groceries' taken?", is_shopping_list_name_taken(all_lists, "weekend groceries"))
    add_shopping_item(my_list, "Egg", 150, "g")
    print("2. After adding Egg:", my_list)
    update_shopping_item(my_list, 1, 50)
    print("3. After updating index 1 (Butter) to 50g:", my_list)
    remove_shopping_item(my_list, 2)
    print("4. After removing index 2 (Sugar):", my_list)
    delete_shopping_list(all_lists, 0)
    print("5. After deleting shopping list:", all_lists)
