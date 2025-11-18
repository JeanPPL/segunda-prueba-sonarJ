import math

# Nombre del archivo: calidad.py

# Funcion con alta complejidad ciclomática y muchos if/elif
# SonarQube lo califica como un "Code Smell" por complejidad.
def calcular_area_o_volumen(tipo, valor1, valor2=1):
    
    # Bug: La variable 'PI' nunca se usa, pero se declara.
    # SonarQube lo marca como un Code Smell: Unused Variable
    PI = 3.14159 

    # Condición 1: Alta complejidad
    if tipo == 'circulo':
        if valor1 > 0:
            return math.pi * valor1 ** 2
        else:
            return "Error: Radio debe ser positivo."
            
    # Condición 2: Alta complejidad
    elif tipo == 'rectangulo':
        if valor1 > 0 and valor2 > 0:
            area = valor1 * valor2 # Se podría optimizar
            return area
        else:
            return "Error: Lados deben ser positivos."
            
    # Condición 3: Alta complejidad
    elif tipo == 'esfera':
        if valor1 > 0:
            # Uso de "número mágico" (4/3)
            # Esto puede ser marcado como un Code Smell o Bug potencial
            return (4/3) * math.pi * valor1 ** 3
        else:
            return "Error: Radio debe ser positivo."
            
    # Condición 4: Alta complejidad
    else:
        # SonarQube podría marcar este path como poco claro o incompleto
        print("Tipo de figura no reconocido.") 
        return None

# Llamadas de prueba (El scanner no necesita esto, pero ayuda a probar la función)
# resultado = calcular_area_o_volumen('rectangulo', 10, 5)
# print(f"El área del rectángulo es: {resultado}")