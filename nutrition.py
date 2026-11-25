# nutrition.py
# Responsible: Kenan (US10)

from ingredients import INGREDIENTS


def calculate_calories(recipe):
    total_kcal = 0.0

    for item in recipe["ingredients"]:
        name = item["name"]
        unit = item["unit"]

        if name not in INGREDIENTS:
            return None

        info = INGREDIENTS[name]
        rate_key = "kcal_per_100_" + unit

        if rate_key not in info:
            return None

        rate = info[rate_key]
        total_kcal = total_kcal + (item["quantity"] / 100.0) * rate

    return round(total_kcal, 2)


if __name__ == "__main__":
    sample_recipe = {
        "name": "Tomato Soup",
        "portions": 2,
        "ingredients": [
            {"name": "Tomato", "quantity": 300, "unit": "g"},
            {"name": "Butter", "quantity": 20, "unit": "g"}
        ]
    }
    print("Total calories:", calculate_calories(sample_recipe))
