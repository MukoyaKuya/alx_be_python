# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Conversion functions
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Main function to handle user interaction
def main():
    print("Temperature Conversion Tool")

    try:
        # Get temperature value
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F")
        elif unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Error: {e}")

# Run the tool
if __name__ == "__main__":
    main()
