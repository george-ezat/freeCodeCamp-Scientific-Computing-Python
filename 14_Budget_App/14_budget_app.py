class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.ledger = []

    # -------------------------------------------

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    # -------------------------------------------

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    # -------------------------------------------

    def get_balance(self):
        return self.balance

    # -------------------------------------------

    def transfer(self, amount, another):
        if self.check_funds(amount):
            self.balance -= amount
            another.balance += amount

            self.ledger.append(
                {'amount': -amount, 'description': f'Transfer to {another.name}'})
            another.ledger.append(
                {'amount': amount, 'description': f'Transfer from {self.name}'})

            return True

        return False

    # -------------------------------------------

    def check_funds(self, amount):
        return amount <= self.balance

    # -------------------------------------------

    def __str__(self):
        to_print = []
        to_print.append(f"{self.name:*^30}")
        for item in self.ledger:
            item_line = f"{item['description'][:23]:<23}{item['amount']:>7.2f}"
            to_print.append(item_line)

        to_print.append(f'Total: {self.balance}')

        return '\n'.join(to_print)


# -----------------------------------------------


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent_amounts = []
    category_names = []

    # Calculate total spent for each category
    for category in categories:
        spent = sum(-item['amount']
                    for item in category.ledger if item['amount'] < 0)
        spent_amounts.append(spent)
        category_names.append(category.name)

    # Calculate total spent across all categories and then the percentages
    total_spent = sum(spent_amounts)
    if total_spent == 0:
        # Avoid division by zero if nothing was spent
        percentages = [0] * len(spent_amounts)
    else:
        percentages = [((amount / total_spent) * 100 // 10)
                       * 10 for amount in spent_amounts]

    # --- Build the Chart Bars ---
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            if p >= i:
                chart += "o  "  # Add 'o' if percentage is high enough
            else:
                chart += "   "  # Otherwise, add spaces
        chart += "\n"

    # --- Build the Dashed Line ---
    dashes = "-" * (len(categories) * 3 + 1)
    chart += "    " + dashes + "\n"

    # --- Build the Vertical Category Names ---
    max_len = max(len(name) for name in category_names)

    for i in range(max_len):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        # Add a newline, but not on the very last line
        if i < max_len - 1:
            chart += "\n"

    return chart


# -----------------------------------------------


food = Category("Food")
food.deposit(100, "initial deposit")
food.withdraw(25.50, "groceries")

entertainment = Category("Entertainment")
entertainment.deposit(20, "initial deposit")
entertainment.withdraw(30, "insufficient amount")

clothing = Category("Clothing")
clothing.deposit(50, "initial deposit")
transfer_result = clothing.transfer(15, food)

auto = Category("Auto")
auto.deposit(100, "initial deposit")
auto.withdraw(15, "Fixes")

print(food, '\n')
print(entertainment, '\n')
print(clothing, '\n')
print(auto, '\n')
print(create_spend_chart([food, entertainment,  clothing, auto]))
