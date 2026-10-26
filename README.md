# Student Grade Calculator

A simple Python application that calculates the average grade of a student
and determines whether the student passes.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from calculator import calculate_average, is_passing, get_grade_category

average = calculate_average([10, 12, 14])   # 12.0
print(is_passing(average))                  # True
print(get_grade_category(average))          # Good
```

## Run Tests

```bash
pytest -v
```

## Run Linting

```bash
flake8 .
```