pro=float(input('Qual é o preço do produto? R$'))
des=(pro * 5) / 100
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(pro,pro - des))
