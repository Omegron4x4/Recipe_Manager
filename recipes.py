#Default recipes
def get_default_recipes():
  return [{"name": "Classic Swiss Roesti", "portions": 2, "ingredients": [{"name": "Potato", "quantity": 500, "unit":"g"},{"name": "Rapeseed oil", "quantity": 30, "unit": "ml"}, {"name": "Onion", "quantity": 80, "unit": "g"}, {"name": "Salt", "quantity": 5, "unit": "g"},],}

# USER Story 1
def add_recipe(recipes, name, portions, ingredient_list):
  #Validate and add a new recipe dictionary to the recipe dictionary to the recipes list.#
  cleaned_name = name.strip()
  if cleaned_name == "":
    return None
  if portions <=0:
    return None
  #len checks whether the ingredient list is empty so the funtion can stop before saving a recipe without ingredients.
    if len(ingredients_list) == 0:
    return None
    
  recipe = {"name": cleaned_name,"portions": portions,"ingredients": ingredient_list}
  recipes.append(recipe)
  return recipe
  
def list_recipes(recipes):
  #Return a shallow copy of the saved recipes list
  #Prevents callers from accidentally modifying the original list structure
  copied_recipes = []
  for recipe in recipes:
    copied_recipes.append(recipe)
  return copied_recipes

def search_recipes(recipes, query):
  #Return recipes whose name contains the search query (case-insensitive)
  #Return an empty list if the search text is blank.
  cleaned_query = receipes.strip().lower()
  for recipe["name"] in cleaned_query()
