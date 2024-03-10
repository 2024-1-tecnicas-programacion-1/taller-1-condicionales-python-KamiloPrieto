def evaluar(num_victorias_a, num_victorias_b):
    if abs(num_victorias_a - num_victorias_b) > 2 or max(num_victorias_a, num_victorias_b) > 7:
        return "Inválido"
    elif num_victorias_a >= 6 and num_victorias_a - num_victorias_b == 2:
        return "Ganó A"
    elif num_victorias_b >= 6 and num_victorias_b - num_victorias_a == 2:
        return "Ganó B"
    elif num_victorias_a <= 6 and num_victorias_b <= 6:
        return "Aún no termina"
    else:
        return "Inválido"

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
