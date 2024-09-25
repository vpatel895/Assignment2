class SandwichMaker:

    def __init__(self, resources):
        self.machine_resources = resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredients, amount in ingredients.items():
            if amount > self.machine_resources.get(ingredients, 0):
                print(f"Sorry there is not enough {ingredients}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredients, amount in order_ingredients.items():
            self.machine_resources[ingredients] -= amount
            print(f"{sandwich_size} sandwich is ready. Bon appetit!")