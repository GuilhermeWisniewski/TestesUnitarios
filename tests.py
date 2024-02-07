from triangulo import classifica_triangulo

def test_nao_triangulo():
    assert classifica_triangulo(1, 2, 5) == "Não é um triângulo"
    print("Teste para lados que não formam um triângulo: Passou!")

def test_equilatero():
    assert classifica_triangulo(5, 5, 5) == "Triângulo equilátero"
    print("Teste para triângulo equilátero: Passou!")

def test_isosceles():
    assert classifica_triangulo(5, 5, 8) == "Triângulo isósceles"
    print("Teste para triângulo isósceles: Passou!")

def test_escaleno():
    assert classifica_triangulo(3, 4, 5) == "Triângulo escaleno"
    print("Teste para triângulo escaleno: Passou!")

def test_outro_triangulo():
    assert classifica_triangulo(6, 8, 10) == "Triângulo escaleno"
    print("Teste para outro triângulo: Passou!")
