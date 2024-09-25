class Cashier:
    def __init__(self):
        pass
    @staticmethod
    def process_coins():
        print("Please insert coins.")
        large_dollar = int(input("how many large dollar?: "))
        half_dollar = int(input("how many half dollar?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (large_dollar * 1.00) + (half_dollar * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total

    @staticmethod
    def transaction_result(coins, cost):
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

