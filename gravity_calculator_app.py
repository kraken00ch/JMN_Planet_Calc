#!/usr/bin/env python

"""
gravity_calculator_app.py: A web application for computing gravitational weight on other planets.

This Flask application allows users to input their weight in pounds and select a planet.
It then calculates and displays the weight of the user on the chosen planet.

The application is divided into modular functions and includes the following modules:
- user_input.py: Handles user input for weight and planet selection.
- planet_calculation.py: Performs calculations based on user input.
- display_info.py: Displays weight information on Earth and the selected planet.

The main backend file, app.py, integrates these modules and serves the application through Flask.
"""

__author__ = "Jeffrey Nucci"

# Import the necessary functions from the modules
from user_input import get_user_weight, get_planet_selection
from planet_calculation import calculate_weight_on_planet
from display_info import display_weight_info
import time

# Main program
continue_program = True
try:
    while continue_program:
        # Call the get_user_weight and get_planet_selection functions
        userweight = get_user_weight()
        planet = get_planet_selection()

        # Call the calculate_weight_on_planet function
        result = calculate_weight_on_planet(userweight, planet)

        # Call the display_weight_info function
        display_weight_info(userweight, result)

        user_choice = input("Continue?\nSelect 'Y' for YES\nSelect 'N' for NO\n").upper()
        if user_choice != 'Y':
            continue_program = False
# exit exceptions
except (KeyboardInterrupt, EOFError):
    print("\nProgram interrupted. Exiting.")
except Exception as e:
    print(f"An error occurred: {e}. Exiting.")
finally:
    print("Exiting the program...")
    time.sleep(3)  # Sleep for 3 seconds before quitting