import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
#cashier_instance = Cashier()

### Make an instance of SandwichMachine class and write the rest of the codes ###
def main():

    while True:
       pick = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

       if pick == "off":
           break
       elif pick == "report":
           print(f"bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
           print(f"ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
           print(f"cheese: {sandwich_maker_instance.machine_resources['cheese']} pound(s)")
       elif pick in recipes:
           if sandwich_maker_instance.check_resources(recipes[pick]["ingredients"]):
               coins = Cashier.process_coins()
               if Cashier.transaction_result(coins, recipes[pick]["cost"]):
                   sandwich_maker_instance.make_sandwich(pick, recipes[pick]["ingredients"])
       else:
           print("Invalid input. Please choose from small, medium, large, or off.")



if __name__=="__main__":
  main()