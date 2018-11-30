class Usuari(object):
    def __init__(self, firstName, lastName, userName, password, email):
        self.__firstName=firstName
        self.__lastName = lastName
        self.userName = userName
        self.__password=password
        self.email=email
        self.r=[]#rentalOffering vinculades a l'usuari

    def __eq__(self, other):
        return self.userName ==other.userName

    def __iter__(self):
        return iter(self.r)

    def __str__(self):
        return "User [firstName= " + self.getFirstName() + ", lastName="+self.getLastName() + ", username=" + self.userName +", email="+self.email + "]"

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getPassword(self):
        return self.__password

    def setPassword(self, value):
        self.__password = value


if __name__ == '__main__':
    apartmentRental = ApartmentRental();

    # Create Users

    uCharles = Usuari("Charles", "Bmith Gates", "bSmith", "123456", "Charles@gmail.com")
    uJohn = Usuari("John", "Pitt Jolie", "Pitt", "123456", "mantinajon@gmail.com")
    uBill = Usuari("Bill", "Adams Jovi", "BillJovi", "123456", "BillJovi@gmail.com")

    # Create RentalOffering

    r1 = RentalOffering("Thameses St 45 ent 4", 80, 3, 2, 689, uBill)
    r2 = RentalOffering(" street 1", 180, 5, 2, 915, uBill)
    r3 = RentalOffering("Square street 34 1B", 50, 1, 1, 945, uJohn)
    r4 = RentalOffering("Round St 2", 90, 2, 2, 689, uJohn)
    r5 = RentalOffering("Kennedy avenue 6", 90, 4, 2, 1600, uJohn)
    r6 = RentalOffering("Johnson avenue 56 4B", 95, 3, 2, 515, uCharles)

    uBill.addRentalOffering(r1)
    uBill.addRentalOffering(r2)

    uJohn.addRentalOffering(r3)
    uJohn.addRentalOffering(r4)
    uJohn.addRentalOffering(r5)

    uCharles.addRentalOffering(r6)

    apartmentRental.addUser(uBill)
    apartmentRental.addUser(uJohn)
    apartmentRental.addUser(uCharles)

    # First Definition
    print
    print "--[Print All Rental Offerings: firts definition]---------------"
    print "---------------------------------------------------------------"

    apartmentRental.printAllRentalOffers()

    apartmentRental.removeUser(uCharles)

    # Delete User Charles
    print
    print "--[Print All Rental Offerings: delete user Charles]--------------"
    print "---------------------------------------------------------------"

    apartmentRental.printAllRentalOffers()

    apartmentRental.deleteRentalOffering(uJohn, r4)

    # Delete Rental Offering r4
    print
    print "--[Print All Rental Offerings: Delete Rental Offering r4-> Round St 2]-----------"
    print "-----------------------------------------------------------------------------------------"

    apartmentRental.printAllRentalOffers()

    apartmentRental.modifyPriceRentalOffering(uJohn, r5, 1800)

    # Modify Price Rental Offering r5
    print
    print "--[Print All Rental Offerings: Modify Price Rental Offering r5-> Kennedy avenue 6]-----------"
    print "--------------------------------------------------------------------------------------------"

    apartmentRental.printAllRentalOffers()


