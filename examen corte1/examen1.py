#julio cesar sanchez saavedra 130232 calificasion 8.5
#realizar un programa que resulva: en un grupo de 15 alumnos de la upbc, 
#se busca nombrar a un jefe de grupo mediante el voto de cada uno de ellos, todo esto en
#presencia de su maestro asesor. se decidio una votacion.
# los 3 candidadots son 1.hugo,2.paco y 3.luis
#el maestro asesor les solicito que el primer lugar sea el jefe de grupo y el segundo lugar sera tesorero
#A) queremos saber quien sera el jefe de grupo con cuantos votos y porsentaje
#B) queremos saber quien sera el tesorero con cuantos votos y porsentaje
#C) al terser lugar le daremos las gracias por participal
c1=0
hugo=0
paco=0
luis=3
nv=1
vx=15
print("VOTACION PARA ELEJIR JEFE DE GRUPO Y TESORERO")
while c1 < vx:
    
    try: 
        voto=(int(input(f"voto numero: {nv} (ingrese 1-hugo, 2- paco o 3-luis): ")))
        if voto==1:
            hugo=hugo+1
            c1=c1+1
            nv=nv+1 
        elif voto==2:
            paco=paco+1
            c1=c1+1
            nv=nv+1 
        elif voto==3:
            luis=luis+1
            c1=c1+1
            nv=nv+1
        else:
            print("opcion no valida")
    except ValueError:
        print("entrada no valida")
if hugo>paco and hugo>luis:
    porcentaje=(hugo/vx)*100
    print(f"el nuevo jefe de grupo cera 'Hugo'con la cantidad de votos de {hugo} con {porcentaje} % de votos")
    if paco>luis:
        porcentaje2=(paco/vx)*100
        print(f"el teserero sera paco con {paco} votos ,{porcentaje2}%")
        print("gracias por participar luis C:")
    else:   
        porcentaje2=(luis/vx)*100
        print(f"el teserero sera paco con {luis} votos ,{porcentaje2}%")
        print("gracias por participar paco C:") 
elif paco>hugo and paco>luis:
    porcentaje=(paco/vx)*100
    print(f"el nuevo jefe de grupo cera 'Paco'con la cantidad de votos de {paco} con {porcentaje} % de votos")
    if hugo>luis:
        porcentaje2=(hugo/vx)*100
        print(f"el teserero sera paco con {hugo} votos ,{porcentaje2}%")
        print("gracias por participar luis C:")
    else:
        porcentaje2=(luis/vx)*100
        print(f"el teserero sera paco con {luis} votos ,{porcentaje2}%")
        print("gracias por participar hugo C:")    
else:
    porcentaje=(luis/vx)*100
    print(f"el nuevo jefe de grupo cera 'Luis'con la cantidad de votos de {luis} con {porcentaje} % de votos")
    if hugo>paco:
        porcentaje2=(hugo/vx)*100
        print(f"el teserero sera paco con {hugo} votos ,{porcentaje2}%")
        print("gracias por participar paco C:")
    else:
        porcentaje2=(paco/vx)*100
        print(f"el teserero sera paco con {paco} votos ,{porcentaje2}%")
        print("gracias por participar hugo C:")    