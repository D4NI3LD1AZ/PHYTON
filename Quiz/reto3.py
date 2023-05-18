#Una persona debe realizar un muestreo con 50 personas para determinar el promedio de
#peso de los niños, jóvenes, adultos y viejos que existen en su zona habitacional. Se
#determinan las categorías con base en la siguiente tabla:

#CATEGORIA EDAD
#Niños 0 - 12
#Jóvenes 13 - 29
#Adultos 30 - 59
#Viejos 60 en adelante

can1=0
can2=0
can3=0
can4=0

num = 1
while num <=3:
    edad=int(input("digite su edad "))
    peso=int(input("digite su peso "))

    if edad <=12:
        can1=can1+1
    
    if edad >=13 and edad <29:
        can2=can2+1
    
    if edad >=30 and edad <59:
        can3=can3+1
    
    if edad >=60:
        can4=can4+1
    
    num= num+1


print(f"Niños {can1}")
print(f"Jovenes {can2}")
print(f"Adultos {can3}")
print(f"Viejos {can4}")