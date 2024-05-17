# class CatAge:
    # value = 11
    # valueTwo = 11.75  # Changed to a float value for consistency
# 
# def get_cat_info():
    # cat_name = input("Please enter your cat's name: ")
    # while True:
        # cat_age = input("Please enter your cat's age: ")
        # try:
            # cat_age = float(cat_age)  # Convert input to float
            # break  # Exit the loop if input is successfully converted to float
        # except ValueError:
            # print("Invalid input! Age must be a number.")
    # return cat_name, cat_age
# 
# def compare_cat_age(cat_name, cat_age):
    # if cat_age == CatAge.value:
        # print("This is not my cat!")
    # elif cat_age == CatAge.valueTwo:
        # # print(f"This is my real cat named {cat_name}. This is my real cat's age {cat_age} years.")
    # else:
        # print("This is not my cat.")
# 
# Get cat information from the user
cat_name, cat_age = get_cat_info()

# Compare cat's age with predefined values and print according to the method
compare_cat_age(cat_name, cat_age)
# 
# 
# 
# class CatAge:
    # value = 11
    # valueTwo = "11.75"
    # realCatAge = float(valueTwo)
    # 
    # def __int__(self):
        # return self.value
    # 
    # def __str__(self):
        # return self.valueTwo
# 
# class catNameString:
    # name = "Best Cat Ever"
    # 
    # def __str__(self):
        # return self.name
# 
# class Boolean:
    # def __init__(self):
        # self.num_data_value = CatAge()
        # self.num_data_valueTwo = CatAge()
        # self.name_data = catNameString()
# 
# def get_cat_info():
    # cat_name = input("Please enter your cat's name: ")
    # cat_age = input("Please enter your cat's age: ")
    # return cat_name, cat_age
# 
# Create an instance of the Boolean class
boolean_instance = Boolean()
# 
# Loop to validate user input
# while True:
    # cat_name_input, cat_age_input = get_cat_info()
    # 
    # # if cat_name_input == str(boolean_instance.name_data) and cat_age_input == boolean_instance.num_data_valueTwo.valueTwo:
        # print("Congratulations! You have entered the correct cat information.")
        # break
    # else:
        # # print("Sorry, the entered information does not match our records. Please try again.")

class CatAge:
    value = 11
    valueTwo = 11.75

def get_cat_info():
    cat_name = input("Please enter your cat's name: ")
    while True:
        try:
            cat_age = float(input("Please enter your cat's age: "))
            break
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



