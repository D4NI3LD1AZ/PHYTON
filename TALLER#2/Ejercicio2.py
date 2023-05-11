#En una tienda de descuento las personas que van a pagar el importe de su compra llegan a
#la caja y sacan una bolita de color, que les dirá que descuento tendrán sobre el total de su
#compra. Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta
#que cierra.
 #Se sabe que, si el color de la bolita es rojo, el cliente obtendrá un 40% de
#descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.

o=1
n=int(input("digite el numero de clientes "))
while o <=n:
    precio=int(input("digite el valor de las compras "))
    bola=int(input("digite el color de la bolita que sacaron ,1 rojo ,2 amarillo ,3 blanca "))
    if bola==1:
        desc=precio*100/40
        total=desc-precio
        print(f"el precio total a pagar es de {total} ")
    if bola==2:
        desc=precio*100/25
        total=desc-precio
        print(f"el precio total a pagar es de {total} ")
    if bola==3:
        print(f"el precio total a pagar es de {precio} ")
        