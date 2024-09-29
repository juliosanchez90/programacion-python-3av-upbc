#julio cesar sanchez saavedra 130232
print("donativo para hospital")
print("su donarivo de dividira en ginecologia 40%, traumatologia 30% pediatria 30%.")
donativo=(float(input("ingrese el monto a donar: ")))
gine=donativo*.4
trau=donativo*.3
pedi=donativo*.3
total=gine+trau+pedi
print(f"gracias por donar {total:.2f} $ su donativo a cada area sera")
print(f"Ginecologia : {gine:.2f}$ tramatologia {trau:.2f}$ pediatria {pedi:.2f} $")