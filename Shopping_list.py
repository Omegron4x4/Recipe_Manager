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
    shopping_list = combine_ingredients(all_ingredients)
    return shopping_list
#returns a shopping list with all ingredients from the recipes combined

# USER STORY 9: Add an item to the shopping list
def add_shopping_list_item(shopping_list, name, quantity, unit):
#parameter 1 - name of the list, then the name, quantitiy, unit - this tell python which list to work in
    if quantity <= 0:
        return False
# shopping list item must have a quantity to be valid
# units and names anything is allowed as this is for adding to the shopping list you would take with you such as soap or bin bags
    new_item = {
        "name": name,
        "quantity": quantity,
        "unit": unit
    }
# new item is a dictionary of the parameters, ready to be added to the shopping list
    shopping_list.append(new_item)
#combine ingredients in case user added an item already on the list
    merged_list = combine_ingredients(shopping_list)
#clear the shoppping list, and then rewite every item in the shoping list
# to ensure the program is refrencing the updated list
    shopping_list.clear()
    for item in merged_list:
        shopping_list.append(item)
    return True
# gives the value True to the fact that the item has been added to the shopping list