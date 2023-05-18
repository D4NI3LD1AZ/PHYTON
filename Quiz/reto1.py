#Una persona desea iniciar un negocio, para lo cual piensa verificar cuánto dinero le
#prestara el banco por hipotecar su casa. Tiene una cuenta bancaria, pero no quiere
#disponer de ella a menos que el monto por hipotecar su casa sea muy pequeño.
#a. Si el monto de la hipoteca es menor que $1.000.000, entonces invertirá el 50% de
#la inversión total y un socio invertirá el otro 50%.
#b. Si el monto de la hipoteca es de $ 1.000.000 o más, entonces invertirá el monto
#total de la hipoteca y el resto del dinero que se necesite para cubrir la inversión
#total se repartirá a partes iguales entre el socio y el.

# Ejemplo de 
monto_hipoteca =int(input("digite la cantidad de la hipoteca "))

inversion_total =int(input("digite la inversion total "))


def calcular_inversion(monto_hipoteca, inversion_total):

    if monto_hipoteca < 1000000:
    
        inversion_persona = inversion_total * 0.5
        inversion_socio = inversion_total * 0.5
    
    else:
        inversion_persona = monto_hipoteca

        inversion_restante = inversion_total - monto_hipoteca

        inversion_persona = inversion_restante * 0.5
        inversion_socio = inversion_restante * 0.5

        persona = inversion_persona + monto_hipoteca

    return inversion_persona, inversion_socio, persona

inversion_persona, inversion_socio, persona = calcular_inversion(monto_hipoteca, inversion_total)

print("Inversión de la persona:", persona)
print("Inversión del socio:", inversion_socio)