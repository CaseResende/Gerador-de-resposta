from utilidades import descobrir_data, formatar_data, apresentar, exibir_linha

iniciais = list()

print('Qual é o assunto do chamado?')
escolha = int(input('[1] AD\n[2] E-mail\nDigite aqui: '))

nome_completo = str(input('Nome completo: ')).strip().lower()

nome_separado = nome_completo.split()

exibir_linha()
print('Nome formatado: ', end='')

for indice, nome in enumerate(nome_separado):
    print(nome.capitalize(), end=' ')
    if indice == 0:
        iniciais.append(nome[0].upper())
    else:
        iniciais.append(nome[0])
print()
exibir_linha()

primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]

apresentar(descobrir_data())

if escolha == 1:
    print(f'Usuário: {primeiro_nome}.{ultimo_nome}')
elif escolha == 2:
    print(f'E-mail: {primeiro_nome}.{ultimo_nome}@barbacena.mg.gov.br')

print('Senha: ', end='')
for letra in iniciais:
    print(letra, end='')
print(f'#{formatar_data(descobrir_data())}')
print()
print('Att...')
exibir_linha()