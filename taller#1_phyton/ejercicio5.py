print ("dijite el 1 numero")
n1=int(input())
print ("dijite el 2 numero")
n2=int(input())
print ("dijite el 3 numero")
n3=int(input())

if n1>n2 and n1>n3:
   print ("El numero mayor es ",n1)
elif n2>n1 and n2>n3:
    print ("El numero mayor es ",n2)
elif n3>n1 and n3>n2:
   print ("El numero mayor es ",n3)
else:
    print ("Eror")