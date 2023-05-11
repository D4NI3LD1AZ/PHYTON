#1. Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a
#la semana. Su política de pagos es que un vendedor recibe un sueldo base y un 10% extra
#por comisiones de sus ventas. El gerente de su compañía desea saber cuánto dinero
#obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas
#realizadas, y cuánto gana tomando en cuenta su sueldo base y sus comisiones.

o=1
n=int(input("Ingrese el numero de vendedores "))
while o<=n: 
    v=((100000*100)/10)*3+100000
    print(f"Lo que esta ganado el vendedor es{v}")
    o=o+1