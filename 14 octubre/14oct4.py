# julio cesar sanchez saavedra 130232
dia=1
temtotal=0
tmax=0
tmin=100000000000000000
while dia<8:
    tem=(float(input(F"INGRESE LA TEMPERATURA DEL DIA {dia}: ")))
    temtotal=temtotal+tem
    if tem>tmax:
        tmax=tem
    if tem<tmin:
        tmin=tem   
    dia=dia+1
prom=temtotal/7
print(f"el promedio de temperatura de semana due :{prom:.2f} la maxima: {tmax} la minima{tmin}")    
