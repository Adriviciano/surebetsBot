def encontrar_surebet(cuotas_casa1, cuotas_casa2):
    mejor_surebet = -1  # Inicializamos con un valor que indica que no hay surebet rentable
    mejor_ganancia_esperada = 0  # Inicializamos con 0 ganancia esperada
    mejor_valor_apuesta_casa1 = 0  # Inicializamos con 0 el valor de apuesta en Casa 1
    mejor_valor_apuesta_casa2 = 0  # Inicializamos con 0 el valor de apuesta en Casa 2

    for i in range(len(cuotas_casa1)):
        valor_apuesta_casa1 = cuotas_casa2[i] / (cuotas_casa1[i] + cuotas_casa2[i])  # Valor de apuesta en Casa 1
        valor_apuesta_casa2 = cuotas_casa1[i] / (cuotas_casa1[i] + cuotas_casa2[i])  # Valor de apuesta en Casa 2
        inversión_total = valor_apuesta_casa1 + valor_apuesta_casa2

        ganancia_casa1 = valor_apuesta_casa1 * cuotas_casa1[i] - inversión_total
        ganancia_casa2 = valor_apuesta_casa2 * cuotas_casa2[i] - inversión_total

        if ganancia_casa1 > 0 and ganancia_casa2 > 0:  # Si ambas apuestas son rentables
            ganancia_esperada = (ganancia_casa1 + ganancia_casa2) / 2  # Ganancia esperada promedio
            if ganancia_esperada > mejor_ganancia_esperada:
                mejor_ganancia_esperada = ganancia_esperada
                mejor_surebet = i
                mejor_valor_apuesta_casa1 = valor_apuesta_casa1
                mejor_valor_apuesta_casa2 = valor_apuesta_casa2

    if mejor_surebet >= 0:
        return [mejor_surebet, mejor_ganancia_esperada, mejor_valor_apuesta_casa1, mejor_valor_apuesta_casa2]
    else:
        return []

# Ejemplo de uso:
cuotas_casa1 = [1.65]
cuotas_casa2 = [2.15]
resultado = encontrar_surebet(cuotas_casa1, cuotas_casa2)

if resultado:
    posicion_surebet, mejor_ganacia_esperada, valor_apuesta_casa1, valor_apuesta_casa2 = resultado
    print(f"Surebet rentable en la posición {posicion_surebet}")
    print(f"Ganancia esperada: {round(mejor_ganacia_esperada * 10, 2)}")
    print(f"Valor de apuesta en Casa 1: {round(valor_apuesta_casa1 * 10, 2)}")
    print(f"Valor de apuesta en Casa 2: {round(valor_apuesta_casa2 * 10, 2)}")
else:
    print("No hay surebets rentables.")
