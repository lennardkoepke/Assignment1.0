import random


print("    _______")
print(".  /|_||_\\`._")
print(". (   _    _ _\\")
print("=. `.-(_)--(_)-'")
print("\nGive me three inputs to individualize this basic car and create your own car model!\n")


tires_list = ["(_)", "(x)", "[x]"]
engines= ["V12 biturbo","V8", "electric", "AMG","2.0 TDI"]

while True:
    try:
        print("Choose tires:")
        print("1.", tires_list[0])
        print("2.", tires_list[1])
        print("3.", tires_list[2])
        tires = int(input("Enter 1, 2, or 3: "))
        if tires in [1, 2, 3]:
            break
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Please enter a valid number.")
    if tires == 1:
        tires_list[0] = tires_list[1]

random_engines = random.choice(engines)

selected_tires = tires_list[tires - 1]

print("\nYou selected tires:", selected_tires)

name= str(input("enter the name of your car"))

def draw_car(length):
    car = []


    roof = "    "
    for i in range(7 + length):
        roof += "_"
    car.append(roof)


    windshield = ".  /|"
    for i in range(1 + length):
        windshield += "__|"
    windshield += "__\\"
    car.append(windshield)


    body = ". (   _L "
    for i in range(1 + length):
        body += "_ L"
    body += "_____\\"
    car.append(body)


    wheels = "=. `- " + selected_tires+""
    for i in range(4 + 1 * length):
        wheels += "-"
    wheels += "."+ selected_tires + " D'"
    car.append(wheels)


    for line in car:
        print(line)


while True:
    try:
        user_length = int(input("How long should your car be? (suggested 0–3): "))
        if user_length == user_length:
            break
    except ValueError:
        print("Please enter a valid number.")



draw_car(user_length)
print("VROOOOOM!\n")
print("car model:",name,random_engines,)
