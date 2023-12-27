# gravity_calculator_app.py

# Import the necessary functions from the modules
from user_input import get_user_weight, get_planet_selection
from planet_calculation import calculate_weight_on_planet
from display_info import display_weight_info

def calculate_weight_for_user_on_planet():
    try:
        # Call the get_user_weight and get_planet_selection functions
        userweight = get_user_weight()
        planet = get_planet_selection()

        # Call the calculate_weight_on_planet function
        result = calculate_weight_on_planet(userweight, planet)

        # Call the display_weight_info function (if needed)
        display_weight_info(userweight, result)

        return userweight, result
    except ValueError:
        raise ValueError('Invalid input. Please enter valid numbers.')

# Optionally, you can keep the while loop in a separate function
def run_program():
    try:
        userweight, result = calculate_weight_for_user_on_planet()
    except Exception as e:
        print(f"An error occurred: {e}. Exiting.")
        return

if __name__ == "__main__":
    run_program()
