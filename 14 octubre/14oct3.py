# julio cesar sanchez saavedra 130232
pares=0
inpares=0
ceros=0
c1=1
while True:
    try:
        
        num=(int(input("ingrese un numero:")))
        if num==0:
            ceros+=1
            c1=c1+1
        elif num%2!=0:
            inpares+=1
            c1=c1+1
        elif num%2==0:
            pares+=1
            c1=c1+1
        if c1>10:
            break        
    except ValueError:
        print("entrada no valida solo numeros.")
print(f"los numeros pares fueron :{pares} los inpares fueron:{inpares} y los ceros fueron: {ceros}")