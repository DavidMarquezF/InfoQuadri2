import os, MainLib

NomFitUsuaris ="Usuaris.txt"
NomFitPosts ="Posts.txt"
NomFitHashtags ="Hashtags.txt"

def checkFilesExist(fol):
    return (os.path.isfile(fol + "/" +NomFitUsuaris) and os.path.isfile(fol + "/" + NomFitPosts) and os.path.isfile(fol + "/" + NomFitHashtags))
def askFolder():
    while True:
        fol = raw_input("Esculli el directori on hi ha les dades de la iTICApp: ")
        if(not os.path.exists(fol)):
            print "Aquest directori no existeix"
        else:
            if(not checkFilesExist(fol)):
                print "Aquest directori no es el correcte, ja que no conte els fitxers", NomFitUsuaris, NomFitPosts, NomFitHashtags
            else:
                break
    return fol

def prepareFiles(folderName, createDir =True):
    if(createDir):
        os.makedirs(folderName)
    open(folderName+"/"+NomFitUsuaris, "w").close()
    open(folderName + "/" + NomFitPosts, "w").close()
    open(folderName + "/" + NomFitHashtags, "w").close()

def createUseFolder():
    while True:
        fol = raw_input("Esculli un directori on hi vol guardar la informacio: ")
        if(not os.path.exists(fol)):
            prepareFiles(fol)
            return fol
        else:
            if(MainLib.askYorNQuestion("Aquest directori ja existeix. Vol sobreescriure els seus continguts? ")):
                if(not checkFilesExist(fol)):
                    print "Aquest directori no conte els fitxers necessaris. Creant els fitxers..."
                    prepareFiles(fol, False)
                    print "Done"
                return fol

def checkIfTypeExists(type):
    return type == NomFitUsuaris or type == NomFitPosts or type == NomFitHashtags

def writeToFile(folderName, type, lines):
    if not checkIfTypeExists(type):
        print "El tipus no existeix", type
        return False

    try:
        f = open(folderName+"/"+type,"w")
    except IOError as e:
        print "Error al obrir el fitxer",type,":",e.message
        return False
    except Exception as e:
        print "Error al obrir fitxer",":",e.message
        return False

    f.write("\n".join(lines))
    f.close()
    return True

def readlines(folderName, type):
    if not checkIfTypeExists(type):
        print "El tipus no existeix", type
        return False
    try:
        f = open(folderName + "/" + type)
    except IOError as e:
        print "Error al obrir el fitxer",type,":",e.message
        return
    except Exception as e:
        print "Error al obrir fitxer",":",e.message
        return

    l = f.readlines()
    f.close()
    return l
