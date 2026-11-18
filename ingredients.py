#USER STORY 8: Combine identical ingredients that have the same unit
#this fucntion will combine the ingredients from a list
#ingredient_list is a list of dictionaries
def combine_ingredients(ingredient_list):
    combined_list = []
    #combined_list = empty list to hold results

#the for statement is designed to work with a sequence of data items.
#When the statement executes, it iterates once for each item in the sequence
#each pass, the current dictionary is stored in the variable 'item'
    for item in ingredient_list:
        found = False
# found = False is a boolean Flag, has to be placed inside to reset found to false for each run through.
#if not reset, the program would stop adding ingredients to the list after the first duplicate was found
        for existing_item in combined_list:
            if existing_item["name"] == item["name"] and existing_item["unit"] == item["unit"]:
                existing_item["quantity"] = existing_item["quantity"] + item["quantity"]
                found = True
# if found is still false, the ingredient is added to the list "not found = False" - if it was true it would mean that the ingredieent was found in our list
            if not found:
# new entry - "Alias versus Copy", new entry adds a new dictionary in a new place and appends it to the combined list, 
# instead of appending directly which would also overwrite the the amunts in the original recipe
# alias happens when two different variable names (or two different lists) point to the exact same object in your computer's memory
                new_entry = {
                    "name": item["name"],
                    "quantity": item["quantity"],
                    "unit": item["unit"]
                }
                combined_list.append(new_entry)
        
        return combined_list
#the combined list is now being cycled through again untill all ingredients have been added to "combined list"