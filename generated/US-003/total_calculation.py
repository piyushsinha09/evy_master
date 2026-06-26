def total_per_person(bill: float, tip_percent: float, people: int) -> float:
    """
    Calculate the total amount per person including tip.

    Parameters:
    bill (float): The total bill amount.
    tip_percent (float): The percentage of the bill to be added as tip.
    people (int): The number of people sharing the bill.

    Returns:
    float: The total amount each person should pay, rounded to 2 decimal places.

    Raises:
    ValueError: If the bill is negative or the number of people is less than 1.
    """
    if bill < 0:
        raise ValueError("Bill amount cannot be negative.")
    if people < 1:
        raise ValueError("Number of people must be at least 1.")

    total_with_tip = bill + (bill * tip_percent / 100)
    amount_per_person = total_with_tip / people
    return round(amount_per_person, 2)
