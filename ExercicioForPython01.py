#Ex 1

cont_m = 0

for masc in range(0, 10, 1):
    sexo = input('Digite seu sexo:(f/m)')
    if sexo.lower() == 'm':
        cont_m += 1

print(f"Total de pessoas do sexo masculino: {cont_m}")