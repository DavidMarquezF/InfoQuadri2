import base64
def encode(key, string):
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)

class User(object):
    def __init__(self, nick, email, password, posts = []):
        self.nick=nick
        self.__email=email
        self.__password=password
        self.posts = posts

    def __eq__(self, other):
        return self.nick == other.nick

    def __str__(self):
        txt = "Usuari: "+self.nick + " Email: " + self.getEmail() + " Encripted password: " + encode(3, self.__password) + "\n\n" + "Published posts: "
        if(len(self.posts) <= 0):
            txt+="No posts available"
        txt+="\n\n"
        for post in self.posts:
            txt+=str(post) + "\n\n"
        return txt

    def getEmail(self):
        return self.__email

    def registra_post(self, post):
        self.posts.append(post)

