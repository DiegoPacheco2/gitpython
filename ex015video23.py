dia=int(input('Quantidade de dias que o carro foi alugado: '))
km=float(input('Quantidade de KM rodados: '))
calculo=(dia*60)+(km*0.15)
print('O valor do aluguel foi de R${:.2f}'.format(calculo))