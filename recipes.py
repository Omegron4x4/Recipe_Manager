def add_recipe(recipes, name, portions, ingredient_list):
  cleaned_name = name.strip()
  if cleaned_name == "":
    return None
  if portions <=0:
    return None
  recipe = {"name": cleaned_name,"portions": portions,"ingredients": ingredient_list}
  recipes.append(recipe)
  return recipe
  
def list_recipes(recipes):
  copied_recipes = []
  for recipe in recipes:
    copied_recipes.append(recipe)
  return copied_recipes

def search_recipes(recipes, query):
  cleaned_query = receipes.strip().lower()
  for recipe["name"] in cleaned_query()
