import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivisionNoExacta(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 4"
        valor_actual = evaluar(14, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionExacta(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 10\n" \
                         "Residuo: 0"
        valor_actual = evaluar(100, 10)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionExactaDos(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 24\n" \
                         "Residuo: 0"
        valor_actual = evaluar(48, 2)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivisionNoExactaDos(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 38\n" \
                         "Residuo: 1"
        valor_actual = evaluar(77, 2)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
