#LEIA A ALTURA E LARGURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E A QUATIDADE DE TINTA NECESSARIA PARA PINTALA, SABENDO QUE CADA LITRO DE TINTA PINTA 2M²

l = int(input('Largura: '))
a = int(input('Autura: '))

p = (l*a)
t = float(p/2)

print('A parede tem {:.0f}m², e será necessario {:.1f} litros de tinta para pintala'.format(p, t))

