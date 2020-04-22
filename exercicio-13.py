#CRIE UM PROGRAMA QUE LEIA O SALARIO DO FUNCIONARIO E MOSTRE O NOVO VALOR COM 15% DE AUMENTO

sa = float(input('Qual o valor do salario? ' ))
aumento = (sa * 15)/100
resultado = sa + aumento

print('O Salario é de {}, com o aumento de 15% ficará {}'.format(sa, resultado))