#1. leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.

print ("dijite el primer numero")
num1= int (input())

print ("dijite el segundo numero")
num2= int (input())

multi = num1 * num2
resta = num1 - num2
suma = num2 + num1

if num1 == num2:
    print ("cuando los dijitos son iguales se multiplican", multi)


elif num1 > num2:
    print("como el primer dijito es mayor que el segundo se resta y el resultado es", resta)

else:
    print("cuando el segundo dijito es mayor que el primero se suma y el resultado es", suma)
