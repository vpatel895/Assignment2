### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredients, amount in ingredients.items():
            if amount > self.machine_resources[ingredients]:
                print(f"Sorry there is not enough {ingredients}.")
                return False
        return True
    def process_coins(self):
        print("Please insert coins.")
        large_dollar = int(input("how many large dollar?: "))
        half_dollar = int(input("how many half dollar?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (large_dollar * 1.00) + (half_dollar * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            else:
                print("Here is $0.00 in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredients, amount in order_ingredients.items():
            self.machine_resources[ingredients] -= amount
            print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
def main():
    sandwich_machine = SandwichMachine(resources)

    while True:
       pick = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

       if pick == "off":
           break
       elif pick == "report":
           print(f"bread: {sandwich_machine.machine_resources['bread']} slice(s)")
           print(f"ham: {sandwich_machine.machine_resources['ham']} slice(s)")
           print(f"cheese: {sandwich_machine.machine_resources['cheese']} pound(s)")
       elif pick in recipes:
           if sandwich_machine.check_resources(recipes[pick]["ingredients"]):
               coins = sandwich_machine.process_coins()
               if sandwich_machine.transaction_result(coins, recipes[pick]["cost"]):
                   sandwich_machine.make_sandwich(pick, recipes[pick]["ingredients"])
       else:
           print("Invalid input. Please choose from small, medium, large, or off.")

main()