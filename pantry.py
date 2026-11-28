# pantry.py
# Responsible: Kenan (US7, US13, US14)


from ingredients import combine_items, make_item
from recipe_details import scale_recipe


def add_pantry_item(pantry, name, quantity, unit):
    if quantity <= 0:
        return False

    new_item = make_item(name, quantity, unit)
    pantry.append(new_item)

    merged_pantry = combine_items(pantry)
    pantry.clear()
    for item in merged_pantry:
        pantry.append(item)

    return True


def remove_pantry_item(pantry, name, quantity, unit):
    if quantity <= 0:
        return False

    cleaned_name = name.strip().capitalize()
    cleaned_unit = unit.strip().lower()

    for item in pantry:
        if item["name"] == cleaned_name and item["unit"] == cleaned_unit:
            if quantity > item["quantity"]:
                return False

            item["quantity"] = int(round(item["quantity"] - quantity))
            if item["quantity"] == 0:
                pantry.remove(item)
            return True

    return False


def deduct_pantry(shopping_items, pantry):
    # Create an independent copy of pantry items so we do not mutate the original pantry
    updated_pantry = []
    for p_item in pantry:
        copied_p = {
            "name": p_item["name"],
            "quantity": p_item["quantity"],
            "unit": p_item["unit"]
        }
        updated_pantry.append(copied_p)

    to_buy = []
    merged_shopping = combine_items(shopping_items)

    for s_item in merged_shopping:
        needed = s_item["quantity"]

        for p_item in updated_pantry:
            if p_item["name"] == s_item["name"] and p_item["unit"] == s_item["unit"]:
                if p_item["quantity"] >= needed:
                    p_item["quantity"] = int(round(p_item["quantity"] - needed))
                    needed = 0
                else:
                    needed = int(round(needed - p_item["quantity"]))
                    p_item["quantity"] = 0

        if needed > 0:
            buy_entry = {
                "name": s_item["name"],
                "quantity": needed,
                "unit": s_item["unit"]
            }
            to_buy.append(buy_entry)

    # Keep only pantry items that still have quantity > 0
    final_pantry = []
    for p_item in updated_pantry:
        if p_item["quantity"] > 0:
            final_pantry.append(p_item)

    return to_buy, final_pantry


def find_cookable_recipes(recipes, pantry, desired_portions):
    cookable = []

    for recipe in recipes:
        scaled = scale_recipe(recipe, desired_portions)
        missing_items, _ = deduct_pantry(scaled["ingredients"], pantry)
        if len(missing_items) == 0 and len(scaled["ingredients"]) > 0:
            cookable.append(scaled)

    return cookable


if __name__ == "__main__":
    test_pantry = []
    add_pantry_item(test_pantry, "Tomato", 300, "g")
    add_pantry_item(test_pantry, "Butter", 50, "g")
    sample_recipes = [{
        "name": "Tomato Soup",
        "portions": 2,
        "ingredients": [
            {"name": "Tomato", "quantity": 200, "unit": "g"},
            {"name": "Butter", "quantity": 20, "unit": "g"}
        ]
    }]
    print("Cookable for 3 portions:", find_cookable_recipes(sample_recipes, test_pantry, 3))
    print("Cookable for 4 portions:", find_cookable_recipes(sample_recipes, test_pantry, 4))

#added by Niels - get_default_pantry - naming for the storage file

def get_default_pantry():
    # add enough ingredients to cook 2 portions Rosti and Cheese Fondue for program testing
    #create an empty list
    default_pantry = []

    # Rosti 2 portions
    add_pantry_item(default_pantry, "Potato", 500, "g")
    add_pantry_item(default_pantry, "Rapeseed oil", 30, "ml")
    add_pantry_item(default_pantry, "Onion", 80, "g")
    add_pantry_item(default_pantry, "Salt", 5, "g")

    # Fondue (2 portions)
    add_pantry_item(default_pantry, "Gruyere", 200, "g")
    add_pantry_item(default_pantry, "Emmental", 200, "g")
    add_pantry_item(default_pantry, "White wine", 150, "ml")
    add_pantry_item(default_pantry, "Bread", 300, "g")
    add_pantry_item(default_pantry, "Garlic", 5, "g")

    return default_pantry