# user_input.py

def get_user_weight():
    while True:
        try:
            return float(input("Enter your weight in lbs\n"))
        except ValueError:
            print("Invalid input. Please enter a valid weight.")

def get_planet_selection():
    while True:
        try:
            planet = int(input("List of Planets\n1.Mercury\n2.Venus\n3.Moon\n4.Mars\n5.Jupiter\n6.Saturn\n7.Uranus\n8.Neptune\n9.Pluto\n"))
            if 1 <= planet <= 9:
                return planet
            else:
                print("Invalid selection. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid planet number.")
