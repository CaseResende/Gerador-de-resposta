# Importação das funções
from utilidades import descobrir_data, formatar_data, apresentar, exibir_linha

# Inicialização da variável
iniciais = list()

exibir_linha()
print('Qual é o assunto do chamado?')

# Tratamento de exceções no menu
try:
    escolha = int(input('[1] AD\n[2] E-mail\nDigite aqui: '))

except (ValueError, TypeError):
    print('Escolha inválida!')

except KeyboardInterrupt:
    print('')
else:
    nome_completo = str(input('Nome completo: ')).strip().lower()
    nome_separado = nome_completo.split()

    # Coleta o primeiro e último nomes
    primeiro_nome = nome_separado[0]
    ultimo_nome = nome_separado[-1]

    # Exibe o nome completo formatado e captura as iniciais
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

    # Resposta
    apresentar(descobrir_data())

    # Gera o usuário ou endereço de e-mail
    if escolha == 1:
        print(f'Usuário: {primeiro_nome}.{ultimo_nome}')
    elif escolha == 2:
        print(f'E-mail: {primeiro_nome}.{ultimo_nome}@barbacena.mg.gov.br')

    # Gera a senha
    print('Senha: ', end='')
    for letra in iniciais:
        print(letra, end='')
    print(f'#{formatar_data(descobrir_data())}')
    print()
    print('Att...')
    print()

finally:
    print('Programa finalizado!')
    exibir_linha()
