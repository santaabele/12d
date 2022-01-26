mala=float(input("Ievadi malas garumu centimetros"))
s1=mala**2
s2=(mala+5)**2
starpiba=s2-s1
s_izmaina=(starpiba/s1)*100
print(mala,s1,s2,s_izmaina)
print(f"Kvadrāta laukums mainījās par {round(s_izmaina,2)} procentiem")