import json
from typing import TypedDict
from datetime import date

# ----------------------------
# Exceptions
# ----------------------------

class ExpenseError(Exception):
    pass

class InvalidCategoryError(ExpenseError):
    pass

class NegativeAmountError(ExpenseError):
    pass

# ----------------------------
# JSON data type
# ----------------------------

class ExpenseData(TypedDict):
    amount: float
    category: str
    description: str

# ----------------------------
# Expense
# ----------------------------

class Expense:

    VALID_CATEGORIES = ["food", "drink","cloths"]

    def __init__(
        self,
        amount: float,
        category: str,
        description: str
    ) -> None:

        if amount < 0:
            raise NegativeAmountError("Unacceptable amount")

        if category not in self.VALID_CATEGORIES:
            raise InvalidCategoryError("Unrecognized category")

        self.amount: float = amount
        self.category: str = category
        self.description: str = description

    def __repr__(self) -> str:
        return (
            f"Expense(amount={self.amount}, "
            f"category='{self.category}', "
            f"description='{self.description}')"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Expense):
            return (
                self.amount == other.amount
                and self.category == other.category
                and self.description == other.description
            )

        return False    

# ----------------------------
# ExpenseTracker
# ----------------------------

class ExpenseTracker:

    def __init__(self) -> None:
        self._expenses: list[Expense] = []

    @property
    def expenses(self) -> list[Expense]:
        return self._expenses

    def monthly_summary(self, year: int, month: int) -> dict:
        monthly_expenses = [
            expense
            for expense in self._expenses
            if expense.date.year == year
            and expense.date.month == month
        ]

        total = sum(expense.amount for expense in monthly_expenses)

        by_category = {}

        for expense in monthly_expenses:
            if expense.category not in by_category:
                by_category[expense.category] = 0
            by_category[expense.category] += expense.amount

        return {
            "year": year,
            "month": month,
            "total": total,
            "number_of_expenses": len(monthly_expenses),
            "by_category": by_category
        }

    def category_filter(self,category : str ) -> list:
        return [expense for expense in self._expenses if expense.category == category]

    def add_expense(self, expense: Expense) -> None:
        self._expenses.append(expense)

    def delete_expense(self,description: str) -> Expense | None:
        for expense in self._expenses:
            if expense.description == description:
                self.expenses.remove(expense)
                return expense
        return None
    
    def find_expense(self, description: str) -> Expense | None:
        for expense in self._expenses:
            if expense.description == description:
                return expense

        return None

    def save_to_json(self, filename: str) -> None:
        data: list[ExpenseData] = []

        for expense in self._expenses:
            data.append({
                "amount": expense.amount,
                "category": expense.category,
                "description": expense.description
            })

        # The `with` statement is the context manager.
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename: str) -> None:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return

        self._expenses.clear()

        for item in data:
            expense = Expense(
                amount=item["amount"],
                category=item["category"],
                description=item["description"]
            )

            self._expenses.append(expense)


# ----------------------------
# CLI
# ----------------------------

def main() -> None:

    filename = "expenses.json"

    tracker = ExpenseTracker()

    # Load existing expenses.
    tracker.load_from_json(filename)

    try:
        amount: float = float(input("Inject expense amount: "))

        category: str = input("Inject expense category: ")

        description: str = input("Inject expense description: ")

        expense = Expense(amount,category,description)

        tracker.add_expense(expense)

        tracker.save_to_json(filename)

        print("Expense added successfully.")
        print(expense)

    except NegativeAmountError as error:
        print(f"Catch Error: {error}")

    except InvalidCategoryError as error:
        print(f"Catch Error: {error}")

    except ValueError:
        print("Catch Error: amount must be a number.")

if __name__ == "__main__":
    main()

