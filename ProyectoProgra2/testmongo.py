import pymongo
def getEncuestador():
    Censo = pymongo.MongoClient("mongodb://localhost:27017")
    db = Censo["Usuario"]
    tbl = db["tUsuario"]
    return tbl.find()


def getNumeroRegistrosEncus():
    Censo = pymongo.MongoClient("mongodb://localhost:27017")
    db = Censo["Usuario"]
    size = db.command("collstats", "tUsuario")
    return size["count"]

def getAdmi():
    Censo = pymongo.MongoClient("mongodb://localhost:27017")
    db = Censo["Usuario"]
    tbl = db["tAdministrador"]
    return tbl.find()
def getNumeroRegistrosAdmi():
    Censo = pymongo.MongoClient("mongodb://localhost:27017")
    db = Censo["Usuario"]
    size = db.command("collstats", "tAdministrador")
    return size["count"]
