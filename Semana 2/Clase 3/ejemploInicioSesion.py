#pedirle al usuario que ingrese su contraseña

#si la contraseña coincide con storedPassowrd, mostrarle un mensaje
#de inicio de sesión correcto

#si la contraseña no coincide, mostrarle un mensaje de error
#y pedirle la contraseña nuevamente

maxRetries = 3
storedPassword = "123abc"
userPassword = input("Por favor ingrese su contraseña: ")
cont = 1

while storedPassword != userPassword and cont < maxRetries:
    print("las contraseñas no coinciden")
    cont = cont + 1
    # cont += 1
    print("valor del contador", cont)
    userPassword = input("Por favor ingrese nuevamente la contraseña: ")

if cont >= maxRetries:
    print("Te equivocaste más de 3 veces. Te hemos bloqueado.")
else:
    print("¡inicio de sesión exitoso!")