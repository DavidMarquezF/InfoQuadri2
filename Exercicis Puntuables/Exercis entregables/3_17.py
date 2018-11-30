import string
class RLE(object):
    def __init__(self,seq):
        self.releSeq =seq
        self.encode()


    def __str__(self):
        return str(self.releSeq)
    def encode(self):
        """
        saves the RLE-encoded string
        """
        lastLetter=""
        counter=0
        finalStr=""
        for let in self.releSeq:
            if(let != lastLetter):
                if(lastLetter != "" or counter != 0):
                    finalStr+=str(counter) + lastLetter
                counter = 0
                lastLetter = let
            counter+=1
        finalStr +=str(counter) + lastLetter
        self.releSeq = finalStr



    def decode(self):
        """
        returns the string corresponding to the RLE-encoded string for the class instance
        """
        lastNumber=""
        txtFinal=""
        for let in self.releSeq:
            if(let not in string.digits):
                if(len(lastNumber) != 0):
                    txtFinal+="".join([let for i in range(int(lastNumber))])
                lastNumber=""
            else:
                lastNumber+=let
        return txtFinal

if(__name__ == "__main__"):
    a ="BBBBBBBBBBBBNBBBBBBBBBBB"
    r = RLE(a)
    print "codificacio", r
    print "decodificacio", r.decode()