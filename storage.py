
# Use pickle module to serialize (save) and deserialize (load)
import pickle
#load the pre defined pantry and recipes for program testing
from pantry import get_default_pantry
from recipes import get_default_recipes

DEFAULT_DATA_FILE = "data.dat"
#needs to use data from pantry and recipes

#will run if no data file is found when the programs is started up
def empty_data():
    # creates a clean default data structure for the application - with 3 keys- recipes, pantry and shopping list
    # Preloads the predefined recipes and pantry 
    # determines the 3 keys
    return {
        "recipes": get_default_recipes(),
        "pantry": get_default_pantry(),
        "shopping_lists": [],
    }

#define load and save data


#exception handlers:
except FileNotFoundError:
 # first time you run the program to load the starter data
     starter_data = empty_data()
    save_data(starter_data, filename)
    return starter_data
except OSError:
    print(f"Error: Could not load data from '{filename}'.")
    return None
except EOFError:
    print(f"Error: Data file '{filename}' is empty or corrupted.")
    return None

