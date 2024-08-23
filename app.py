import streamlit as stl

# Define the recipes and their ingredients
recipes = {
    "Spaghetti Bolognese": ["Ground beef", "Onions", "Garlic", "Tomato sauce", "Spaghetti", "Salt", "Pepper", "Olive oil"],
    "Chicken Curry": ["Chicken breast", "Onions", "Garlic", "Ginger", "Curry powder", "Coconut milk", "Salt", "Pepper"],
    "Vegetable Stir Fry": ["Bell peppers", "Broccoli", "Carrots", "Garlic", "Soy sauce", "Sesame oil", "Rice"],
    "Chocolate Cake": ["Flour", "Sugar", "Cocoa powder", "Baking powder", "Eggs", "Milk", "Butter", "Vanilla extract"],
    "Caesar Salad": ["Romaine lettuce", "Croutons", "Parmesan cheese", "Caesar dressing", "Chicken breast (optional)", "Anchovies (optional)"]
}

# Set the title of the Streamlit app
stl.title("Cooking Application")

# Display the list of recipes
stl.header("Select a Recipe :)")
recipe_name = stl.selectbox("Choose a recipe:", list(recipes.keys()))

# Display the ingredients for the selected recipe
if recipe_name:
    stl.header(f"Ingredients for {recipe_name}")
    ingredients = recipes[recipe_name]
    for ingredient in ingredients:
        stl.write(f"- {ingredient}")

# Run the Streamlit app
if __name__ == "__main__":
    stl.write("Welcome to the Cooking Application!")
