# hacer una función que reciba dos strings con números
#y que reciba una operación.
    #puede recibir las operaciones "suma", "multiplicacion", "division", "resta"
#la función debe ejecutar la operación recibida para cada uno
# de los números recibidos en los strings
#ejemplo string 1: '123456'
#        string 2: '824136'
#        operacion: 'suma'
# la función debe retornar
#                  '9475812'

def calculoNumeroANumero(string1,string2,operacion):
    print("longitud: ",len(string1))
    resultado = ''
    for i in range(len(string1)):
        print(f"caracter {i} del string1",string1[i])
        print(f"caraceter {i} del string2",string2[i])
        if operacion == "suma":
            resultadoNumero = int(string1[i]) + int(string2[i])
            resultado = resultado + str(resultadoNumero)
        elif operacion == "resta":
            resultadoNumero = int(string1[i]) - int(string2[i])
            resultado = resultado + str(resultadoNumero)
        elif operacion == "multiplicacion":
            resultadoNumero = int(string1[i]) * int(string2[i])
            resultado = resultado + str(resultadoNumero)
        elif operacion == "division":
            resultadoNumero = int(string1[i]) / int(string2[i])
            resultado = resultado + str(resultadoNumero)
    return resultado


st1='123456'
st2='824136'
resultado = calculoNumeroANumero(st1,st2,'division')
print("resultado final",resultado)