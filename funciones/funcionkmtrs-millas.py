#julio cesar sanchez saavedra 130232
def KilometroMilla(k):
    milla=k*(1/1.609)
    return milla 

def MillaKilometro(m):
    kilometro=m*(1.609)
    return kilometro

a=(int(input("ingresa los kilometros para transformar a millas:")))
resulrado= KilometroMilla(a)
print(f"{resulrado}")
