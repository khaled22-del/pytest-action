#PROVA_ESCRITA --2--
"""
Exercici 1 (2 punts)
Escriu una funció crear_sequencia(inici, final) que generi una llista amb tots els números des de inici fins a final (ambdós inclosos). Valida que inici i final siguin dos enters positius i inici sigui més petit que final, sinó és així retorna una llista buida.
"""
def crear_sequencia(inici, final):
    l = []
    if isinstance(inici, int) and isinstance(final, int) and inici < final and inici >= 0:
        l = [i for i in range(inici, final + 1)]
    return l

"""
Exercici 2 (2 punts)
Crea una funció numeros_senars_majors(llista, limit) que retorni una nova llista amb només els números senars que siguin majors que limit. Valida que llista sigui una llista no buida i que limit sigui un número enter, sinó retorna una llista buida.
"""
def numeros_imparells_majors(llista, limit):
    l = []
    if isinstance(llista, list) and isinstance(limit, int) and llista:
        l = [i for i in llista if i % 2 != 0 and i > limit]
    return l
"""

Exercici 3 (2 punts)
Fes una funció primera_posicio(llista, element) que trobi la posició de la primera aparició d'un element a la llista. Si no existeix, ha de retornar -1. No pots utilitzar el mètode .index()
"""
def primera_posicio(llista, element):
    posicio = -1
    for i in range(len(llista)):
        if llista[i] == element and posicio == -1:
            posicio = i
    return posicio
"""
Exercici 4 (2 punts)
Escriu una funció diagonal_principal(matriu) que retorni una llista amb els elements de la diagonal principal d'una matriu quadrada . Valida que matriu sigui una llista de llistes no buida, que totes les files tinguin la mateixa longitud i que sigui quadrada (mateix número de files i columnes), sinó retorna una llista buida.
"""
def diagonal_principal(matriu):
    l = []
    # penseu una solució més senzilla
    if isinstance(matriu, list) and all(isinstance(fila, list) and len(fila) == len(matriu[0]) for fila in matriu) and len(matriu) == len(matriu[0]):
        l = [matriu[i][i] for i in range(len(matriu))]
    return l
