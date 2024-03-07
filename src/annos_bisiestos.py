def evaluar(anno):
    # TODO: 
    if anno % 4 == 0:
        print(int(anno), str(' es bisiesto'))
    elif anno % 400 == 0:
        print(int(anno) , str(' es bisiesto'))
    else :
        print(int(anno) , str(' no es bisiesto'))
    return "";

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
