# julio cesar sanchez saavedra 130232
# suma de los numeros primeros N numeros naturales ,por ejemplo, si la N es 5, la suma seria 
# 1+2+3+4+5.
print("suma de numerois naturales")
n=(int(input("ingrese un numero natural: ")))
n2=0
signo=0
nx=n
for n in range(1,(n+1)):
    print(f"{n}",end="")
    n2=n2+n
    
    if signo<nx-1:
        print("+",end="")
        signo=signo+1
           
#print("") este print es para que de en diferente renglos pero aqui lo desabilitamos.   
print(f"={n2}")