#FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE UM DESCONTO DE 5%

valor = float(input('Valor do produto: '))
desconto = (valor * 5)/100
resultado = (valor - desconto)

print('O valor do produto é {} e com o desconto de 5% ficará {:.3f}'.format(valor, resultado))