

def split_bill(total: float, people: int) -> float:
    """
    Splits the total bill amount evenly among the given number of people.

    Parameters:
    total (float): The total bill amount. Must be non-negative.
    people (int): The number of people to split the bill among. Must be greater than zero.

    Returns:
    float: The share of the bill each person should pay, rounded to 2 decimal places.

    Raises:
    ValueError: If the total is negative or the number of people is less than or equal to zero.
    """
    if total < 0:
        raise ValueError("Total bill amount cannot be negative.")
    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    share = total / people
    return round(share, 2)
