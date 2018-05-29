import pandas as pd
def quatris():#Funcion que retorna lista con [codass,asignatura,quatri] 
    asignaturas=pd.read_csv('logic/Asignaturas.csv')
    codigo=list(asignaturas.CODASS)
    asignatura=list(asignaturas.NOMBRE)
    quatri=list(asignaturas.Q)
    final=[]
    for x in range(len(codigo)):
        final.append([codigo [x],asignatura[x]])
    return final
    
