alturas = []
altura_media_dos_homens = []
altura_media_das_mulheres = []
numero_de_pessoas = 5

for i in range(numero_de_pessoas):
    print("Pessoa", i + 1)

    while True:
        alturas_digitada = input("Digite sua altura (ex: 1,75): ")

        if not alturas_digitada.strip():
            print("Erro: A altura não pode ficar em branco. Tente novamente.")
            continue
        try:

            alturas_digitada1 = float(alturas_digitada.replace(',', '.'))
            break
        except ValueError:

            print("Erro: Entrada inválida. Por favor, digite um número.")

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

print("--- Resultados Finais ---")

if alturas:
    print(f"A maior altura registrada foi: {max(alturas):.2f}")
    print(f"A menor altura registrada foi: {min(alturas):.2f}")
else:
    print("Nenhuma altura foi registrada.")

if media_dos_homens > 0:
    print(f"A média da altura dos homens é: {media_dos_homens:.2f}")

else:
    print("Não foram registrados homens para calcular a média.")

if media_das_mulheres > 0:
    print(f"A média da altura das mulheres é: {media_das_mulheres:.2f}")

else:
    print("Não foram registradas mulheres para calcular a média.")

print(f"Número de homens registrados: {len(altura_media_dos_homens)}")
print(f"Número de mulheres registradas: {len(altura_media_das_mulheres)}")