import sys
# Recebe tres entradas e verifica se é triangulo, caso seja, o classifica
def classifica_triangulo(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Não é um triângulo"
    elif a == b == c:
        return "Triângulo equilátero"
    elif a == b or a == c or b == c:
        return "Triângulo isósceles"
    else:
        return "Triângulo escaleno"


# Recebe as entradas do Standard Input
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python triangulo.py <lado1> <lado2> <lado3>")
        sys.exit(1)

    try:
        a, b, c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    except ValueError:
        print("Erro: Insira valores numéricos para os lados do triângulo.")
        sys.exit(1)

    resultado = classifica_triangulo(a, b, c)
    print(resultado)