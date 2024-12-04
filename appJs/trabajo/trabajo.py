def suma_tres_anteriores(n, secuencia):
    # Caso base: si ya hemos generado los n términos, devolvemos la secuencia.
    if len(secuencia) >= n:
        return secuencia
    # Caso recursivo: sumamos los tres últimos números de la secuencia.
    siguiente = secuencia[-1] + secuencia[-2] + secuencia[-3]
    secuencia.append(siguiente)
    return suma_tres_anteriores(n, secuencia)

# Ejemplo de uso:
primeros_tres = [2023, 2024, 2025]  # Valores iniciales
n = 100  # Número de términos deseados

resultado = suma_tres_anteriores(n, primeros_tres)
def resultadoFuncion(n):
    for i in range(len(n)):
        print(i)
resultadoFuncion(resultado)
