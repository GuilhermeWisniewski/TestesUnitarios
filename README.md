Guilherme dos Santos Wisniewski RA: 813319

A aplicação a ser testada é uma função que recebe três valores, 
verifica se esses tres valores formam um triangulo e então o classifica

O primeiro teste verifica se as entradas formam um triangulo,
4 testes seguintes verificam as três classificações de um triangulo (equilatero, isoceles e escaleno)

Verifique se o python e o pytest estão instalados em seu ambiente:

    pytest --version
    
    python --version

Caso seja necessário instale-os:

    pip install python
    
    pip install pytest

Com o ambiente configurado:
Para executar a aplicação use o comando (com a, b, c sendo numeros naturais):
    
    python triangulo.py a b c

Para executar os testes use o comando:
    
    pytest -s tests.py
