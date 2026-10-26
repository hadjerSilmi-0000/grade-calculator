def calculate_average(grades):
    if not grades:
        raise ValueError("The grades list cannot be empty")
    return sum(grades) / len(grades)


def is_passing(average):
    return average > 10


def get_grade_category(average):
    if average >= 16:
        return "Excellent"
    elif average >= 12:
        return "Good"
    elif average >= 10:
        return "Average"
    else:
        return "Fail"
