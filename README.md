# Expense Tracker

A simple command-line expense tracker built with Python.

The project demonstrates:

* Custom exception handling
* Object-oriented programming
* Type hints
* `@property`
* `__repr__` and `__eq__`
* In-memory expense storage
* JSON persistence
* Context managers
* `pytest`
* `mypy`

## Requirements

* Python 3.10+
* pip

Check your Python version:

```bash
python --version
```

---

## Project Structure

```text
expense-tracker/
├── app.py
├── test_app.py
└── README.md
```

`expenses.json` is created automatically when the application saves expenses.

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd expense-tracker
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install pytest mypy
```

Verify the installations:

```bash
pytest --version
mypy --version
```

---

## Run the Application

Start the application with:

```bash
python app.py
```

You will be prompted for:

```text
Insert expense amount:
Insert expense category:
Insert expense description:
```

Example:

```text
Insert expense amount: 50
Insert expense category: food
Insert expense description: lunch
```

The application will create the expense, add it to the `ExpenseTracker`, and save the expenses to `expenses.json`.

---

## Valid Categories

The application currently accepts:

* `food`
* `drink`

Example:

```text
Insert expense amount: 25
Insert expense category: drink
Insert expense description: coffee
```

---

## Error Handling

### Negative Amount

Negative amounts are rejected:

```text
Insert expense amount: -20
```

This raises:

```text
NegativeAmountError
```

### Invalid Category

Unsupported categories are rejected:

```text
Insert expense category: transport
```

This raises:

```text
InvalidCategoryError
```

### Invalid Amount

The amount must be a valid number:

```text
Insert expense amount: abc
```

The application handles the resulting `ValueError`.

---

## Run Tests

Run the complete test suite:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

The test suite covers:

* Expense creation
* `__repr__`
* `__eq__`
* Negative amounts
* Invalid categories
* Adding expenses
* Finding expenses
* Missing expenses
* JSON saving
* JSON loading
* pytest fixtures

---

## Run Mypy

Check the application for type errors:

```bash
mypy app.py
```

Check the test file:

```bash
mypy test_app.py
```

The goal is for both commands to complete without type-checking errors.

---

## JSON Storage

Expenses are stored in:

```text
expenses.json
```

The application:

1. Loads existing expenses when it starts.
2. Accepts a new expense from the user.
3. Adds the expense to the `ExpenseTracker`.
4. Saves the updated expenses to the JSON file.

File operations use Python's context manager:

```python
with open(...) as file:
    ...
```

This ensures that the file is properly closed after the operation.

---

## Typical Workflow

```text
Start application
       ↓
Load expenses from JSON
       ↓
Ask for amount
       ↓
Ask for category
       ↓
Ask for description
       ↓
Validate input
       ↓
Create Expense
       ↓
Add Expense to ExpenseTracker
       ↓
Save expenses to JSON
       ↓
Display result
```

---

## Useful Commands

Run the application:

```bash
python app.py
```

Run tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Check types:

```bash
mypy app.py
```

Check test types:

```bash
mypy test_app.py
```

---

## Future Improvements

Possible future features include:

* Delete expenses
* Edit expenses
* List all expenses
* Search by category
* Calculate total spending
* Add more categories
* Validate empty descriptions
* Handle corrupted JSON files
* Add dates to expenses
* Store expenses in PostgreSQL

## License

This project is for educational and learning purposes.
