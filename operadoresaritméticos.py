nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Digite um numero {:.2f}'.format(5), end=' ')
n1=float(input('Digite o primeiro valor: '))
n2=float(input('Digite o segundo valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
so=n1%n2
p=n1**n2
print('Digite a soma {}, \n e a multiplicacao {} e a divisao {} e a sobra {}'.format(s,m,d,so))

