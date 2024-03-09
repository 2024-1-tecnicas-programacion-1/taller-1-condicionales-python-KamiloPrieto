def evaluar(anno):
    # TODO: 
    if anno % 4 != 0:
        return str(anno) + " no es bisiesto"
    elif anno % 100 != 0:
        return str(anno) + " es bisiesto"
    elif anno % 400 == 0:
        return str(anno) + " es bisiesto"
    else :
        return str(anno) + " no es bisiesto"
    

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
