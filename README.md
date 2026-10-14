🍲 Recipe Manager – Group G

A Python console application for managing recipes, scaling portions, generating shopping lists, tracking pantry inventory, and viewing nutritional information.

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

📚 User Stories

US1 – Add Recipe
As a user, I want to add a recipe with ingredients, quantities, and yield in portions
so that I can save it and scale it later.

US2 – View Recipes
As a user, I want to view my saved recipes
so that I know which recipes are available.

US3 – Search Recipes
As a user, I want to search for recipes by name
so that I can quickly find the one I need.

US4 – View Recipe Details
As a user, I want to see the ingredients, quantities, and portion yield of a recipe
so that I know what is required to prepare it.

US5 – Scale Recipe
As a user, I want to specify how many portions I want to cook
so that ingredient quantities adjust automatically.

US6 – Create Shopping List
As a user, I want to create a shopping list for one or multiple recipes
so that I know which ingredients I need to buy.

US7 – Combine Ingredients
As a user, I want ingredients that appear in multiple recipes to be combined
so that my shopping list does not contain duplicates.

US8 – Edit Shopping List
As a user, I want to add or remove items from my shopping list
so that I can adjust it to my needs.

US9 – View Calories
As a user, I want to see how many calories a dish contains
so that I know how much I am consuming.

US10 – Save & Load Data
As a user, I want my recipes and shopping lists to be saved and loaded from a file
so that my data persists after restarting the application.

US11 – Vegetarian/Vegan Classification
As a user, I want to know if a recipe is vegetarian or vegan
so that I can choose recipes that fit my dietary needs.

US12 – Manage Pantry
As a user, I want to add and remove items from my pantry
so that I can track what I already have at home.

US13 – Exclude Pantry Items from Shopping List
As a user, I don’t want items I already have in my pantry to appear on my shopping list
so that I don’t buy duplicates.

US14 – Cookable Recipes from Pantry
As a user, I want to see which recipes I can cook entirely from my pantry
so that I can start cooking without shopping.

✔️ Acceptance Criteria

US1 – Add Recipe
Given I am in the recipe menu

When I enter a name, ingredients, quantities, and portion yield

Then the recipe is saved and appears in the recipe list

Invalid inputs (empty name, negative quantities) trigger an error message

US2 – View Recipes
All recipes are displayed

Empty list → message shown

US3 – Search Recipes
Partial matches are shown

Search is case‑insensitive

No matches → message shown

US4 – View Recipe Details
All details are displayed correctly

Invalid recipe name → error message

US5 – Scale Recipe
Quantities scale proportionally

Rounding rules defined in README

Invalid portion input → error message

US6 – Create Shopping List
Ingredients from selected recipes are collected

Quantities are summed correctly

List is saved

US7 – Combine Ingredients
Identical ingredients are merged

Units must match

US8 – Edit Shopping List
Items can be added or removed

Invalid inputs → error message

US9 – View Calories
Calories calculated using predefined dataset

Missing calorie data → warning message

US10 – Save & Load Data
Data saved to file

Loading restores all data

Corrupted file → error message

US11 – Vegetarian/Vegan Classification
Classification uses predefined dataset

Unknown ingredients → warning message

US12 – Manage Pantry
Quantities stored correctly

Removing more than available → error message

US13 – Exclude Pantry Items from Shopping List
Pantry quantities deducted

Fully covered items removed

Partial quantities adjusted

US14 – Cookable Recipes from Pantry
Recipe shown only if all ingredients exist in sufficient quantity

Missing ingredients → recipe excluded

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
