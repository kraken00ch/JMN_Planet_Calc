# display_info.py
def display_weight_info(userweight, result):
    """
    Display weight information on Earth and the selected planet.

    Args:
        userweight (float): The user's weight in pounds.
        result (float): The calculated weight on the selected planet.
    """
    print(f"Weight on Earth: {userweight:.2f}")
    print(f"Weight on selected planet: {result:.2f}")
