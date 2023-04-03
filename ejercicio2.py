def resta(a, b, multiplicador1, multiplicador2, lista):
    b[0] = b[0]+ a[0]*(-multiplicador2/multiplicador1)
    if len(a) == 1:
        lista.append(b[0])
    else:
        lista.append(b[0])
        resta(a[1:], b[1:], multiplicador1, multiplicador2, lista)

def gauss(matriz, matrizRes):
    if len(matriz) != 1:
        matrizLocal = []        
        if matriz[0][len(matrizRes)] == 0:
            for fila in matriz[1:]:
                if fila[len(matrizRes)-1] != 0:
                    matriz[0], fila = fila, matriz[0]
                    matriz[0][len(matrizRes)-1] *= -1
                    break
            else:
                #parece que esta saltando todo el rato
                print("esta ocurriendo")
                matrizRes.clear()
                matrizRes.append([0])
                return 
        matrizRes.append(matriz[0])
        for fila in matriz[1:]:
           if fila[len(matrizRes)-1] != 0: 
            lista = []
            resta(matriz[0], fila, matriz[0][len(matrizRes)-1], fila[len(matrizRes)-1], lista)
            matrizLocal.append(lista)
           else:
                matrizLocal.append(fila)
        gauss(matrizLocal, matrizRes)

    else:
        matrizRes.append(matriz[0])

def determinante(matriz):
    lista = []
    listaMultiplicar = []
    print("matriz:", matriz)
    gauss(matriz, lista)
    print("lista gauss:", lista)
    for indice in range(len(lista)):
        listaMultiplicar.append(lista[indice][indice])
    multiplicador = 1
    for indice in range(len(listaMultiplicar)):
        multiplicador *= listaMultiplicar[indice]
    return multiplicador