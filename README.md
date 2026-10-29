# 🍲 Recipe Manager — Group G

A Python console application to store recipes, scale portions, create shopping lists, manage pantry inventory, and view nutritional and dietary information.

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Problem and Motivation](#problem-and-motivation)
- [User Role](#user-role)
- [Console Interaction](#console-interaction)
- [Features](#features)
- [User Stories and Acceptance Criteria](#user-stories-and-acceptance-criteria)
- [Ingredient Dataset](#ingredient-dataset)
- [Unit and Scaling Rules](#unit-and-scaling-rules)
- [Responsibilities](#responsibilities)

## Project Overview

The Recipe Manager is a menu-driven Python console application that helps users organize recipes, plan shopping, and keep track of ingredients at home.

## Problem and Motivation

Home cooks often struggle with:

- Scattered recipe notes
- Difficulty scaling portions
- Duplicate ingredient purchases
- Unclear pantry inventory
- Missing calorie or dietary information

The Recipe Manager addresses these problems through a unified, easy-to-use console interface.

## User Role

The application has one role: **User**.

Users can manage recipes, shopping lists, and pantry items, and view nutritional and dietary information.

## Console Interaction

The application provides the following menu options:

1. View recipes
2. Add recipe
3. Search recipes
4. View recipe details
5. Scale recipe
6. Create shopping list
7. Manage pantry
8. Save / Load data
9. Exit

## Features

| Area | Features |
| --- | --- |
| Recipes | Add, view, search, and scale recipes |
| Shopping lists | Create lists for multiple recipes, combine duplicate ingredients, and edit items |
| Pantry | Track inventory and deduct pantry quantities from shopping lists |
| Cooking | Find recipes that can be prepared using pantry stock |
| Nutrition | Display calorie information |
| Dietary information | Determine vegetarian and vegan status |
| Data storage | Save and load all application data |

## User Stories and Acceptance Criteria

### US1 — Add Recipe

**Responsible:** Karolina

**User story:**  
As a user, I want to add a recipe with its ingredients, quantities, and portion yield so that I can save it and scale it later.

**Acceptance criteria:**

- The user can enter a recipe name, ingredients, quantities, and portion yield.
- Ingredients must be chosen from the predefined ingredient list.
- The recipe is saved and appears in the recipe list.
- Invalid inputs, such as empty names or negative quantities, trigger an error message.

### US2 — View Recipes

**Responsible:** Karolina

**User story:**  
As a user, I want to view my saved recipes so that I know which recipes are available.

**Acceptance criteria:**

- All saved recipes are displayed.
- If no recipes exist, the user receives a message indicating that the list is empty.

### US3 — Search Recipes

**Responsible:** Karolina

**User story:**  
As a user, I want to search for a recipe by name so that I can quickly find the one I am looking for.

**Acceptance criteria:**

- Partial matches are displayed.
- The search is case-insensitive.
- If no recipes match the search term, the user receives a message.

### US4 — View Recipe Details

**Responsible:** Sebastian

**User story:**  
As a user, I want to view a recipe's ingredients, quantities, and portion yield, and see which ingredients I already have in the pantry, so that I know what I need to prepare it.

**Acceptance criteria:**

- All recipe details are displayed correctly.
- The user is informed of any recipe ingredients already available in the pantry.

### US5 — Scale Recipe

**Responsible:** Sebastian

**User story:**  
As a user, I want to specify how many portions I want to cook so that ingredient quantities adjust automatically.

**Acceptance criteria:**

- Quantities scale proportionally based on the requested number of portions.
- Rounding rules are applied consistently.
- Invalid portion inputs trigger an error message.

### US6 — Create Shopping List

**Responsible:** Niels

**User story:**  
As a user, I want to create a shopping list for one or multiple recipes so that I know which ingredients I need to buy.

**Acceptance criteria:**

- Ingredients from the selected recipes are collected.
- Quantities are summed correctly.
- The shopping list is saved.

### US7 — Exclude Pantry Items from Shopping List

**Responsible:** Kenan

**User story:**  
As a user, I want the option to deduct pantry quantities from my shopping list so that I do not buy too much or purchase duplicate items.

**Acceptance criteria:**

- Pantry quantities can be deducted from the shopping list.
- Items fully covered by pantry stock are removed from the shopping list.
- Items partially covered by pantry stock have their quantities adjusted correctly.

### US8 — Combine Recipes

**Responsible:** Niels

**User story:**  
As a user, I want ingredients that appear in multiple recipes to be combined so that my shopping list does not contain duplicates.

**Acceptance criteria:**

- Identical ingredients with the same unit are merged.
- Their quantities are summed correctly.

### US9 — Edit Shopping List

**Responsible:** Niels

**User story:**  
As a user, I want to add, remove, or update shopping list items so that I can adjust the list to my needs.

**Acceptance criteria:**

- Items can be added, removed, or updated.
- Invalid inputs trigger an error message.

### US10 — View Calories

**Responsible:** Kenan

**User story:**  
As a user, I want to see how many calories are in a dish so that I know how much I am consuming.

**Acceptance criteria:**

- Calories are calculated using the predefined ingredient dataset.

### US11 — Save and Load Data

**Responsible:** All team members — shared responsibility

**User story:**  
As a user, I want my recipes, shopping lists, and pantry inventory to be saved to and loaded from a file so that my data remains available when I restart the application.

**Acceptance criteria:**

- All application data is saved correctly.
- Loading restores the data fully.
- Corrupted files trigger an error message.

### US12 — Determine Vegetarian or Vegan Status

**Responsible:** Sebastian

**User story:**  
As a user, I want to know whether a recipe is vegetarian, vegan, or neither so that I can choose recipes according to my dietary needs.

**Acceptance criteria:**

- The classification is based on the predefined ingredient dataset.
- Unknown ingredients trigger a warning.

### US13 — Manage Pantry

**Responsible:** Kenan

**User story:**  
As a user, I want to add and remove pantry items so that I can see what I have at home.

**Acceptance criteria:**

- Quantities are stored correctly.
- Removing more than the available quantity triggers an error message.

### US14 — Cook Recipes Without Shopping

**Responsible:** Kenan

**User story:**  
As a user, I want to find recipes I can cook using my pantry stock so that I can start cooking without going shopping.

**Acceptance criteria:**

- Recipes are shown only if all required ingredients are available in sufficient quantities.
- Recipes with missing ingredients or insufficient quantities are excluded.

## Ingredient Dataset

| Ingredient | kcal per 100 g | Vegan | Vegetarian |
| --- | ---: | :---: | :---: |
| Sugar | 400 | Yes | Yes |
| Milk | 60 | No | Yes |
| Egg | 155 | No | Yes |
| Butter | 720 | No | Yes |
| Tomato | 18 | Yes | Yes |

## Unit and Scaling Rules

### Units

- Units are **not automatically converted**, for example, from `g` to `kg`.
- Ingredients must have the **same unit** to be combined.

### Scaling Formula

```python
new_quantity = old_quantity * (new_portions / old_portions)
```

## Responsibilities

| Team member | User stories | Main areas |
| --- | --- | --- |
| Karolina | US1, US2, US3 | Add, view, and search recipes |
| Sebastian | US4, US5, US12 | Recipe details, scaling, and dietary classification |
| Niels | US6, US8, US9 | Shopping list creation, combining ingredients, and editing |
| Kenan | US7, US10, US13, US14 | Pantry management, pantry deductions, calories, and available recipes |
| All team members | US11 | Saving and loading data |