#En una empresa se requiere calcular el salario semanal de cada uno de los n obreros que
#laboran en ella. El salario se obtiene de la sig. forma: Si el obrero trabaja 40 horas o menos
#se le paga $20 por hora, Si trabaja más de 40 horas se le paga $20 por cada una de las
#primeras 40 horas y $25 por cada hora extra.

n=int(input("digite el numero de obreros"))

for i in range(n):
    horas=int(input("digite el numero horas que trabaja"))

    salario_base = 20  # Salario por hora regular
    horas_regulares = 40  # Número de horas regulares a pagar
    salario_extra = 25  # Salario por hora extra

    if horas <= horas_regulares:
        salario = salario_base * horas
        print("El salario es del obrero es ", salario)
    else:
        horas_extra = horas - horas_regulares
        salario = (salario_base * horas_regulares) + (salario_extra * horas_extra)
        print("El salario es del obrero es ", salario)