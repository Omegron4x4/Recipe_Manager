
#this fucntion will combine the ingredients from a list of chosen recipes
#ingredient_list is a list of dictionaries
def combine_recipes(ingredient_list):
    combined_list = []
    #combined_list = empty list to hold results

#the for statement is designed to work with a sequence of data items.
#When the statement executes, it iterates once for each item in the sequence
#each pass, the current dictionary is stored in the variable 'item'
    for item in ingredient_list
        found = False
# found = False is a boolean Flag, has to be placed inside to reset found to false for each run through.
#if not reset, the program would stop adding ingredients to the list after the first duplicate was found
        for exsting_item in combined_list
        if existing_item["name"] == item["name"] and existing_item["unit"] == item["unit"]:
            existing_item["quantity"] = existing_item["quantity"] + item["quantity"]
            found = True
# if found is still false, the ingredient is added to the list "not found = False"
        if not found:
                    new_entry = {
                        "name": item["name"],
                        "quantity": item["quantity"],
                        "unit": item["unit"]
                    }
                    combined_list.append(new_entry)
        
            return combined_list
#the combined list is now being cycled through again untill all ingredients have been added to "combined list"