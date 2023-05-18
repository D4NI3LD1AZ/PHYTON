#El gobierno de Colombia, desea reforestar un bosque que mide determinado número de
#hectáreas. Si la superficie del terreno excede a 1 millón de metros cuadrados, entonces
#decidirá sembrar de la siguiente manera:
#a. Porcentaje de la superficie del bosque Tipo de árbol
#70% pino
#20% oyamel
#10% cedro
#b. Si la superficie del terreno es menor o igual a un millón de metros cuadrados,
#entonces decidirá sembrar de la sig. manera:
#Porcentaje de la superficie del bosque Tipo de árbol
#50% pino
#30% oyamel
#20% cedro

print ("dijite el numero de hectareas")
num_hectareas= int (input())

hectareas= num_hectareas *10000

if hectareas > 1000000:
    Pinos= hectareas*(70/100)
    Oyamel= hectareas*(20/100)
    Cedro= hectareas*(10/100)
    print ("Se sembraran Pinos en el ", Pinos)
    print ("Se sembraran Oyamel en el",Oyamel)
    print ("Se sembraran Cedro en el", Cedro)

elif hectareas <= 1000000:
        Pinos= hectareas*(50/100)
        Oyamel= hectareas*(30/100)
        Cedro= hectareas*(20/100)
        print ("Se sembraran Pinos en el ", Pinos)
        print ("Se sembraran Oyamel en el", Oyamel)
        print ("Se sembraran Cedro en el",Cedro)
