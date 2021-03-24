y=float(input("enter the angle 0<y<=2pi"))
h=30
h1=(y/h)
h2=(y//h)
m=((h1-h2)*60)
a=6*m
print ("угол для минутной стрелки","%.2f" % a)
print ("полных часов", h2)
print ("полных минут","%.2f" % m)

