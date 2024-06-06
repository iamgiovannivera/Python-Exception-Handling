# 1. Exceptional Weather Forecast



# def get_temperature():
#     while True:
#         try:
#             temp = float(input("Enter the temperature in Fahrenheit: "))
#             return temp
#         except ValueError:
#             print("Invalid input. Please enter a numerical value for the temperature.")
            
            
# Task 2: Temperature Conversion



# def fahrenheit_to_celsius(fahrenheit):
#     try:
#         celsius = (fahrenheit - 32) * 5 / 9
#         return celsius
#     except (OverflowError, ZeroDivisionError) as e:
#         print(f"An error occurred during the conversion: {e}")
#         return None
    
    
# Task 3: User Experience


# def main():
#     print("Welcome to the Weather Forecast Application!")

#     temperature_fahrenheit = get_temperature()

#     try:
#         temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
#         if temperature_celsius is not None:
#             print(f"The temperature in Celsius is {temperature_celsius:.2f}°C.")
#     else:
#         print("The temperature conversion was successful.")
#     finally:
#         print("Thank you for using the Weather Forecast Application!")

# if __name__ == "__main__":
#     main()
