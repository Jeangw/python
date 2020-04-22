#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR

real = float(input('Informe quantos reais você tem na carteira: '))
dolar = (real / 5.29)

print('Você pode comprar {:.2f} dólares'.format(dolar))