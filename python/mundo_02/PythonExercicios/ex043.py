"""

Desenvolva uma lógica que leia o peso e altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
print('&=' * 12)
print('ÍNDICE DE MASSA CORPORAL')
print('&=' * 12)
print('\n**** TABELA IMC ****')
print('- Abaixo de 18.5: Abaixo do peso\n'
      '- Entre 18.5 e 24.9: Peso ideal\n'
      '- 25 até 39.9: Sobrepeso\n'
      '- 30 até 40: Obesidade\n'
      '- Acima de 40: Obesidade mórbida')
print('**** TABELA IMC ****\n')
altura = float(input('Qual a sua altura? '))
peso = float(input('Quanto você pesa? '))
imc = peso / (altura * altura)
seuImc = imc
print('\n#### RESULTADO ####')
print(f'Seu IMC está em: {seuImc:.2f}.')
if seuImc < 18.5:
    print('Abaixo de 18.5: Abaixo do peso')
elif seuImc >= 18.5 and seuImc <= 24.9:
    print('- Entre 18.5 e 24.9: Peso ideal')
elif seuImc >= 25 and seuImc <= 39.9:
    print('- 25 até 39.9: Sobrepeso')
elif seuImc >= 30 and seuImc <= 39.9:
    print('- 30 até 39.9: Obesidade')
else:
    print('- Acima de 40: Obesidade mórbida')
