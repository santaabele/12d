import math

radiuss=float(input("Ievadi riņķa rādiusu centimetros"))
hipotenuza=float(input("Ievadi hipotenuzas garumu centimetros"))
mala=math.sqrt(hipotenuza/2)

starpiba=((math.pi*(radiuss**2))-((mala**2)/2))
print(f"Riņķa laukums ir par {round(starpiba,1)} kvadrātcentimetriem lielāks nekā trijstūra laukums")