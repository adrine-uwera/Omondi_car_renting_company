# Program for Mr Omindi car renting business
# This program will help Omindi to keep a record of his car collection and do some business operations
# like adding and removing car from his collection, keep track of times the car has been rented and the amount of income
# from that car

# class for car object
class Car:
    # Method to initial car properties
    def __init__(self, model, year_released, year_acquired, plate_number, status):
        self.model = model
        self.year_released = year_released
        self.year_acquired = year_acquired
        self.plate_number = plate_number
        self.status = status
        self.times_rent = 0
        self.rent_income = []


# Initial car collection
cars_collection = [
    Car(model='BMW', year_released='2012', year_acquired='2021', plate_number='RAC234C21', status='On offer'),
    Car(model='TOYOTA', year_released='2006', year_acquired='2021', plate_number='RAB234G22', status='On offer'),
    Car(model='MERCEDES', year_released='2020', year_acquired='2021', plate_number='RAE234B23', status='On offer'),
    Car(model='VOLKSWAGEN', year_released='2013', year_acquired='2021', plate_number='RAB234A24', status='On offer'),
    Car(model='JAGUAR', year_released='2015', year_acquired='2021', plate_number='RAC234D25', status='On offer'),
]


# This function display the general description of Omindi business
def print_program_intro():
    print(" ")
    print("OMINDI CAR RENTING COMPANY")
    print("--------------------------")
    print(" ")


# This function display the list of cars in cars collection
def print_car_collection():
    print("Current car collection")
    print('----------------------')
    for car in cars_collection:
        print(car.model, car.plate_number, car.status)


# This function adds(append) a car to the cars collection
def add_car(car):
    cars_collection.append(car)


# This function removes a car from the cars collection
def remove_car(car):
    cars_collection.remove(car)


# This function adds income from the cars rented to the rent_income array
def rent_car(car, amount):
    car.rent_income.append(amount)


# This function calculates the number of times the car has been rented
def times_rent(car):
    print(f"The car has been rented {len(car.rent_income)} times")


# This function calculates the total income from the car
def print_rent_income(car):
    print(f'Total rent amount for {car.plate_number}: ${sum(car.rent_income)}')


# This function will allow users to do different business operations; adding a car to the car collection,
# removing a car from the car collection, renting a car, returning a rented car, and displaying the car collection.
def perform_business_operation():
    while True:
        start = input("Enter 'Y' to do a business operation or any other key to exit: ")
        if start.upper() == 'Y':    # checks if the user wants to do a business operation

            # display a list of business operations the user can choose from and receive user's choice
            is_action = input("Enter:\n '1' to add a car to the collection, \n '2' to remove a car from the collection,"
                              " \n '3' to lend a car, \n '4' to return a rented car, "
                              "\n '5' to view the current car collection or any key to exit. \n Enter your choice: ")

            # display when the user chooses '1' to add a car to the collection
            if is_action == '1':
                print(" ")
                print("Add new car")
                print("-----------")
                try:         # Checks if the user's input type is valid
                    add_number = int(input("Enter in numerical form the number of cars "
                                           "to be added to the collection: "))
                except ValueError:  # displayed when the user's input type is invalid
                    print('ONLY NUMBER ARE ALLOWED!!!!')
                    continue

                # This loop will allow the user to add the number of cars entered
                for number in range(add_number):
                    try:                    # Checks if the user's input type is valid
                        print(" ")
                        print("Add bellow all car details")
                        add_car(Car(
                            model=input("Enter model: "),
                            year_released=int(input("Enter released year in numerical form: ")),
                            year_acquired=int(input("Enter acquired year in numerical form: ")),
                            plate_number=input("Enter plate number: "),
                            status="On offer",
                        ))                   # calls the add_car function
                    except ValueError:      # displayed when the user's input type is invalid
                        print('ONLY NUMBER ARE ALLOWED!!!!')
                        continue
                else:
                    continue

            # display when the user chooses '2' to remove a car from the collection
            elif is_action == '2':
                print(" ")
                print("Remove a car")
                print('------------')
                try:         # Checks if the user's input type is valid
                    remove_number = int(input("Enter in numerical form the number of cars "
                                              "to be removed from the collection: "))
                except ValueError:  # displayed when the user's input type is invalid
                    print('ONLY NUMBER ARE ALLOWED!!!!')
                    continue

                # This loop will allow the user to remove the number of cars entered
                for number in range(remove_number):
                    plate = input("Enter plate number: ")

                    # loops through the car collection
                    for car in cars_collection:

                        # checks if the the plate number provided matches one of car's in car collection
                        if plate == car.plate_number:
                            remove_car(car)              # calls the remove_car function
                            print("The car has been removed from car collection")
                        elif plate != car.plate_number:
                            print("The plate number provided doesn't match any car in the car collection")
                            break
                else:
                    continue

            # display when the user chooses '3' to lend a car to a client
            elif is_action == '3':
                print(" ")
                print("Rent car")
                print("----------")
                try:         # Checks if the user's input type is valid
                    rent_number = int(input("Enter in numerical form the number of cars to be rented: "))
                except ValueError:  # displayed when the user's input type is invalid
                    print('ONLY NUMBER ARE ALLOWED!!!!')
                    continue
                # This loop will allow the user to rent the number of cars entered
                for number in range(rent_number):
                    plate = input("Enter plate: ")

                    # loops through the car collection
                    for car in cars_collection:

                        # checks if the the plate number provided matches one of car's in car collection
                        if plate == car.plate_number:
                            if car.status == 'On offer':
                                try:                    # Checks if the user's input type is valid
                                    rent_car(car, int(input("Enter amount of the rent: $")))
                                    times_rent(car)              # calls the times_rent function
                                    print_rent_income(car)       # calls the print_rent_income function
                                    car.status = "Rented"
                                except ValueError:      # displayed when the user's input type is invalid
                                    print('ONLY NUMBER ARE ALLOWED!!!!')

                            else:
                                print("The car has already been rented")

                        elif plate != car.plate_number:
                            print("The plate number provided doesn't match any car in the car collection")
                            break
                else:
                    continue

            # display when the user chooses '4' to return a car to the collection after it was rented
            elif is_action == '4':
                print(" ")
                print("Return a car")
                print("----------")
                try:         # Checks if the user's input type is valid
                    return_number = int(input("Enter in numerical form the number of cars "
                                              "returned from the borrowers: "))
                except ValueError:  # displayed when the user's input type is invalid
                    print('ONLY NUMBER ARE ALLOWED!!!!')
                    continue

                # This loop will allow the user to return the number of cars entered
                for number in range(return_number):
                    plate = input("Enter plate number: ")

                    # loops through the car details in the car collection
                    for car in cars_collection:

                        # checks if the plate number matches cars details in the collection
                        if plate == car.plate_number:
                            car.status = "On offer"
                            print("The car has been returned by the borrower.")

                            print("The car has been removed from car collection")
                        elif plate != car.plate_number:
                            print("The plate number provided doesn't match any car in the car collection")
                            break
                else:
                    continue

            # display when the user chooses '5' to view the current car collection
            elif is_action == '5':
                print(" ")
                print_car_collection()      # calls the print_car_collection function
                print(" ")

            else:
                break

        else:
            print("DONE!")
            break


# This function arranges how the order in which the above functions will be executed
# i.e. sets the layout of the program
def main():
    print_program_intro()
    perform_business_operation()


# This code calls the 'main' function which will also call the other functions
if __name__ == '__main__':
    main()
