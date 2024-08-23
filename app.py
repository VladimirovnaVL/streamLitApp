import streamlit as st

# Define the recipes and their ingredients
recipes = {
    "Spaghetti Bolognese": ["Ground beef", "Onions", "Garlic", "Tomato sauce", "Spaghetti", "Salt", "Pepper", "Olive oil"],
    "Chicken Curry": ["Chicken breast", "Onions", "Garlic", "Ginger", "Curry powder", "Coconut milk", "Salt", "Pepper"],
    "Vegetable Stir Fry": ["Bell peppers", "Broccoli", "Carrots", "Garlic", "Soy sauce", "Sesame oil", "Rice"],
    "Chocolate Cake": ["Flour", "Sugar", "Cocoa powder", "Baking powder", "Eggs", "Milk", "Butter", "Vanilla extract"],
    "Caesar Salad": ["Romaine lettuce", "Croutons", "Parmesan cheese", "Caesar dressing", "Chicken breast (optional)", "Anchovies (optional)"]
}

# Set the title of the Streamlit app
st.title("Cooking Application")

# Display the list of recipes
st.header("Select a Recipe")
recipe_name = st.selectbox("Choose a recipe:", list(recipes.keys()))

# Display the ingredients for the selected recipe
if recipe_name:
    st.header(f"Ingredients for {recipe_name}")
    ingredients = recipes[recipe_name]
    for ingredient in ingredients:
        st.write(f"- {ingredient}")

# Run the Streamlit app
if __name__ == "__main__":
    st.write("Welcome to the Cooking Application!")
