invitados=[]
invitados.append(input("Nombre del Invitado: "))
print(invitados)

otro=input("desea agregar otro s/n: ")

while otro == "s":
    invitados.append(input("Nombre del Invitado: "))
    print(invitados)
    otro=input("desea agregar otro s/n: ")
    
print("usted tiene",len(invitados),"invitados")
invitados.sort()
print(invitados)
    
   