#!usr/bin/env python

"""JMNplanetCalc.py: A calculator to compute your gravitational weight on other planets.

This program takes user input for weight in pounds and the selection of a planet.
It then calculates and prints the weight of the user on the chosen planet.
"""

__author__ = "Jeffrey Nucci"

import time

def get_user_weight():
    """
    Prompt the user to enter their weight and validate the input.
    
    Returns:
    float: The user's weight in pounds.
    """
    while True:
        try:
            return float(input("Enter your weight in lbs\n"))
        # Input validation
        except ValueError:
            print("Invalid input. Please enter a valid weight.")

def get_planet_selection():
    """
    Prompt the user to select a planet and validate the input.

    Returns:
        int: The selected planet number.
    """
    while True:
        try:
            planet = int(input("List of Planets\n1.Mercury\n2.Venus\n3.Moon\n4.Mars\n5.Jupiter\n6.Saturn\n7.Uranus\n8.Neptune\n9.Pluto\n"))
            if 1 <= planet <= 9:
                return planet  # Break out of the loop if the input is a valid planet number
            else:
                print("Invalid selection. Please enter a number between 1 and 9.")
        # Input validation
        except ValueError:
            print("Invalid input. Please enter a valid planet number.")
# switch case to calculate weight
def calculate_weight_on_planet(userweight, planet):
    """
    Calculate the weight on a selected planet based on user input.

    Args:
        userweight (float): The user's weight in pounds.
        planet (int): The selected planet number.
        
    Returns:
        float: The calculated weight on the selected planet.
    """
    match planet: 
        case 1: # Mercury
            result = userweight * 0.38
            print(f"Weight on Mercury: {result}")
        case 2: # Venus
            result = userweight * 0.91
            print(f"Weight on Venus: {result}")
        case 3: # Moon
            result = userweight * 0.17
            print(f"Weight on the Moon: {result}")
        case 4: # Mars
            result = userweight * 0.38
            print(f"Weight on Mars: {result}")
        case 5: # Jupiter
            result = userweight * 2.34
            print(f"Weight on Jupiter: {result}")
        case 6: # Saturn
            result = userweight * 1.06
            print(f"Weight on Saturn: {result}")
        case 7: # Uranus
            result = userweight * 0.92
            print(f"Weight on Uranus: {result}")
        case 8: # Neptune
            result = userweight * 1.19
            print(f"Weight on Neptune: {result}")
        case 9: # Pluto
            result = userweight * 0.07
            print(f"Weight on Pluto: {result}")
        case _:
            print("Invalid selection")
# print formatting and output rounding
def display_weight_info(userweight, result):
    """
    Display weight information on Earth and the selected planet.

    Args:
        userweight (float): The user's weight in pounds.
        result (float): The calculated weight on the selected planet.
    """
    print(f"Weight on Earth: {userweight:.2f}")
    print(f"Weight on selected planet: {result:.2f}")
# get input values from the user   
def planet_calc():
    """
    Perform the planet claculation based on user input.
    """
    print("Welcome to JMN Planet Calc!\n")
    userweight = get_user_weight()
    planet = get_planet_selection()
    print("Weight on Earth:", userweight)
    calculate_weight_on_planet(userweight, planet)
# Main program
continue_program = True
try:
    while continue_program:
        planet_calc()
        user_choice = input("Continue?\nSelect 'Y' for YES\nSelect 'N' for NO\n").upper()
        if user_choice != 'Y':
            continue_program = False
# exit exceptions
except (KeyboardInterrupt, EOFError):
    print("\nProgram interrupted. Exiting.")
except Exception as e:
    print(f"An error occured: {e}. Exiting.")
finally:
    continue_program = False
    print("Exiting the program...")
    time.sleep(3) # Sleep for 3 seconds before quitting