palavras = ('python', 'programacao', 'linguagem', 'desenvolvimento')

for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais.append(letra)
    
    print(f'Vogais na palavra "{palavra}":', vogais)