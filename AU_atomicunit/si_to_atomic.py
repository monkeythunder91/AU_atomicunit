
#---------------------------Energy-----------------------------------
def eVtoAtomic(eV):
    return eV / 27.211386245988


def meVtoAtomic(meV):
    return eVtoAtomic(meV) / 1000

#---------------------------Energy-----------------------------------


#---------------------------Time-----------------------------------


def stoAtomic(s):

    return s / (2.418884326*(10**-17))

def pstoAtomic(ps):

    return stoAtomic(ps)*(10**-12)

#---------------------------Time-----------------------------------
