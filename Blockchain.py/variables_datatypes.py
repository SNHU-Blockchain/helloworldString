class CatAge:
    value = 11
    valueTwo = 11.75  # Changed to a float value for consistency

def get_cat_info():
    cat_name = input("Please enter your cat's name: ")
    while True:
        cat_age = input("Please enter your cat's age: ")
        try:
            cat_age = float(cat_age)  # Convert input to float
            break  # Exit the loop if input is successfully converted to float
        except ValueError:
            print("Invalid input! Age must be a number.")
    return cat_name, cat_age

def compare_cat_age(cat_name, cat_age):
    if cat_age == CatAge.value:
        print("This is not my cat!")
    elif cat_age == CatAge.valueTwo:
        print(f"This is my real cat named {cat_name}. This is my real cat's age {cat_age} years.")
    else:
        print("This is not my cat.")

# Get cat information from the user
cat_name, cat_age = get_cat_info()

# Compare cat's age with predefined values and print according to the method
compare_cat_age(cat_name, cat_age)







