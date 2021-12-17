l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
area = l*a
print(f'Sua parede tem dimensão de {l}x{a} e sua áre é de {area} m².')
print('Quantidade de tinta necessária: {} litros'.format(area/2))