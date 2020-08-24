#import math
import numpy as np
def adicion_vec(c1,c2):
    if len(c1) != len(c2): return "Dimensiones incorrectas"
    for i in range(len(c1)):
        c1[i]=c1[i]+c2[i]
    return c1
def inverso_aditivo(c1):
    for i in range(len(c1)):
        c1[i] = c1[i]*-1
    return c1
def mult_esc_vec(c1,c2):
    for i in range(len(c2)):
        c2[i]=c2[i]*c1
def adicion_matriz(c1,c2):
    a, b = np.shape(c1), np.shape(c2)
    if a != b:return "Dimensiones incorrectas"
    for i in range(a[0]):
        for j in range(a[1]):
            c1[i][j] = c1[i][j]+c2[i][j]
    return c1
def invesa_adi_matriz(c1):
    for i in range(len(c1)):
        for j in range(len(c1)):
            c1[i][j] = c1[i][j]*-1
    return c1
def mult_esc_matrizcomp(a,c1):
    b = np.shape(c1)
    for i in range(b[0]):
        for j in range(b[1]):
            c1[i][j]=c1[i][j]*a 
    return c1
def transpuesta(c1):
    t = []
    for i in range(len(c1[0])):
        t.append([])
        for j in range(len(c1)):
            t[i].append(c1[j][i])
    return t
def conjugada(c1):
    a = np.shape(c1)
    for i in range(a[0]):
        for j in range(a[1]):
            c1[i][j]= c1[i][j].conjugate()
    return c1
def adjunta(c1):
    c1 = conjugada(c1)
    c1 = transpuesta(c1)
    return c1
def producto_matrices(c1,c2):
    res = []
    a, b = np.shape(c1), np.shape(c2)
    if a[1] != b[0]:return "Dimensiones incorrectas"
    for i in range(len(c1)):
        res.append([])
        for j in range(len(c2[0])):
            res[i].append(0)
    for i in range(len(c1)):
        for j in range(len(c2[0])):
            for k in range(len(c1[0])):
                res[i][j] += c1[i][k]*c2[k][j]
    return res
def accion_mat_vec(c1,c2):
    res=[]
    a, b = np.shape(c1), np.shape(c2)
    if a[1] != b[0]:return "Dimensiones incorrectas"
    for i in range(len(c1)):
        res.append([])
        for j in range(len(c2[0])):
            res[i].append(0)
    for i in range(len(c1)):
        for j in range(len(c2[0])):
            for k in range(len(c1[0])):
                res[i][j] += c1[i][k]*c2[k][j]
    return res
def producto_inter_vect(c1,c2):
    a, b = np.shape(c1), np.shape(c2)
    if a != b:return "Dimensiones incorrectas"
    res=0
    for i in range(len(c1)):
        res = res+ (c1[i]*c2[i])
    return res
def norma_vect(c1):
    res = 0
    for i in range(len(c1)):
        res+= c1[i]**2
    res = res**0.5
    return res
def distancia_vect(c1,c2):
    a, b = np.shape(c1), np.shape(c2)
    if a != b:return "Dimensiones incorrectas"
    res=0 
    for i in range(len(c1)):
        res =res+ (c1[i]-c2[i])**2
    res=res**0.5
    return res
def mat_unitaria(c1):
    c2=adjunta(c1)
    c1= conjugada(c2)
    res = producto_matrices(c1, c2)
    x = 0
    for i in range(len(res)):
        for j in range(len(res)):
            if i==j:
                if res[i][j]==1:
                    x = "es unitaria"
                else:
                    return "No es unitaria"
            elif i != j:
                if res[i][j]==0:
                    x = "es unitaria"
    return x
def mat_hermitiana(c1):
    c2 = adjunta(c1)
    c3 = conjugada(c2)
    if c2 == c3:return "es hemitiana" 
    else: return "No es hermitiana"
def producto_tensor(c1,c2):
    a, b = np.shape(c1), np.shape(c2)
    if a[1] != b[0]:return "Dimensiones incorrectas"
    res=[]   
    for i in range(a[0]):
        res.append([])
        for j in range(a[1]):
            res[i]=res[i] +[[]]
            for k in range(a[1]):
                for l in range(a[0]):
                    res[i][j] = res[i][j]+[c1[i][j]*c2[k][l]]
    return res    
    
    
    
    
    
    
    