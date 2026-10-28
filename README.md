# Student Grade Calculator

A simple Python application that calculates the average grade of a student, determines whether the student passes, and assigns a grade category.

Built as a DevOps lab on Git, GitHub collaboration, and Continuous Integration.

## Features

- `calculate_average(grades)`: average of a list of grades (raises `ValueError` if the list is empty)
- `is_passing(average)`: `True` when the average is 10 or more
- `get_grade_category(average)`: returns `Excellent` (16+), `Good` (12 to 15.99), `Average` (10 to 11.99), or `Fail` (below 10)

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

## Continuous Integration

A GitHub Actions workflow (`.github/workflows/ci.yml`) runs `flake8` and `pytest` on every pull request to `main` and on every push to `main`. The `main` branch is protected: changes need a pull request, one approval, and a passing `quality-gate` check.

## Team and Workflow

| Role | GitHub user | Work |
|---|---|---|
| Project owner | `hadjerSilmi-0000` | Repository, CI workflow, branch protection, reviews, release |
| Contributor B | `asma00ik` | Grade category feature, README documentation |
| Contributor C | `Roumaissa-Kenn-H` | Passing grade bug fix |

Workflow: Issue → feature branch → commits → pull request → CI → review → merge → release.

## Release

`v1.0.0`: first stable release (grade categories, exact passing limit of 10, improved documentation, CI quality gate).
