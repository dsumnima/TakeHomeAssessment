'''
Program: Manage dishes using Dish and Cookbook classes
'''

class Dish:
    def __init__(self, dish_id, name, ingredients, instructions):
        self.dish_id = dish_id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class Cookbook:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def display_dishes(self):
        print("\n--- Cookbook ---")
        for dish in self.dishes:
            print("\nID:", dish.dish_id)
            print("Name:", dish.name)
            print("Ingredients:", dish.ingredients)
            print("Instructions:", dish.instructions)

# Example usage
cb = Cookbook()

for i in range(2):
    print(f"\nEnter details for Dish {i+1}")
    dish = Dish(
        input("ID: "),
        input("Name: "),
        input("Ingredients: "),
        input("Instructions: ")
    )
    cb.add_dish(dish)

cb.display_dishes()
