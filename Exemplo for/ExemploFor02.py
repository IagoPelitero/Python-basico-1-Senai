#Exempo 2

inicio = int(input('Informe o número de início: '))
fim = int(input('Informe o número final: '))
salto = int(input('Informe o número de salto: '))
texto = "Calculo= "
soma = 0

#Criação do loop
for numero in range(inicio, fim, salto):
  soma = soma + numero
  texto = texto + str(numero)
  if numero > 50:
    texto = texto + '\nPassou de 50'
    break
  if numero != fim-1:
    texto = texto + ' + '
print(texto)
print (f'Soma: {soma}')