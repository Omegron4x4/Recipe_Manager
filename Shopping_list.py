# shopping.py
# Responsible: Niels (US6, US8, US9)

# Importing functions needed from other files (to combine duplicate ingredients and create standardized items)
from ingredients import combine_items, make_item


# Determines if a shopping list name has already been taken, preventing duplicate list names
def is_shopping_list_name_taken(shopping_lists, list_name):
    # Change everything to lowercase and strip spaces away
    cleaned_target = list_name.strip().lower()
    # Compares if any existing list has the same name as the input list_name
    for existing_list in shopping_lists:
        if existing_list["name"].strip().lower() == cleaned_target:
            return True
    return False


# USER STORY 6 & 8: Create a shopping list from one or multiple selected recipes
def create_shopping_list(selected_recipes, list_name):
    # Empty list to hold all collected ingredient dictionaries
    all_ingredients = []

    # Loops through each ingredient in each recipe from the selected recipes
    # Create a shopping list by combining ingredients from one or more recipes
    # Merges identical ingredients that share the same unit into one entry
    for recipe in selected_recipes:
        for item in recipe["ingredients"]:
            # Add each ingredient dictionary to the end of 'all_ingredients'
            all_ingredients.append(item)

    # Combine all ingredients to avoid duplicates
    merged_items = combine_items(all_ingredients)
    shopping_list = {
        "name": list_name.strip(),
        "items": merged_items
    }
    # Returns a shopping list dictionary with all ingredients from the recipes combined
    return shopping_list


# Adds a single recipe's ingredients into an already existing shopping list
def add_recipe_to_shopping_list(shopping_list, recipe):
    # Add a recipe's ingredients into an existing shopping list and merge duplicates
    # Loop through each ingredient in the recipe and add a copy to the list
    for item in recipe["ingredients"]:
        new_item = make_item(item["name"], item["quantity"], item["unit"])
        shopping_list["items"].append(new_item)

    # Combine ingredients in case the recipe had items already on the shopping list
    merged_list = combine_items(shopping_list["items"])

    # Clear the shopping list items and rewrite them so the program references the updated list
    shopping_list["items"].clear()
    for item in merged_list:
        shopping_list["items"].append(item)

    return True


# USER STORY 9: Add an item to the shopping list
def add_shopping_item(shopping_list, name, quantity, unit):
    # Parameter 1 is the shopping list dictionary, followed by name, quantity, and unit
    # Shopping list item must have a quantity > 0 to be valid
    # Automatically merges with an existing item if name and unit match
    if quantity <= 0:
        return False

    # Build a dictionary of the parameters and append it to the shopping list items
    new_item = make_item(name, quantity, unit)
    shopping_list["items"].append(new_item)

    # Combine ingredients in case the user added an item already on the list
    merged_list = combine_items(shopping_list["items"])

    # Clear the shopping list items, and then rewrite every item
    # to ensure the program is referencing the updated list
    shopping_list["items"].clear()
    for item in merged_list:
        shopping_list["items"].append(item)

    # Gives the value True to confirm the item has been added to the shopping list
    return True


# USER STORY 9: Update the quantity of an existing item on the shopping list
# Update the quantity of an existing shopping list item by index
# Rejects quantities <= 0 or out-of-range list indices
def update_shopping_item(shopping_list, index, new_quantity):
    # Makes sure the new quantity is valid (> 0)
    if new_quantity <= 0:
        return False

    items = shopping_list["items"]
    # Makes sure the index points to a valid item on the list
    if index < 0 or index >= len(items):
        return False

    # Updates the quantity (rounded to the nearest whole number)
    items[index]["quantity"] = int(round(new_quantity))
    return True


# USER STORY 9: Remove an item from the shopping list
def remove_shopping_item(shopping_list, index):
    items = shopping_list["items"]
    # Makes sure the index points to a valid item on the list
    if index < 0 or index >= len(items):
        return False

    # Find the item at that index and remove it from the list
    item_to_remove = items[index]
    items.remove(item_to_remove)
    return True


# USER STORY 9: Delete an entire shopping list
    # Delete a shopping list from the list of shopping lists by index
    # Returns False if the index does not exist

def delete_shopping_list(shopping_lists, index):
    # Looks for a valid index of the shopping list to delete
    if index < 0 or index >= len(shopping_lists):
        return False

    # Remove the selected shopping list dictionary from the master list
    list_to_remove = shopping_lists[index]
    shopping_lists.remove(list_to_remove)
    return True

