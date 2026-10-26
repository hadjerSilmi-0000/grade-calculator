def calculate_average(grades):
    if not grades:
        raise ValueError("The grades list cannot be empty")
    return sum(grades) / len(grades)


def is_passing(average):
    return average >= 10
