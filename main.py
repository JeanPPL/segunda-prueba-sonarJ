def calculadora(num, num2, operacion):
    if operacion == "+":
        return num+num2
    elif operacion == "-":
        return num-num2
    elif operacion == "*":
        return num*num2
    elif operacion == "/":
        return num/num2
    return "Ingrese una opcion valida"


num = int(input("Ingrese un numero ->"))
num2 = int(input("Ingrese otro numero ->"))
operacion = input("Ingrese una operacion ->")
print(calculadora(num,num2, operacion))