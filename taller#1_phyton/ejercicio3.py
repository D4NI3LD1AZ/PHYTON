#En una llantera se ha establecido una promoción de las llantas marca “Ponchadas”,dicha promoción consiste en lo siguiente
# Si se compran menos de cinco llantas el precio es de $300 cada una,
# de $250 si se compran de cinco a 10 y
# de $200 si se compran más de 10.
# Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compra y la que tiene que pagar por el total de la compra.


print ("dijite el numero de llantas va a comprar")
num_llantas= int (input())


if num_llantas < 5 :

    total=num_llantas* 300
    print("el valor de las llantas que compro es de",total)

elif num_llantas > 5 and num_llantas < 10:

    total2=num_llantas* 250
    print("el valor de las llantas que compro es de",total2)

elif num_llantas > 10:

    total3=num_llantas* 200
    print("el valor de las llantas que compro es de",total3)