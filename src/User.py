class User(object):
    def __init__(self, nick, email, password):
        self.nick=nick
        self.__email=email
        self.__password=password

    def __str__(self):
        return "Usuari: "+self.nick + " Email: " + self.getEmail() + " Encripted password: " +

    def getEmail(self):
        return self.__email