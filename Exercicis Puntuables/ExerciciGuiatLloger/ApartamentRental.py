class ApartamentRental(object):
    def __init__(self, users=[]):
        self.users=users
    def __iter__(self):
        return iter(self.users)
    def __len__(self):
        return len(self.users)
    def __str__(self):
        print "Usuaris emmagatzemats: " + len(self)
        for user in self:
            print user
        return ""
    def afegirUsuari(self, user):
        if(user not in self):
            self.users+=[user]
    def removeUser(self, user):
        if(user in self):
            for i, u in enumerate(self):
                if(u==user):
                    del self.users[i]
                    break

class RentalOffering(object):
    def __init__(self, street,squaremeters,numRooms,numBathrooms,price,user):
        self.street=street
        self.sqmeters=squaremeters
        self.numRooms=numRooms
        self.numBathrooms=numBathrooms
        self.price=price
        self.user=user

    def __str__(self):
        return self.street + " " + str(self.sqmeters) + " " + str(self.numRooms) + " "+ str(self.numBathrooms) + " "+str(self.price)