# 2. The Recipe Ratio Adjuster


# def get_servings():
#     while True:
#         try:
#             original_servings = int(input("Enter the number of servings the recipe is originally for: "))
#             desired_servings = int(input("Enter the number of servings you wish to make: "))
#             return original_servings, desired_servings
#         except ValueError:
#             print("Invalid input. Please enter valid numbers for servings.")


# Task 2: 

# def calculate_adjustment_factor(original_servings, desired_servings):
#     try:
#         adjustment_factor = desired_servings / original_servings
#         return adjustment_factor
#     except (ZeroDivisionError, OverflowError) as e:
#         print(f"An error occurred during the calculation: {e}")
#         return None
    
    
# Task 3: 
    
    
# def main():
#     print("Welcome to the Recipe Ratio Adjuster!")

#     original_servings, desired_servings = get_servings()

#     try:
#         adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)
#         if adjustment_factor is not None:
#             print(f"The adjustment factor for the recipe is {adjustment_factor:.2f}. Adjust your ingredient quantities accordingly.")
#     else:
#         print("The quantity adjustment calculation was successful.")
#     finally:
#         print("Enjoy your cooking!")

# if __name__ == "__main__":
#     main()
