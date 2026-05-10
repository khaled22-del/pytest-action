"""
Fitxer de tests de les proves escrites 01 i 02
"""

# Imports de les funcions a provar
from prova1 import (
    buscar_per_titol,
    afegir_a_biblioteca,
    joc_mes_car
)

from prova2 import (
    crear_sequencia,
    numeros_imparells_majors,
    primera_posicio,
    diagonal_principal
)


class TestProva01:
    """
    Bateria de proves per a la Prova Escrita 01
    Exercicis 2, 3 i 4
    """

    def test_buscar_per_titol(self):
        """Comprova la cerca per títol (insensible a majúscules)."""
        videojocs = [
            {"titol": "Zelda", "preu": 50},
            {"titol": "FIFA", "preu": 70}
        ]

        assert buscar_per_titol("zelda", videojocs) == {"titol": "Zelda", "preu": 50}
        assert buscar_per_titol("FIFA", videojocs) == {"titol": "FIFA", "preu": 70}
        assert buscar_per_titol("Mario", videojocs) is None

    def test_afegir_a_biblioteca(self):
        """Valida afegir jocs, duplicats i jocs inexistents."""
        videojocs = [{"titol": "Zelda", "preu": 50}]
        biblioteca = []

        assert afegir_a_biblioteca("Zelda", videojocs, biblioteca) == "✅ Joc afegit!"
        assert afegir_a_biblioteca("Zelda", videojocs, biblioteca) == "⚠️ Ja està a la biblioteca"
        assert afegir_a_biblioteca("Mario", videojocs, biblioteca) == "❌ Joc no trobat"

    def test_joc_mes_car(self):
        """Comprova que retorna el joc amb el preu més alt."""
        videojocs = [
            {"titol": "Zelda", "preu": 50},
            {"titol": "FIFA", "preu": 70},
            {"titol": "Mario", "preu": 40}
        ]

        assert joc_mes_car(videojocs) == {"titol": "FIFA", "preu": 70}


class TestProva02:
    """
    Bateria de proves per a la Prova Escrita 02
    Exercicis 1 a 4
    """

    def test_crear_sequencia(self):
        """Prova seqüències vàlides i invàlides."""
        assert crear_sequencia(5, 10) == [5, 6, 7, 8, 9, 10]
        assert crear_sequencia(10, 5) == []
        assert crear_sequencia(-2, 5) == []

    def test_numeros_imparells_majors(self):
        """Filtra números senars majors que el límit."""
        llista = [3, -1, 7, 2, -1, 9, 4, 7]

        assert numeros_imparells_majors(llista, 3) == [7, 9, 7]
        assert numeros_imparells_majors([], 3) == []

    def test_primera_posicio(self):
        """Retorna la primera posició o -1."""
        llista = [3, -1, 7, 2, -1, 9, 4, 7]

        assert primera_posicio(llista, 7) == 2
        assert primera_posicio(llista, 15) == -1
        assert primera_posicio([], 5) == -1

    def test_diagonal_principal(self):
        """Extreu la diagonal principal de matrius quadrades."""
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        assert diagonal_principal(matriu) == [1, 5, 9]
        assert diagonal_principal([[1, 2], [3, 4, 5]]) == []

if __name__ == "__main__":
    print("=== Test Prova Escrita 01 ===")
    t1 = TestProva01()

    t1.test_buscar_per_titol()
    print("✔ test_buscar_per_titol OK")

    t1.test_afegir_a_biblioteca()
    print("✔ test_afegir_a_biblioteca OK")

    t1.test_joc_mes_car()
    print("✔ test_joc_mes_car OK")

    print("\n=== Test Prova Escrita 02 ===")
    t2 = TestProva02()

    t2.test_crear_sequencia()
    print("✔ test_crear_sequencia OK")

    t2.test_numeros_imparells_majors()
    print("✔ test_numeros_imparells_majors OK")

    t2.test_primera_posicio()
    print("✔ test_primera_posicio OK")

    t2.test_diagonal_principal()
    print("✔ test_diagonal_principal OK")
