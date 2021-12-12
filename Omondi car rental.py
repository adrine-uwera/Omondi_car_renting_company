# A program for Mr.Omondi's car renting service that will allow him to rent cars from his collection, add
# new cars to the collection or remove them, track the number of times each car has been rented and the money it
# generated so far.

# This module will allow me to use the function of sys.exit so as to exit the program when needed
import sys

# This list will hold all instances of class car
cars_list = []


class Car:
    # The __init__ method has been modified to accept parameters containing information about the car, and it will
    # initialize the instance variables to the parameters passed to it
    def __init__(self, model, release_year, acquisition_year, plate_number):
        self.model = model
        self.release_year = release_year
        self.acquisition_year = acquisition_year
        self.plate_number = plate_number
        self.times_rented = 0
        self.generated_money = 0
        self.status = "Available"
        cars_list.append(self)  # The instance will automatically be appended to the list upon creation

    # This method will represent class instances as strings when printing them
    def __repr__(self):
        return 'model:' + str(self.model) + ',year_of_release :' + str(self.release_year) + \
               ',year_bought :' + str(self.acquisition_year) + ',generated_money :' + str(
            self.generated_money) + ',plate_nbr' \
                                    ' :' + str(self.plate_number) + ',times_rent :' + str(
            self.times_rented) + ',status :' + str(self.status) + '\n'

    # This method will be called when the user needs to rent a car. It will check if the calling instance's status is
    # available before it can be rent, increment the number of times it has been rented, and the money it has generated
    # by the money it is going to be rent for.
    def rent(self):
        if self.status.upper() == "AVAILABLE":
            self.times_rented += 1
            self.status = "Rent"
            self.generated_money += int(input("Please enter the fees for which the car will be rent: "))
            print("The car has been successfully rent.")
        else:
            print("Car not available")

    # This method will change the calling instance's status to a new status specified by the user
    def car_status(self, sta):
        self.status = sta
        print("The car's new status is " + self.status)

    # This method will show the user the number of times a car has been rented and the money it has generated so far.
    def track(self):
        print(f"This car has been rented {self.times_rented} times and it has generated {self.generated_money} "
              f"amount of money.")


# Creating the 5 instances (cars) Mr.Omondi is starting with by passing the arguments of car's model, year of release,
# acquisition year and it's plate number
car_1 = Car("VW", "2021", "2021", "RAD345")
car_2 = Car("BMW", "2021", "2021", "RAD346")
car_3 = Car("BUGATTI", "2021", "2021", "RAD347")
car_4 = Car("FERRARI", "2021", "2021", "RAD348")
car_5 = Car("TOYOTA", "2021", "2021", "RAD349")


# this function will print the menu of operations the user can choose from and execute those operations or call other
# functions/methods to do them
def choose_operation():
    operation = int(input("Please enter a digit corresponding to the operation you want to perform:\n"
                          "1.Rent a car\n"
                          "2.Add a new car(s) to the collection\n"
                          "3.Remove a car(s) from the collection.\n"
                          "4.Track the number of times that a car has been rented and the money it has generated so far.\n"
                          "5.Generate a report of the cars in the collection\n"
                          "6.Change a car's status\n"))

    # The following conditions from line 71 to 106 will check if user input is a certain number corresponding to a
    # certain operation and if so execute that operation
    if operation == 1:
        # Asking the user the plate number of the car on which they would like to do the operation to identify it
        pn1 = input("Enter the plate number of the car you would like to rent: ")
        for car in cars_list:  # looping through all instances stored in the list
            # Checking for each object in the list if it's plate number matches the user's specification
            if car.plate_number == pn1.upper():
                car.rent()  # Calling a module which will execute the operation the user wants to do

    if operation == 2:
        # Asking the user the number of cars they would like to add as they could be more than 1
        nbr_of_cars = int(input("how many cars would you like to add? "))
        # This loop will iterate a number of times equal to the number of cars the user wants to add
        for n in range(nbr_of_cars):
            get_car_info()  # Calling the function which will capture the car's information

    if operation == 3:
        # Asking the user the number of cars they would like to delete as they could be more than 1
        n_cars = int(input("how many cars would you like to delete? "))
        # This loop will iterate a number of times equal to the number of cars the user wants to delete
        for m in range(n_cars):
            # Asking the user the plate number of the car on which they would like to do the operation to identify it
            p = input("Enter the plate number of the car you would like to delete: ")
            for item in cars_list:  # looping through all instances stored in the list
                # Checking for each object in the list if it's plate number matches the user's specification
                if item.plate_number == p.upper():
                    cars_list.remove(item)  # Removing the instance from the list we appended it to upon creation
                    del item  # deleting the item entirely where it was stored in the memory

    if operation == 4:
        n_car = int(input("how many cars would you like to track? "))
        # This loop will iterate a number of times equal to the number of cars the user wants to track
        for x in range(n_car):
            # Asking the user the plate number of the car on which they would like track to identify it
            pn2 = input("Enter the plate number of the car you would like to track: ")
            for i in cars_list:  # looping through all instances stored in the list
                # Checking for each object in the list if it's plate number matches the user's specification
                if i.plate_number == pn2.upper():
                    i.track()  # Calling the method which will execute the operation

    if operation == 5:
        print(cars_list)  # Printing information in the instance variables for each car stored in the list

    if operation == 6:
        n_c = int(input("how many cars would you like to change status for? "))
        # This loop will iterate a number of times equal to the number of cars the user wants to track
        for x in range(n_c):
            # Asking the user the plate number of the car on which they would like change status for to identify it
            pn3 = input("Enter the plate number of the car you would like to change status for: ")
            for j in cars_list:  # looping through all instances stored in the list
                if j.plate_number == pn3.upper():
                    stat = input("Enter the car's new status: ")
                    j.car_status(stat)  # Calling the method which will execute the operation and passing the new status

    # Calling the function which will allow the user to perform another operation after the first if they would like
    re_run()


# This function will ask the user to enter the information about the car they would like to add
def get_car_info():
    mod = input("Please enter the model of the new car: ")
    rel_year = input("Please enter the year of release for this car: ")
    acq_year = input("Please enter the year in which this car was acquired by Mr.Omondi: ")
    pl_number = input("Please enter this car's plate number: ")
    print("Car will be added automatically!")
    Car(mod, rel_year, acq_year, pl_number)  # Creating an instance an passing arguments to the init method


# This function will ask the user if they want to do an other operation and call the choose operation function again if
# so, or end the program if the user doesn't want to
def re_run():
    while True:
        operation2 = str(
            input("Enter 'yes' if you would like to do any other operation and 'no' if you do not want to: "))
        if operation2.upper() in ('YES', 'NO'):
            break
        print("invalid input.")
    if operation2.upper() == 'YES':
        choose_operation()
    else:
        sys.exit("Thank you!!")


# This is the main function which will call the choose_operation function.
def main():
    choose_operation()


# This is where the program will start from when running, it is where the main function will be called.
if __name__ == '__main__':
    main()