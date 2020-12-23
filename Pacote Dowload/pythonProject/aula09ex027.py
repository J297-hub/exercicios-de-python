nome=str(input('Digite seu nome completo:')).strip()
n=nome.split()
print('Muito prazer em te cohnecer! {}'.format(nome))
print('Seu primeiro nome é = {}'.format(n[0]))
print('Seu último nome é = {}'.format(n[len(n)-1]))


