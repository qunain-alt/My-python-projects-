# Fuel Cost Calculator for Cars

def get_positive_float_input(prompt_message):
    """
    Prompts the user for a floating-point number and handles invalid input.
    Continues to prompt until a valid, positive number is entered.
    """
    while True:
        try:
            value = float(input(prompt_message))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_fuel_cost():
    """
    Calculates the fuel cost for a car trip based on user input.
    """
    # Get validated user input
    distance = get_positive_float_input("Enter the distance of your trip in km: ")
    efficiency = get_positive_float_input("Enter your car's fuel efficiency (km per liter): ")
    fuel_price = get_positive_float_input("Enter the fuel price per liter: ")

    # Calculate fuel needed
    fuel_needed = distance / efficiency

    # Calculate cost
    total_cost = fuel_needed * fuel_price

    # Show results
    print(f"\nFor a trip of {distance:.2f} km:")
    print(f"Fuel needed: {fuel_needed:.2f} liters")
    print(f"Total cost: {total_cost:.2f} currency units")

# Run the calculator
if __name__ == "__main__":
    calculate_fuel_cost()
