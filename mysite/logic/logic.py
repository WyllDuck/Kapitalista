import pandas as pd

#Se leen los archivos

dpers = pd.read_csv('dpersnomespreinsc18.csv')
dfase_ini = pd.read_csv('qfaseini18.csv')
dfase_noini = pd.read_csv('qfasenoini18.csv')
drenta = pd.read_csv('Definitiva.csv')
dasig = pd.read_csv('asignaturas.csv')

franjas = [0, 10000, 15000, 20000, 25000, 30000, 50000]

#nuevas columnas en dpers que son RF(Renta familiar) y RC(Renta centro)

rf = []
rc = []
for codex in dpers['CODEX']:
    cp = dpers[['CODEX'] == codex].iloc[0]['CP_FAM']
    renta = drenta[drenta['CP'] == cp].iloc[0]['NETA']   
    rf.append(renta)
    cp = dpers[['CODEX'] == codex].iloc[0]['CP_CENTRE']
    renta = drenta[drenta['CP'] == cp].iloc[0]['NETA']   
    rc.append(renta)

dpers['RF'] = rf
dpers['RC'] = rc
 

#funcion que calcula la nota media para la franja de renta [n,m]
#para una asignatura en concretro, si i = 0 --> cp centre si i = 1 --> cp centre

def fase_ini(codass):
	return (codass > 240011 and codass < 240026) 

def desglose(codass, n, m, i):
	if (fase_ini(codass)):
            nota = dfase_ini[ dfase_ini['CODASS'] == codass ]
        else:
            nota = dfase_noini[ dfase_noini['CODASS'] == codass ]
        comunes = dpers[ dpers.CODEX.isin(nota.CODEX) ]
        if(i):
            franja = comunes[ comunes.RF > n and comunes.RF  < m]
        else:
            franja = comunes[ comunes.RC > n and comunes.RC  < m]
        nota = nota[nota.CODEX.isin(franja.CODEX)]
        return(nota['NF'].mean())


def separacion(codass, i):
    v = [0] * 6
    for i in range(6):
        v[i] = desglose(codass, franjas[i], franjas[i+1], i)
    return v

#mismo procedimiento pero con las notas de SELE

def desglose_sele(n, m, i):
        if(i):
            franja = dpers[ dpers.RF > n and dpers.RF  < m]
        else:
            franja = dpers[ dpers.RC > n and dpers.RC  < m]
        return(franja['NF'].mean())

def separacion_sele(codass, i):
    v = [0]*6
    for i in range(6):
        v[i] = desglose_sele(franjas[i], franjas[i+1], i)
    return v


#cuenta el efectivo de alumnos en cada franja de renta del dataframe nota

def cuenta(nota, n, m, i):
     comunes = dpers[dpers.CODEX.isin(nota.CODEX)]
     if(i):
         franja = comunes[ comunes.RF > n and comunes.RF  < m]
     else:
         franja = comunes[ comunes.RC > n and comunes.RC  < m]
     nota = nota[nota.CODEX.isin(franja.CODEX)]
     return(nota['NF'].count())
    
#devuelve la separacion por renta de los (p*100) % mejores

def mejores(codass, p, i):
    if (fase_ini(codass)):
        nota = dfase_ini[dfase_ini['CODASS'] == codass]
    else:
        nota = dfase_noini[dfase_noini['CODASS'] == codass]
    cuantil = nota.CODASS.quantile(1-p)
    nota = nota[['CODASS'] >= cuantil]  
    v = [0]*6
    for i in range(6):
        v[i] = cuenta(nota, franjas[i], franjas[i+1], i)
    return v


def peores(codass, p, i):
    if (fase_ini(codass)):
        nota = dfase_ini[dfase_ini['CODASS'] == codass]
    else:
        nota = dfase_noini[dfase_noini['CODASS'] == codass]
    cuantil = nota.CODASS.quantile(p)
    nota = nota[['CODASS'] <= cuantil]  
    v = [0]*6
    for i in range(6):
        v[i] = cuenta(nota, franjas[i], franjas[i+1], i)
    return v

#pasa del nombre de la asignatura al código

del codigo_ass(nombre):
    codass = dasig[dasig['NOMBRE'] == nombre]
    return codass.iloc[0]['CODASS']
    
#crea matriz n*6 con n #asignaturas y M(n,i) la nota media de la franja iesima
#en la asignatura n. Variables vector de asignaturas, i(tipo de CP), 

def comparar(v,i):
    n = len(v)
    f = [0]*6
    M = [f]*n
    for j in range(n):
        codass = codigo_ass(v[j])
        M[j] = separacion(codass, i)
    return M







        
        
