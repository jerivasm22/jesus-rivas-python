# Section 1

name = "Jesus"
age = 28
height = 5.11
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2

name = input("What is your name?: ")
year_birth = int(input("What is your year of birth?: "))
current_year = 2026
age = current_year - year_birth
print(f"Hi, {name}! You are approximately {age} years old.")

#Section 3

number_one = float(input("Enter the firt number: "))
number_two = float(input("Enter the second number: "))
multiply = float(number_one * number_two)
print(f"{number_one} × {number_two} = {multiply:.1f}")

#Section 4

item = "Keyboard Deluxe"
price = float(74.99)
quantity = int(3)
total = float(price * quantity)

print("===========================")
print("        RECEIPT     ")
print("===========================")
print(f"Item:      {item}")
print(f"Price:     ${price}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")

#Section 5

name = input("What is your name?: ")
hometown = input("What is your hometown?: ")
estate = input("Which state in the country is it in? (for example: IL, NC, VA): ")
hobby = input("What is your favority hobbie?: ")
fun_fact = input("Tell me an fun fact about yourself: ")
year_born = int(input("What is your year of birth?: "))
act_year = 2026
age_now = act_year - year_born

print("╔══════════════════════════════╗")
print(f"      PROFILE: {name}      ")
print("╚══════════════════════════════╝")
print(f"Hometown:   {hometown}, {estate}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {age_now}")
