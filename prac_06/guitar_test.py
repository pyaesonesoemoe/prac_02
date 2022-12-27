from prac_06.guitar import Guitar

CURRENT_YEAR= 2022

def run_tests():
    name= "Gibson L-5 CES"
    year= 1922
    cost= 16035.40

    guitar= Guitar(name, year, cost)
    other= Guitar("Another guitar", 2016, 16543.30)
    print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {5}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()})")

if __name__== '__main__':
    run_tests()