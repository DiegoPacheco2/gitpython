import random
p=str(input('Primeiro aluno: '))
s=str(input('Segundo aluno: '))
t=str(input('Terceiro aluno: '))
q=str(input('Quarto aluno: '))
list=[p, s, t, q]
print('O aluno escolhido foi {}'.format(random.choice(list)))
print('A orden da lista {}'.format(random.shuffle(list)))

