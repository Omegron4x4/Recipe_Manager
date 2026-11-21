def add_recipe(recipes, name, portions, ingredient_list):
  cleaned_name = name.strip()
  if cleaned_name == "":
    return None
  if portions <=0:
    return None
  recipe = {"name": cleaned_name,"portions": portions,"ingredients": ingredient_list}
  recipes.append(recipe)
  return recipe
  
