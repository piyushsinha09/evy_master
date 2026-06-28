

def split_bill(total: float, people: int) -> float:
    """
    Splits the total bill amount evenly among the specified number of people.

    Parameters:
    total (float): The total bill amount.
    people (int): The number of people to split the bill among.

    Returns:
    float: The amount each person should pay, rounded to 2 decimal places.

    Raises:
    ValueError: If the total is negative or the number of people is less than 1.
    """
    if total < 0:
        raise ValueError("Total amount cannot be negative.")
    if people < 1:
        raise ValueError("Number of people must be at least 1.")
    share = total / people
    return round(share, 2)
