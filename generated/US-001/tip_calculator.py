def calculate_tip(bill: float, tip_percent: float) -> float:
    """
    Calculate the tip amount based on the bill and tip percentage.

    Parameters:
    bill (float): The total bill amount. Must be non-negative.
    tip_percent (float): The tip percentage to apply. Must be non-negative.

    Returns:
    float: The calculated tip amount, rounded to 2 decimal places.

    Raises:
    ValueError: If either bill or tip_percent is negative.
    """
    if bill < 0:
        raise ValueError("Bill amount cannot be negative.")
    if tip_percent < 0:
        raise ValueError("Tip percentage cannot be negative.")

    tip_amount = (bill * tip_percent) / 100
    return round(tip_amount, 2)
