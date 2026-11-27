#Default recipes
def get_default_recipes():
  return [{"name": "Classic Swiss Roesti",
           "portions": 2,
           "ingredients": [
             {"name": "Potato", "quantity": 500, "unit":"g"},
             {"name": "Rapeseed oil", "quantity": 30, "unit": "ml"},
             {"name": "Onion", "quantity": 80, "unit": "g"},
             {"name": "Salt", "quantity": 5, "unit": "g"},],},
         
          {"name": "Tomato Basil Pasta",
           "portions": 2,
           "ingredients": [
             {"name": "Spaghetti", "quantity": 200, "unit": "g"},
             {"name": "Tomato sauce", "quantity": 250, "unit": "ml"},
             {"name": "Olive oil", "quantity": 20, "unit": "ml"},
             {"name": "Garlic", "quantity": 10, "unit": "g"},
             {"name": "Basil", "quantity": 10, "unit": "g"},],}, 
          
          {"name": "Lentil Vegetable Soup",
           "portions": 4,
           "ingredients": [
             {"name": "Lentils", "quantity": 200, "unit": "g"},
             {"name": "Carrot", "quantity": 150, "unit": "g"},
             {"name": "Potato", "quantity": 200, "unit": "g"},
             {"name": "Leek", "quantity": 100, "unit": "g"},
             {"name": "Vegetable broth", "quantity": 800, "unit": "ml"},
             {"name": "Olive oil", "quantity": 15, "unit": "ml"},],},

          {"name": "Swiss Cheese Fondue",
           "portions": 2,
           "ingredients": [
             {"name": "Gruyere", "quantity": 200, "unit": "g"},
             {"name": "Emmental", "quantity": 200, "unit": "g"},
             {"name": "White wine", "quantity": 150, "unit": "ml"},
             {"name": "Bread", "quantity": 300, "unit": "g"},
             {"name": "Garlic", "quantity": 5, "unit": "g"},],},
            

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
