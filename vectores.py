import mathcplx as lc
import math


def adicionVectores(v,w,z):
    if z=='resta':
        w=multscalar((-1,0),w)
    if (len(v) != len(w)):
        return "NO"
    suma=[(0,0) for i in range(len(v))]
    for i in range(0, len(v)):
        suma[i]=lc.sumacplx(v[i],w[i])
    return suma

def multscalar(c,v):
    mult=[(0,0) for i in range(len(v))]
    for i in range(0,len(v)):
        mult[i]=lc.multcplx(c,v[i])
    return mult

def inversoVectorAdd(v):
    inv=[(0,0) for i in range(len(v))]
    for i in range(0,len(inv)):
        inv[i]=(v[i][0]*-1,v[i][1]*-1)
    return inv

def matricesAdd(v,w,z):
    if(len(v)!=len(w)):
        return 'No'
    if(len(v[0])!=len(w[0])):
        return 'No'

    newMatrix=[(0,0) for i in range(len(v))]

    for i in range(len(v)):
        newMatrix[i]=adicionVectores(v[i],w[i],z)

    return newMatrix

def inversaMatrizAdd(v):
    newMatrix = []
    for i in range(len(v)):
        newMatrix.append([])
        for j in range(len(v[0])):
            newMatrix[i].append(None)

    for i in range(0,len(v)):
        for j in range(0,len(v[i])):
            newMatrix[i][j]=v[i][j][0]*-1,v[i][j][1]*-1


    return newMatrix

def multiplicacionMatrizScalar(c,v):
    newMatrix = []
    for i in range(0,len(v)):
        newMatrix.append(multscalar(c,v[i]))

    return newMatrix

def transpuestaMV(v):
    transpuesta=[]

    for i in range(len(v[0])):
        transpuesta.append([])
        for j in range(len(v)):
            transpuesta[i].append(v[j][i])

    return transpuesta

def conjugadaMV(v):
    conjugada=[]
    for i in range(len(v)):
        conjugada.append([])
        for j in range(len(v[i])):
            conjugada[i].append((v[i][j][0],v[i][j][1]*-1))
    return conjugada

def dagaMV(v):
    return transpuestaMV(conjugadaMV(v))

def prodMv(v,w):
    if len(v)!=len(w[0]):
        return 'No'

    prod=[]
    i=0
    while i<len(v[0]):
        prod.append([])
        j=0
        while j<len(w):
            k=0
            suma=(0,0)

            while k<len(v):

                suma=lc.sumacplx(suma,lc.multcplx(v[k][i],w[j][k]))
                k+=1
            prod[i].append(suma)
            j+=1
        i+=1


    return transpuestaMV(prod)

def prodInterno(v,w):
    daga=dagaMV(v)
    return prodMv(daga,w)

def normaV(v):
    return math.sqrt(prodInterno(v,v)[0][0][0])

def distanciaVectores(v,w):
    gap=adicionVectores(v,w,'resta')
    print(gap)
    return normaV([gap])

def matrizU(v):
    matrizIdentidad=[]
    for i in range(len(v)):
        matrizIdentidad.append([])
        for j in range(len(v[0])):
            matrizIdentidad[i].append((0,0))
            if i==j:
                matrizIdentidad[i][j]=(1,0)
    daga=dagaMV(v)
    valor1=prodMv(v,daga)
    valor2=prodMv(daga,v)
    if valor1==valor2:
        if valor1==matrizIdentidad:
            if valor2==matrizIdentidad:
                return 'Matriz Unitaria'
    return 'Matriz no Unitaria'


def matrizH(v):
    h=dagaMV(v)
    if h==v:
        return 'Matriz Hermitiana'
    return 'Matriz no Hermitiana'


def tensorMV(v,w):
    tensor=[]
    for i in range(len(v)*len(w)):
        tensor.append([])
        for j in range(len(v[0])*len(w[0])):
            tensor[i].append(None)

    for k in range(len(tensor)):
        for j in range(len(tensor[k])):
            #print(v[k//len(w)][j//len(w[0])])
            #print(w[k%len(w)][j%len(w[0])])
            tensor[k][j]=lc.multcplx(v[k//len(w)][j//len(w[0])],w[k%len(w)][j%len(w[0])])

    return tensor



#print(adicionVectores([(-5, -6), (-6, -8)],[(5,6),(6,8)],'resta'))
#print(multscalar((2,3),[(5,6),(6,8)]))
#print(inversoVectorAdd([(5,6),(6,8)]))
#print(matricesAdd([[(5,4),(17,12)], [(8,-2),(1,3)]],[[(2,6),(5,8)],[(5,1),(2,5)]],'suma'))
#print(inversaMatrizAdd([[(5,4),(17,12)], [(8,-2),(1,3)]]))
#print(multiplicacionMatrizScalar((5,9),[[(5,4),(17,12)], [(8,-2),(1,3)]]))
#print(transpuestaMV([[(5,4),(17,12)], [(8,-2),(1,3)]]))
#print(conjugadaMV([[(5,4),(17,12)], [(8,-2),(1,3)], [(8,-2),(1,3)]]))
#print(dagaMV([[(5,4),(17,12)], [(8,-2),(1,3)], [(8,-2),(1,3)]]))
#print(prodMv([[(3,2),(1,0),(4,-1)],[(0,0),(4,2),(0,0)],[(5,-6),(0,1),(4,0)]],[[(5,0),(0,0),(7,-4)],[(2,-1),(4,5),(2,7)],[(6,-4),(2,0),(0,0)]]))
#print(prodMv([[(-1,0),(2,-1),(0,0)],[(1,1),(0,0),(1,-1)],[(0,0),(1,0),(0,1)]],[[(1,0),(1,1),(0,1)]])) #Matriz sobre un vector
#print(prodInterno([[(1,0),(0,1),(1,-3)]],[[(2,1),(0,1),(2,0)]]))
#print(normaV([[(6,3.3),(4.9,-5.8)]]))
#print(distanciaVectores([(-5, -6), (-6, -8)],[(3,1),(8,5)]))
#print(matrizU([[(1/2,1/2),(1/2,-1/2)],[(1/2,-1/2),(1/2,1/2)]]))
#print(matrizH([[(5,0),(4,-5),(6,16)],[(4,5),(13,0),(7,0)],[(6,-16),(7,0),(-2.1,0)]]))
#print(tensorMV([[(1,0),(3,0)],[(2,0),(1,0)]],[[(0,0),(2,0)],[(3,0),(1,0)]]))
#print(matrizU([[(0,2),(0,0)],[(0,0),(0,-2)]]))
#print(transpuestaMV(tensorMV([[(1,0),(2,0),(5,0)]],[[(4,0),(-3,0)]])))
#print(tensorMV([[(0,0),(1,0)],[(1,0),(0,0)]],[[(1/math.sqrt(2),0),(1/math.sqrt(2),0)],[(1/math.sqrt(2),0),(-1/math.sqrt(2),0)]]))


