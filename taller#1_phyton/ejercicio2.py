#En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número de computadoras que compre. Si las computadoras son menos
#de cinco se les dará un 10% de descuento sobre el total de la compra; si el número de computadoras es mayor o igual a cinco, pero menos de diez se le otorga un 20% de
#descuento; y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de $15,000

print ("Dijite el numero de computadores que va a comprar")
num_compu = int (input())

total_venta= num_compu * 15000


if num_compu < 5:

    desc1= total_venta * 0.1
    total1= total_venta - desc1
    print("Señor comprador usted compro ", num_compu," computadoras y tiene un descuento del 10%, lo que tiene que pagar es: ",total1)

elif num_compu >5 and num_compu > 10:

    desc2= total_venta * 0.2
    total2 = total_venta - desc2
    print("Señor comprador usted compro ", num_compu," computadoras y tiene un descuento del 20%, lo que tiene que pagar es: ",total2)

else:

    descuento3= total_venta * 0.4
    total3= total_venta - descuento3
    print("Señor comprador usted compro ", num_compu," computadoras y tiene un descuento del 40%, lo que tiene que pagar es: ",total3)