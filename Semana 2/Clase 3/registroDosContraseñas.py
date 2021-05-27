
contraseñasIguales = False

while contraseñasIguales == False:
    contraseña1 = input("ingrese la contraseña1: ")
    contraseña2 = input("ingrese la contraseña2: ")
    if contraseña1 == contraseña2:
        contraseñasIguales = True
    else:
        print("Las contraseñas son diferentes. Por favor ingreselas nuevamente.")

print("Las contraseñas coinciden. El registro se ha efectuado de manera correcta.")