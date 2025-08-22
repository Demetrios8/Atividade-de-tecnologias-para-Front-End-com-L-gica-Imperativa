
alturas = []
genero = []
altura_media_dos_homens = []
altura_media_das_mulheres = []
numero_de_pessoas = 5

for i in range(numero_de_pessoas):
    print("Pessoa", i + 1)
    alturas_digitada = input("Digite sua altura (ex: 1,75): ")
    alturas_digitada1 = float(alturas_digitada.replace(',', '.'))
    alturas.append(alturas_digitada1)

    while True:
        genero = input("Digite M para masculino ou F para feminino: ").upper()
        if genero == "M":
            altura_media_dos_homens.append(alturas_digitada1)
            break
        elif genero == "F":
            altura_media_das_mulheres.append(alturas_digitada1)
            break
        else:
            print("Digite M ou F")

media_dos_homens = 0
if altura_media_dos_homens:
    media_dos_homens = sum(altura_media_dos_homens) / len(altura_media_dos_homens)

media_das_mulheres = 0
if altura_media_das_mulheres:
    media_das_mulheres = sum(altura_media_das_mulheres) / len(altura_media_das_mulheres)


print(f"A maior altura é: {max(alturas)}\nA menor altura é: {min(alturas)}\nA média da altura dos homens é: {media_dos_homens: .2f}\nA média da altura das mulheres é: {media_das_mulheres: .2f}")
if media_dos_homens > 0:
    print(f"A média da altura dos homens é: {media_dos_homens:.2f}")
else:
    print("Não foram registrados homens para calcular a média.")

if media_das_mulheres > 0:
    print(f"A média da altura das mulheres é: {media_das_mulheres:.2f}")
else:
    print("Não foram registradas mulheres para calcular a média.")