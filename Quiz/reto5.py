precio_boleta=float(input("Digite el valor de la boleta"))
edad=int(input("¿Que edad tienes?"))
if edad >= 5 and edad <=15:
    print("Haz entrado a la primera categoria \n Felicidades tienes un descuento del 35%")
    descuento_1=precio_boleta*0.35
    print("Tendras que pagar ",descuento_1)
    perdida_1=(descuento_1-precio_boleta)
    print("Las perdidas del teatro son de",perdida_1)
elif edad >= 15 and edad<=19:
    print("Haz entrado a la segunda categoria \n Felicidades tienes un descuento del 25%")
    descuento_2=precio_boleta*0.25
    print("Tendras que pagar ",descuento_2)
    perdida_2=(descuento_2-precio_boleta)
    print("Las perdidas del teatro son de: ",perdida_2)
elif edad >= 20 and edad<=45:
    print("Haz entrado a la tercera categoria \n Felicidades tienes un descuento del 10%")
    descuento_3=precio_boleta*0.1
    print("Tendras que pagar ",descuento_3)
    perdida_3=(descuento_3-precio_boleta)
    print("Las perdidas del teatro son de",perdida_3)
elif edad >= 46 and edad<=65:
    print("Haz entrado a la cuarta categoria \n Felicidades tienes un descuento del 25%")
    descuento_4=precio_boleta*0.25
    print("Tendras que pagar ",descuento_4)
    perdida_4=(descuento_4-precio_boleta)
    print("Las perdidas del teatro son de: ",perdida_4)
elif edad >= 66 :
    print("Haz entrado a la quinta categoria \n Felicidades tienes un descuento del 25%")
    descuento_5=precio_boleta*0.35
    print("Tendras que pagar",descuento_5)
    perdida_5=(descuento_5-precio_boleta)
    print("Las perdidas del teatro son de: ",perdida_5)
else:
    print("Lo siento no tienes la edad necesaria")