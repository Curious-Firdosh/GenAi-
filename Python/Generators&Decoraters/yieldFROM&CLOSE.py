def parnets():
    yield "Son1"
    yield "Son2"

def againChilds():
    yield from parnets()
    yield "Daughter hui h"


print(list(againChilds()))


def chai_stall () :
    try :
        while True:
            order = yield print("Hellllo Ji Kya chahiye")
    except:
        print("Chai Stall Is Closed")


firdosh = chai_stall()
next(firdosh)
firdosh.close()
