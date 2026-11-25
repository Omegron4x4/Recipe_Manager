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
- [Project Requirements Verification (Console Input, Data Validation, File Processing)](#Project-Requirements-Verification)

## Project Overview

The Recipe Manager is a menu-driven Python console application that helps users organize recipes, plan shopping, and keep track of ingredients at home.

## Problem and Motivation

Problem: Home cooks frequently rely on scattered notes, miscalculate ingredient quantities when adjusting servings, buy duplicate items already stored at home, and lack clear visibility into meal calories or vegetarian/vegan suitability. 

Scenario: Before cooking or grocery shopping, a user launches the console application, adds or searches recipes, scales portions to the desired yield, checks available pantry stock, generates a deduplicated shopping list, and saves all application data to disk for future sessions.

## User Role

User Role: Home Cook (User) — Manages personal recipes, scales serving sizes, maintains pantry inventory, builds and edits shopping lists, and checks nutritional/dietary details.

Console Interaction: Users interact via numbered menu options (1–9). Surrounding whitespace is trimmed and text commands are handled case-insensitively. Invalid menu entries display a clear warning message and re-prompt without terminating the program.
1. View recipes
2. Add recipe
3. Search recipes
4. View recipe details
5. Scale recipe
6. Create / edit shopping list
7. Manage pantry
8. Save / Load data
9. Exit

## Features

| Area | Features |
| --- | --- |
| Recipes | Add recipes using predefined ingredients, list saved recipes, search case-insensitively, view details with pantry comparison, and scale portions proportionally. |
| Shopping lists | Create uniquely named lists across multiple recipes, merge identical ingredients sharing the same unit, deduct pantry stock, and add/update/remove items. |
| Pantry | Track home ingredient stock, add/remove quantities with validation, and filter recipes cookable solely from current pantry inventory. |
| Cooking |Identify recipes whose full ingredient requirements (name, unit, and quantity) are met by current pantry stock. |
| Nutrition | Calculate total and per-portion kcal from the predefined ingredient dataset with warnings for unknown ingredients or non-gram units. |
| Dietary information | Classify recipes as Vegan, Vegetarian, or Neither based on the predefined dataset. |
| Data storage | Save and load shopping lists, and pantry data across sessions |

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
As a user, I want to view a recipe's ingredients, quantities, units, portion yield, and pantry availability status, so that I know which items are already at home and what is missing.

**Acceptance criteria:**

- Given a valid recipe selection, when details are viewed, the output shows the recipe name, portion yield, and each ingredient with its required quantity and unit.
- Comparing each ingredient (matching name and unit) against pantry stock clearly marks items as "Available" (pantry ≥ required), "Partially available" (0 < pantry < required, showing available quantity), or "Missing", and handles invalid selections or empty lists without a traceback.

### US5 — Scale Recipe

**Responsible:** Sebastian

**User story:**  
As a user, I want to enter a target number of portions so that all ingredient quantities scale proportionally according to a consistent rounding rule.

**Acceptance criteria:**

- Using new_quantity = old_quantity * (new_portions / old_portions) without automatic unit conversion (e.g., 2 portions with 150 g Sugar scaled to 5 portions gives 375.00 g Sugar).
- All scaled quantities are rounded consistently to 2 decimal places ( round(value, 2) ) without mutating the saved recipe unless explicitly saved.
- Given 0, a negative number (-2), a decimal (1.5), or non-numeric text ("abc"), an error message is shown and the user is re-prompted without a traceback.

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
- Items whose stock reaches zero are removed from the pantry.

### US8 — Combine Ingredients

**Responsible:** Niels

**User story:**  
As a user, I want ingredients that appear in multiple recipes to be combined so that my shopping list does not contain duplicates.

**Acceptance criteria:**

- Identical ingredients with the same unit are merged.
- Their quantities are summed correctly.

### US9 — Edit Shopping List for Recipes

**Responsible:** Niels

**User story:**  
As a user, I want to add, remove, or update shopping list items so that I can adjust the Recipe-list to my needs.

**Acceptance criteria:**

- Items can be added, removed, or updated.
- Invalid inputs trigger an error message.
- Each list must have one unique name for order

### US10 — View Calories

**Responsible:** Kenan

**User story:**  
As a user, I want to see how many calories are in a dish so that I know how much I am consuming.

**Acceptance criteria:**

- Calories are calculated using the predefined ingredient dataset.

### US11 — Save and Load Data

**Responsible:** All team members — shared responsibility

**User story:**  
As a user, I want all recipes, shopping lists, and pantry inventory to be persisted to structured files and restored upon loading, so that no data is lost between sessions.

**Acceptance criteria:**

- Saving writes all recipes, shopping lists, and pantry items to disk and displays a confirmation message.
- Loading a valid data file restores recipes, shopping lists, and pantry items completely.
- Missing or corrupted/malformed files display a clear error message, keep existing inmemory data intact, and never raise a Python traceback.

### US12 — Determine Vegetarian or Vegan Status

**Responsible:** Sebastian

**User story:**  
As a user, I want to see whether a recipe is Vegan, Vegetarian, or Neither based on the predefined ingredient dataset, so that I can filter dishes according to dietary restrictions..

**Acceptance criteria:**

- All Vegan = Yes → "Vegan"; all Vegetarian = Yes with at least one "Vegetarian (not vegan)"; any known Vegan = No → Vegetarian = No → "Neither vegetarian nor vegan".
- Any ingredient missing from the dataset prints a warning ( Warning: Unknown ingredient '<name>' ) and marks the status as "Unknown / Incomplete" without crashing.


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
