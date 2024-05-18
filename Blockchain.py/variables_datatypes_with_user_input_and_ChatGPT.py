

# class CatAge:
    # value = 11
    # valueTwo = 11.75
# 
# def get_cat_info():
    # cat_name = input("Please enter your cat's name: ")
    # while True:
        # try:
            # cat_age = float(input("Please enter your cat's age: "))
            # break
        # except ValueError:
            # print("Invalid input! Age must be a number.")
    # return cat_name, cat_age
# 
# class catNameString:
    # name = "Best Cat Ever"
    # 
    # def __str__(self):
        # return self.name
# 
# name_data = catNameString()
# print("My Cat's name is " + str(name_data) + "!")
# 
# def compare_cat_age(cat_name, cat_age):
    # cat_name == catNameString.name
    # while True: 
        # if cat_age == CatAge.value:
            # print("This is not my cat!")
            # break
        # elif cat_age == CatAge.valueTwo:
            # # print(f"This is my real cat named {cat_name}. This is my real cat's age {cat_age} years.")
        # else:
            # print("This is not my cat.")
# 
# Get cat information from the user
# cat_name, cat_age = get_cat_info()
# 
# Compare cat's age with predefined values and print according to the method
# compare_cat_age(cat_name, cat_age)
# 
# 
# 

class CatAge:
    value = 11
    valueTwo = 11.75

class catNameString:
    name = "Best Cat Ever"
    
    def __str__(self):
        return self.name

def get_cat_info():
    cat_name_input = input("Please enter your cat's name: ")
    while cat_name_input != catNameString.name:
        print("Incorrect cat name. Please try again.")
        cat_name_input = input("Please enter your cat's name: ")
    
    while True:
        try:
            cat_age_input = float(input("Please enter your cat's age: "))
            break
        except ValueError:
            print("Invalid input! Age must be a number.")
    return cat_name_input, cat_age_input

def compare_cat_age(cat_name, cat_age):
    if cat_age == CatAge.value:
        print("This is not my cat!")
    elif cat_age == CatAge.valueTwo:
        print(f"Congratulations! You have found your cat named {cat_name}. Your cat is {cat_age} years old.")
    else:
        print("This is not my cat.")

# Get cat information from the user
cat_name, cat_age = get_cat_info()

# Compare cat's age with predefined values and print according to the method
compare_cat_age(cat_name, cat_age)

