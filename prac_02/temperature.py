MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = change_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit_temperature=float(input("Fahrenheit: "))
            convert_celsius = change_to_celsius(fahrenheit_temperature)
            print(f"Result: {convert_celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def change_to_celsius(fahrenheit_temperature):
    convert_celsius = 5 / 9 * (fahrenheit_temperature - 32)
    return convert_celsius


def change_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()