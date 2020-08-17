#LEIA UM VALOR EM METROS, DEPOIS EXIBA EM CENTIMETROS E MILIMETROS.

metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mi = metros * 1000

print('{} metros, tem {} centimetros'.format(metros, cm))
print('{} metros, tem {} milimetros'.format(metros, mi))
