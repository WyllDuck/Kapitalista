import pandas as pd
import numpy as np
from scipy import stats

#Se leen los archivos

dpers = pd.read_csv('logic/dpersnomespreinsc18v2.csv')
dfase_ini = pd.read_csv('logic/qfaseini18v2.csv')
dfase_noini = pd.read_csv('logic/qfasenoini18v2.csv')
drenta = pd.read_csv('logic/Definitiv.csv')
default = [0,13500, 18000,20000, 23000, 30000, 50000]
default2 = [0,13500,13500, 18000,18000 , 20000, 20000, 23000, 23000, 30000, 30000 , 50000]

#funcion que calcula la nota media para la franja de renta [n,m]
#para una asignatura en concretro, si i = 0 --> cp centre si i = 1 --> cp centre

def fase_ini(codass):
    return (codass >= 240011 and codass < 240026) 

def desglose(codass, n, m, i):
    codass = int(codass)
    w = [0]*2
    if (fase_ini(codass)):
        nota = dfase_ini[ dfase_ini['CODASS'] == codass ]
    else:
        nota = dfase_noini[ dfase_noini['CODASS'] == codass ]
    comunes = dpers[ dpers.CODEX.isin(nota.CODEX) ]
    if(i):
        comunes = comunes[ comunes.RC >= n]
        comunes = comunes[ comunes.RC < m]
    else:
        comunes = comunes[ comunes.RF >= n]
        comunes = comunes[ comunes.RF < m]
    nota = nota[nota.CODEX.isin(comunes.CODEX)]
    w[0] = len(nota.CODEX)
    w[1] = nota['NF'].mean()
    return w

def separacion(codass,franjas, i):
    n = int(len(franjas)/2)
    v = [0] * n
    for j in range(n):
        w = desglose(codass, franjas[2*j], franjas[2*j+1], i)
        if (w[0] > 70):
            v[j] = w[1]
        else:
            return False
    return v


#mismo procedimiento pero con las notas de SELE

def desglose_sele(n, m, i):
    franja = dpers
    v = [0]*2
    if(i):
        franja = franja[ franja.RC >= n]
        franja = franja[ franja.RC < m]
    else:
        franja = franja[ franja.RF >= n]
        franja = franja[ franja.RF < m]
    v[0] = len(franja.CODEX) 
    v[1] = franja['SELE'].mean()
    return(v)

def separacion_sele(franjas, i):
    n = int(len(franjas)/2)
    v = [0] * n
    for j in range(n):
        w = desglose_sele(franjas[2*j], franjas[2*j+1], i)
        if (w[0]>=50):
            v[j] = w[1]
        else:
            return False
    return v

                
def medias(v, franjas, i):   
    n = len(v)
    f = [0]*int(len(franjas)/2)
    M = [f]*n
    for j in range(n):
        if(v[j] == 'SELE'):
            M[j] = separacion_sele(franjas, i)
        else:
            M[j] = separacion(v[j], franjas,i)
        if (M[j] == False):
            return False
    return M

#cuenta el efectivo de alumnos en cada franja de rent a[n,m] del dataframe nota

def cuenta(nota, n, m, i):
     comunes = dpers[dpers.CODEX.isin(nota.CODEX)]
     if(i):
         comunes = comunes[ comunes.RC >= n]
         comunes = comunes[ comunes.RC < m]
     else:
         comunes = comunes[ comunes.RF >= n]
         comunes = comunes[ comunes.RF < m]
     nota = nota[nota.CODEX.isin(comunes.CODEX)]
     return(nota['NF'].count())
    
#devuelve la separacion por renta de los (p*100) % mejores
#las franjas son elegidas de manera que su efectivo total
#en el dataframe nota sea parecido

def equilibrar(nota, i):
    equilibrado = [0]*7
    rt = []
    for j in range(len(nota.CODEX)):
        a = nota.iloc[j].CODEX
        rt.append(renta(a, i))
    nota['RT'] = rt
    for j in range(6):
        equilibrado[j] = int(nota.RT.quantile(j/6))

    equilibrado[0] = 0 
    equilibrado[6] = 60000    
    return equilibrado    

def mejores(codass, p, i):
    if (fase_ini(codass)):
        nota = dfase_ini[dfase_ini['CODASS'] == codass]
    else:
        nota = dfase_noini[dfase_noini['CODASS'] == codass]
    cuantil = nota.NF.quantile(1-p)
    w = equilibrar(nota,i)
    nota = nota[nota['NF'] >= cuantil]
    n = len(nota.NF)
    v = [0]*6
    for j in range(6):
        v[j] = (cuenta(nota, w[j], w[j+1], i)/n)*100
    return [v,w]


def peores(codass, p, i):
    if (fase_ini(codass)):
        nota = dfase_ini[dfase_ini['CODASS'] == codass]
    else:
        nota = dfase_noini[dfase_noini['CODASS'] == codass]
    cuantil = nota.NF.quantile(p)
    w = equilibrar(nota,i)
    nota = nota[nota['NF'] <= cuantil]
    n = len(nota.NF)
    v = [0]*6
    for j in range(6):
        v[j] = (cuenta(nota, w[j], w[j+1], i)/n)*100
    return [v,w]

#grafo 1

def aux(a, b, codass, i):
    if (fase_ini(codass)):
        nota = dfase_ini[dfase_ini['CODASS'] == codass]
    else:
        nota = dfase_noini[dfase_noini['CODASS'] == codass]
    nota = nota[nota['NF'] <= b]
    nota = nota[nota['NF'] >= a]
    v = [0]*6
    for j in range(6):
        v[j] = cuenta(nota, default[j], default[j+1], i)
    return v
    
def graf1(codass, i):
    f = [0]*6
    M = [f]*10
    for j in range(10):
        M[j] = aux(j,j+1,codass, i)
    return M

#regresion lineal renta v.s. NF

def renta(codex, i):
    if (i):    
        renta = dpers[dpers.CODEX == codex].iloc[0]['RC']
    else :
        renta = dpers[dpers.CODEX == codex].iloc[0]['RF']
    return renta
  
def reg_lineal(codass, i):
    if (fase_ini(codass)):
        nota = dfase_ini[dfase_ini['CODASS'] == codass]
    else:
        nota = dfase_noini[dfase_noini['CODASS'] == codass]
    comunes = dpers[ dpers.CODEX.isin(nota.CODEX)]
    nt, rent = [],[]
    for j in range(len(nota.NF)):
        a = nota.iloc[j].CODEX
        if(a != 'NaN' or a != 'nan'):
            nt.append(nota.iloc[j].NF)
            rent.append(renta(a, i))   
    x = np.array(rent)
    y = np.array(nt)
    mask = ~np.isnan(x) & ~np.isnan(y)
    m, c, r, p, std_err = stats.linregress(x[mask],y[mask])
    v = [m, c, nt, rent]
    return v

#pones tu cp y te da la renta

def codigo_p(str_cp):
    cp = int(str_cp)
    aux = drenta[drenta.CP == cp]
    if(len(aux.CP) == 0):
        return False
    aux = str(aux.NETA.iloc[0])
    return round(float(aux.replace(',','.')))