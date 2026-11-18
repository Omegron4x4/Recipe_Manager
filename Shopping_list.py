#USER STORY 6: Create a shopping list from one or multiple selected recipes
# importing functions needed from other files
#needed for combining the ingredients in the shopping list to avoid duplicates
from ingredients import combine_ingredients

#this function will wirte a shopping list from the seleted recipes
def create_shopping_list(selected_recipes):
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