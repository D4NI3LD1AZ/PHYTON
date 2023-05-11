#Un grupo de 100 estudiantes presentan un examen de Física. Diseñe un diagrama que lea
#por cada estudiante la calificación obtenida y calcule e imprima:
# La cantidad de estudiantes que obtuvieron una calificación menor a 50 en el área
#del Tecnólogo en Análisis y Desarrollo de Sistemas de Información.
# La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero
#menor que 70.
# La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero
#menor que 80.
# La cantidad de estudiantes que obtuvieron una calificación de 80 o más.

a=1
con1=0
con2=0
con3=0
con4=0
while a<=100:
    nota=int(input("digite la calificacion del estudiante "))
    if nota<50:
        con1=con2+1
    elif nota>=50 and nota<70:
        con2=con2+1
    elif nota>=70 and nota<80:
        con3=con3+1
    elif nota>=80:
        con4=con4+1
    print(f"la cantidad de estudiantes que tienen una nota menor a 50 son {con1}, entre 50 y 69 son {con2}, entre 70 79 son {con3} , superior o igual a 80 son {con4}")
    a=a+1