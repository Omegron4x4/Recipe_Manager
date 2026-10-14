🍲 Recipe Manager – Group G


📑 Table of Contents
Project Overview

Problem & Motivation

User Role

Console Interaction

Features

User Stories

Acceptance Criteria

Ingredient Dataset

Unit & Scaling Rules

Responsibilities

🧩 Project Overview

The Recipe Manager is a Python console application designed to help users store recipes, scale portions, create shopping lists, manage pantry inventory, and access nutritional and dietary information.

🎯 Problem & Motivation

Home cooks often struggle with:

scattered recipe notes

difficulty scaling portions

duplicate ingredient purchases

unclear pantry inventory

missing calorie or dietary information

The Recipe Manager solves these issues through a unified, easy‑to‑use console interface.

👥 User Role

User  
The only role in the system.
Users can manage recipes, shopping lists, pantry items, and view nutritional information.

💻 Console Interaction

The application is menu‑driven:

View recipes

Add recipe

Search recipe

View recipe details

Scale recipe

Create shopping list

Manage pantry

Save / Load data

Exit

🧰 Features

Add, view, search, and scale recipes

Create shopping lists for multiple recipes

Combine duplicate ingredients

Edit shopping lists

Track pantry inventory

Exclude pantry items from shopping lists

Show which recipes can be cooked from pantry stock

Display calorie information

Determine vegetarian/vegan status

Save and load all data from file

📚 User Stories & Acceptance Criteria

US1 – Add Recipe
As a user, I want to add a recipe with its ingredients, quantities, and portion yield so that I can save it and scale it later.

Acceptance Criteria:  
The user can enter a recipe name, ingredients, quantities, and portion yield, and the recipe is saved and appears in the recipe list. Ingredients must be chosen from the pre defined list. Invalid inputs such as empty names or negative quantities must trigger an error message. 

US2 – View Recipes
As a user, I want to view my saved recipes so that I know which recipes are available.

Acceptance Criteria:  
All saved recipes are displayed, and if no recipes exist, the user receives a message indicating that the list is empty.

US3 – Search Recipes
As a user, I want to search for a recipe by name so that I can quickly find the one I am looking for.

Acceptance Criteria:  
Partial matches are shown, the search is case‑insensitive, and if no recipe matches the search term, the user receives a message.

US4 – View Recipe Details
As a user, I want to view the ingredients, quantities, and portion yield and see what i already have in the pantry of a recipe so that I know what I need to prepare it.

Acceptance Criteria:  
All recipe details are displayed correctly and the user is informed of any ingredients already in the pantry for this recipe.

US5 – Scale Recipe
As a user, I want to specify how many portions I want to cook so that the ingredient quantities adjust automatically.

Acceptance Criteria:  
Quantities scale proportionally based on the new portion amount, rounding rules are applied consistently, and invalid portion inputs trigger an error message.

US6 – Create Shopping List
As a user, I want to create a shopping list for one or multiple recipes so that I know which ingredients I need to buy. 

Acceptance Criteria:  
Ingredients from selected recipes are collected, quantities are summed correctly, and the shopping list is saved.

US7 – Exclude Pantry Items from Shopping List
As a user, i want the option to discount the pantry from my shopping list so that I don’t buy too much or duplicates.

Acceptance Criteria:  
Pantry quantities can be deducted from the shopping list, items fully covered by pantry stock are removed, and partial quantities are adjusted correctly.

US8 – Combine Recipes
As a user, I want ingredients that appear in multiple recipes to be combined so that my shopping list does not contain duplicates.

Acceptance Criteria:  
Identical ingredients are merged in the list with the units.

US9 – Edit Shopping List
As a user, I want to add, remove or update the items from my shopping list so that I can adjust it to my needs.

Acceptance Criteria:  
Items can be added, removed or updated, and invalid inputs result in an error message.

US10 – View Calories
As a user, I want to see how many calories are in a dish so that I know how much I am consuming.

Acceptance Criteria:  
Calories are calculated using a predefined ingredient dataset.

No Chose here US11 – Save and Load Data
As a user, I want my recipes and shopping lists to be saved and loaded from a file so that my data is still available when I restart the application.

Acceptance Criteria:  
All data is saved correctly, loading restores the data fully, and corrupted files trigger an error message.

US12 – Determine if a Recipe Is Vegetarian or Vegan
As a user, I want to know if a recipe is vegetarian, vegan, or not so that I can pick the right recipe according to my dietary needs.

Acceptance Criteria:  
The classification is based on a predefined ingredient dataset, and unknown ingredients trigger a warning.

US13 – Manage Pantry
As a user, I want to be able to add and remove items from my pantry so that I can see what I have at home.

Acceptance Criteria:  
Quantities are stored correctly, and removing more than what is available triggers an error message.

US14 – Cook Recipes Without Shopping
As a user, I want to be able to cook a recipe without going shopping so that I can start cooking straight away.

Acceptance Criteria:  
Recipes are shown only if all required ingredients exist in sufficient quantity in the pantry, and recipes missing ingredients are excluded.

🍏 Ingredient Dataset

Ingredient	kcal/100g	Vegan	Vegetarian

Sugar	400	Yes	Yes

Milk	60	No	Yes

Egg	155	No	Yes

Butter	720	No	Yes

Tomato	18	Yes	Yes


📐 Unit & Scaling Rules

Units are not automatically converted (e.g., g ↔ kg).

Ingredients must share the same unit to be combined.

Scaling formula:

Code
new_quantity = old_quantity * (new_portions / old_portions)

🧑‍🏫 Responsibilities

(Three substantive stories per student. US10 and menu navigation do not count.)

Code
### Student A:
- US …
- US …
- US …

### Student B:
- US …
- US …
- US …

### Student C:
- US …
- US …
- US …

### Student D:
- US …
- US …
- US …
