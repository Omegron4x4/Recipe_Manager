# recipe_details.py
# Responsible: Sebastian (US4, US5, US12)

from ingredients import INGREDIENTS, combine_items


def get_recipe_details(recipe, pantry):
    # Return recipe ingredients together with how much is available in the pantry
    # Checks each merged ingredient against pantry items with the same name and unit
    details = []
    # Combine duplicate ingredients in the recipe first
    merged_ingredients = combine_items(recipe["ingredients"])

    for item in merged_ingredients:
        available_qty = 0

        # Check if the same ingredient and unit exist in the pantry
        for pantry_item in pantry:
            if pantry_item["name"] == item["name"] and pantry_item["unit"] == item["unit"]:
                available_qty = pantry_item["quantity"]

        detail_entry = {
            "name": item["name"],
            "quantity": item["quantity"],
            "unit": item["unit"],
            "available": available_qty,
        }
        details.append(detail_entry)

    return details


def scale_recipe(recipe, new_portions):
    # Scale ingredient quantities proportionally to new_portions
    # Returns a new scaled recipe dictionary without changing the original recipe
    old_portions = recipe["portions"]

    # Prevent division by zero or negative portion counts
    if old_portions <= 0 or new_portions <= 0:
        print("Error: Portions must be greater than 0.")
        return None

    factor = new_portions / old_portions
    scaled_items = []
    merged_ingredients = combine_items(recipe["ingredients"])

    for item in merged_ingredients:
        # Round scaled quantities to whole numbers
        new_qty = int(round(item["quantity"] * factor))
        if new_qty > 0:
            scaled_entry = {
                "name": item["name"],
                "quantity": new_qty,
                "unit": item["unit"],
            }
            scaled_items.append(scaled_entry)

    # Return a new dictionary so the original recipe stays unchanged
    scaled_recipe = {
        "name": recipe["name"],
        "portions": new_portions,
        "ingredients": scaled_items,
    }
    return scaled_recipe


def classify_recipe(recipe):
    # Check if a recipe is Vegan, Vegetarian, or Neither
    # Looks up every ingredient in the predefined INGREDIENTS dataset
    is_vegan = True
    is_vegetarian = True

    for item in recipe["ingredients"]:
        name = item["name"]

        # Warn if an ingredient is missing from the predefined dataset
        if name not in INGREDIENTS:
            return "Unknown (missing dietary data for " + name + ")"

        info = INGREDIENTS[name]
        if not info["vegan"]:
            is_vegan = False
        if not info["vegetarian"]:
            is_vegetarian = False

    if is_vegan:
        return "Vegan"
    elif is_vegetarian:
        return "Vegetarian"
    else:
        return "Neither vegetarian nor vegan"


if __name__ == "__main__":
    # Quick manual check when running this file directly
    sample_recipe = {
        "name": "Tomato Soup",
        "portions": 2,
        "ingredients": [
            {"name": "Tomato", "quantity": 300, "unit": "g"},
            {"name": "Butter", "quantity": 25, "unit": "g"},
        ],
    }
    sample_pantry = [{"name": "Tomato", "quantity": 150, "unit": "g"}]

    print("Details:", get_recipe_details(sample_recipe, sample_pantry))
    print("Scaled to 3 portions:", scale_recipe(sample_recipe, 3))
    print("Dietary status:", classify_recipe(sample_recipe))
