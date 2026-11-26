
# list of ingredients and units
INGREDIENTS = {
    "Almonds": {"kcal_per_100_g": 579, "vegan": True, "vegetarian": True},
    "Appenzeller": {"kcal_per_100_g": 395, "vegan": False, "vegetarian": True},
    "Apple": {"kcal_per_100_g": 52, "vegan": True, "vegetarian": True},
    "Bacon": {"kcal_per_100_g": 417, "vegan": False, "vegetarian": False},
    "Baking powder": {"kcal_per_100_g": 53, "vegan": True, "vegetarian": True},
    "Balsamic vinegar": {"kcal_per_100_g": 88, "kcal_per_100_ml": 88, "vegan": True, "vegetarian": True},
    "Banana": {"kcal_per_100_g": 89, "vegan": True, "vegetarian": True},
    "Basil": {"kcal_per_100_g": 23, "vegan": True, "vegetarian": True},
    "Beef": {"kcal_per_100_g": 250, "vegan": False, "vegetarian": False},
    "Beetroot": {"kcal_per_100_g": 43, "vegan": True, "vegetarian": True},
    "Bell pepper": {"kcal_per_100_g": 31, "vegan": True, "vegetarian": True},
    "Berries": {"kcal_per_100_g": 50, "vegan": True, "vegetarian": True},
    "Black pepper": {"kcal_per_100_g": 251, "vegan": True, "vegetarian": True},
    "Bratwurst": {"kcal_per_100_g": 297, "vegan": False, "vegetarian": False},
    "Bread": {"kcal_per_100_g": 265, "vegan": True, "vegetarian": True},
    "Breadcrumbs": {"kcal_per_100_g": 395, "vegan": True, "vegetarian": True},
    "Broccoli": {"kcal_per_100_g": 34, "vegan": True, "vegetarian": True},
    "Butter": {"kcal_per_100_g": 717, "vegan": False, "vegetarian": True},
    "Cabbage": {"kcal_per_100_g": 25, "vegan": True, "vegetarian": True},
    "Carrot": {"kcal_per_100_g": 41, "vegan": True, "vegetarian": True},
    "Cauliflower": {"kcal_per_100_g": 25, "vegan": True, "vegetarian": True},
    "Celery": {"kcal_per_100_g": 16, "vegan": True, "vegetarian": True},
    "Cervelat": {"kcal_per_100_g": 260, "vegan": False, "vegetarian": False},
    "Chicken breast": {"kcal_per_100_g": 165, "vegan": False, "vegetarian": False},
    "Chickpeas": {"kcal_per_100_g": 364, "vegan": True, "vegetarian": True},
    "Cod": {"kcal_per_100_g": 82, "vegan": False, "vegetarian": False},
    "Corn": {"kcal_per_100_g": 86, "vegan": True, "vegetarian": True},
    "Cottage cheese": {"kcal_per_100_g": 98, "vegan": False, "vegetarian": True},
    "Couscous": {"kcal_per_100_g": 376, "vegan": True, "vegetarian": True},
    "Cream": {"kcal_per_100_g": 340, "kcal_per_100_ml": 340, "vegan": False, "vegetarian": True},
    "Cucumber": {"kcal_per_100_g": 15, "vegan": True, "vegetarian": True},
    "Dark chocolate": {"kcal_per_100_g": 546, "vegan": True, "vegetarian": True},
    "Egg": {"kcal_per_100_g": 155, "vegan": False, "vegetarian": True},
    "Eggplant": {"kcal_per_100_g": 25, "vegan": True, "vegetarian": True},
    "Emmental": {"kcal_per_100_g": 380, "vegan": False, "vegetarian": True},
    "Feta": {"kcal_per_100_g": 264, "vegan": False, "vegetarian": True},
    "Flour": {"kcal_per_100_g": 364, "vegan": True, "vegetarian": True},
    "Garlic": {"kcal_per_100_g": 149, "vegan": True, "vegetarian": True},
    "Gnocchi": {"kcal_per_100_g": 160, "vegan": True, "vegetarian": True},
    "Green beans": {"kcal_per_100_g": 31, "vegan": True, "vegetarian": True},
    "Gruyere": {"kcal_per_100_g": 413, "vegan": False, "vegetarian": True},
    "Ham": {"kcal_per_100_g": 145, "vegan": False, "vegetarian": False},
    "Hazelnuts": {"kcal_per_100_g": 628, "vegan": True, "vegetarian": True},
    "Honey": {"kcal_per_100_g": 304, "vegan": False, "vegetarian": True},
    "Leek": {"kcal_per_100_g": 61, "vegan": True, "vegetarian": True},
    "Lemon": {"kcal_per_100_g": 29, "vegan": True, "vegetarian": True},
    "Lentils": {"kcal_per_100_g": 353, "vegan": True, "vegetarian": True},
    "Lettuce": {"kcal_per_100_g": 15, "vegan": True, "vegetarian": True},
    "Milk": {"kcal_per_100_g": 64, "kcal_per_100_ml": 64, "vegan": False, "vegetarian": True},
    "Minced beef": {"kcal_per_100_g": 215, "vegan": False, "vegetarian": False},
    "Mozzarella": {"kcal_per_100_g": 280, "vegan": False, "vegetarian": True},
    "Mushroom": {"kcal_per_100_g": 22, "vegan": True, "vegetarian": True},
    "Mustard": {"kcal_per_100_g": 66, "vegan": True, "vegetarian": True},
    "Oat milk": {"kcal_per_100_g": 46, "kcal_per_100_ml": 46, "vegan": True, "vegetarian": True},
    "Oats": {"kcal_per_100_g": 389, "vegan": True, "vegetarian": True},
    "Olive oil": {"kcal_per_100_g": 884, "kcal_per_100_ml": 810, "vegan": True, "vegetarian": True},
    "Onion": {"kcal_per_100_g": 40, "vegan": True, "vegetarian": True},
    "Orange": {"kcal_per_100_g": 47, "vegan": True, "vegetarian": True},
    "Parmesan": {"kcal_per_100_g": 431, "vegan": False, "vegetarian": True},
    "Parsley": {"kcal_per_100_g": 36, "vegan": True, "vegetarian": True},
    "Pasta": {"kcal_per_100_g": 371, "vegan": True, "vegetarian": True},
    "Pear": {"kcal_per_100_g": 57, "vegan": True, "vegetarian": True},
    "Peas": {"kcal_per_100_g": 81, "vegan": True, "vegetarian": True},
    "Polenta": {"kcal_per_100_g": 362, "vegan": True, "vegetarian": True},
    "Pork": {"kcal_per_100_g": 242, "vegan": False, "vegetarian": False},
    "Potato": {"kcal_per_100_g": 77, "vegan": True, "vegetarian": True},
    "Puff pastry": {"kcal_per_100_g": 558, "vegan": True, "vegetarian": True},
    "Pumpkin": {"kcal_per_100_g": 26, "vegan": True, "vegetarian": True},
    "Quark": {"kcal_per_100_g": 73, "vegan": False, "vegetarian": True},
    "Quinoa": {"kcal_per_100_g": 368, "vegan": True, "vegetarian": True},
    "Raclette cheese": {"kcal_per_100_g": 357, "vegan": False, "vegetarian": True},
    "Raisins": {"kcal_per_100_g": 299, "vegan": True, "vegetarian": True},
    "Rapeseed oil": {"kcal_per_100_g": 884, "kcal_per_100_ml": 810, "vegan": True, "vegetarian": True},
    "Red kidney beans": {"kcal_per_100_g": 333, "vegan": True, "vegetarian": True},
    "Rice": {"kcal_per_100_g": 365, "vegan": True, "vegetarian": True},
    "Ricotta": {"kcal_per_100_g": 174, "vegan": False, "vegetarian": True},
    "Risotto rice": {"kcal_per_100_g": 358, "vegan": True, "vegetarian": True},
    "Salami": {"kcal_per_100_g": 378, "vegan": False, "vegetarian": False},
    "Salmon": {"kcal_per_100_g": 208, "vegan": False, "vegetarian": False},
    "Salt": {"kcal_per_100_g": 0, "vegan": True, "vegetarian": True},
    "Shrimp": {"kcal_per_100_g": 99, "vegan": False, "vegetarian": False},
    "Sour cream": {"kcal_per_100_g": 193, "vegan": False, "vegetarian": True},
    "Soy milk": {"kcal_per_100_g": 33, "kcal_per_100_ml": 33, "vegan": True, "vegetarian": True},
    "Soy sauce": {"kcal_per_100_g": 53, "kcal_per_100_ml": 53, "vegan": True, "vegetarian": True},
    "Spaetzli": {"kcal_per_100_g": 150, "vegan": False, "vegetarian": True},
    "Spaghetti": {"kcal_per_100_g": 371, "vegan": True, "vegetarian": True},
    "Spinach": {"kcal_per_100_g": 23, "vegan": True, "vegetarian": True},
    "Sugar": {"kcal_per_100_g": 400, "vegan": True, "vegetarian": True},
    "Tofu": {"kcal_per_100_g": 144, "vegan": True, "vegetarian": True},
    "Tomato": {"kcal_per_100_g": 18, "vegan": True, "vegetarian": True},
    "Tomato paste": {"kcal_per_100_g": 82, "vegan": True, "vegetarian": True},
    "Tomato sauce": {"kcal_per_100_g": 32, "kcal_per_100_ml": 32, "vegan": True, "vegetarian": True},
    "Tuna": {"kcal_per_100_g": 132, "vegan": False, "vegetarian": False},
    "Veal": {"kcal_per_100_g": 172, "vegan": False, "vegetarian": False},
    "Vegetable broth": {"kcal_per_100_g": 6, "kcal_per_100_ml": 6, "vegan": True, "vegetarian": True},
    "Vinegar": {"kcal_per_100_g": 18, "kcal_per_100_ml": 18, "vegan": True, "vegetarian": True},
    "Walnuts": {"kcal_per_100_g": 654, "vegan": True, "vegetarian": True},
    "White wine": {"kcal_per_100_g": 82, "kcal_per_100_ml": 82, "vegan": True, "vegetarian": True},
    "Yogurt": {"kcal_per_100_g": 61, "kcal_per_100_ml": 61, "vegan": False, "vegetarian": True},
    "Zucchini": {"kcal_per_100_g": 17, "vegan": True, "vegetarian": True},
}

UNITS = ("g", "ml")

#USER STORY 8: Combine identical ingredients that have the same unit
#this fucntion will combine the ingredients from a list
#ingredient_list is a list of dictionaries
def combine_items(ingredient_list):
    combined_list = []
    #combined_list = empty list to hold results

#the for statement is designed to work with a sequence of data items.
#When the statement executes, it iterates once for each item in the sequence
#each pass, the current dictionary is stored in the variable 'item'
    for item in ingredient_list:
        cleaned_name = item["name"].strip().capitalize()
        cleaned_unit = item["unit"].strip().lower()
        found = False
# found = False is a boolean Flag, has to be placed inside to reset found to false for each run through.
#if not reset, the program would stop adding ingredients to the list after the first duplicate was found
        for existing_item in combined_list:
            if existing_item["name"] == cleaned_name["name"] and existing_item["unit"] == cleaned_unit["unit"]:
                existing_item["quantity"] = existing_item["quantity"] + item["quantity"]
                found = True
                break
 # break - Stops the inner search as soon as the match is found (cleaner and faster)
# if found is still false, the ingredient is added to the list "not found = False" - if it was true it would mean that the ingredieent was found in our list
            if not found:
# new entry - "Alias versus Copy", new entry adds a new dictionary in a new place and appends it to the combined list, 
# instead of appending directly which would also overwrite the the amunts in the original recipe
# alias happens when two different variable names (or two different lists) point to the exact same object in your computer's memory
                new_entry = {
                    "name": cleaned_name,
                    "quantity": item["quantity"],
                    "unit": cleaned_unit,
                }
                combined_list.append(new_entry)
        
    return combined_list
#the combined list is now being cycled through again untill all ingredients have been added to "combined list"