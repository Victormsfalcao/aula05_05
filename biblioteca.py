def piramide1(num):
    for i in range (1, num + 1):
        for j in range(0,i):
            print(i,end= " ")
        print()

def piramide2(num):
    for i in range (1, num + 1):
        for j in range(0,i):
            print(i,end= " ")
        print()

def verificarVogal(frase):
    vogais = "AEIOU"
    frase = frase.upper()
    qtdVogais = 0
    for i in frase:
        if i in vogais:
            qtdVogais += 1
    print(f"A frase {frase} contém {qtdVogais} vogais ")

