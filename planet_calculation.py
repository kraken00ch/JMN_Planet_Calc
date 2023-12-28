# planet_calculation.py
def calculate_weight_on_planet(userweight, planet):
    planet_factors = {
        1: 0.38,  # Mercury
        2: 0.91,  # Venus
        3: 0.17,  # Moon
        4: 0.38,  # Mars
        5: 2.34,  # Jupiter
        6: 1.06,  # Saturn
        7: 0.92,  # Uranus
        8: 1.19,  # Neptune
        9: 0.07   # Pluto
    }

    try:
        userweight = float(userweight)  # Convert userweight to float
    except ValueError:
        print("Invalid userweight. Could not convert to a number.")
        return None

    if planet in planet_factors:
        gravity_factors = planet_factors[planet]
        result = userweight * gravity_factors
        return result
    else:
        print("Invalid selection")
        return None
