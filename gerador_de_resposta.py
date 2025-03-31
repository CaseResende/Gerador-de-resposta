# Importação das funções
from utilidades import *

# Inicialização da variável
iniciais = list()

exibir_linha()
print('Qual é o assunto do chamado?')

# Tratamento de exceções no menu
try:
    escolha = int(input('[1] AD\n[2] E-mail\nDigite aqui: '))
    if escolha not in [1, 2]:
        raise ValueError

except ValueError:
    print('Escolha inválida!')

except KeyboardInterrupt:
    print('\nEntrada interrompida pelo usuário.')

else:
    nome_completo = str(input('Nome completo: ')).strip().lower()
    nome_separado = nome_completo.split()

    # Coleta o primeiro e último nomes sem acentos
    primeiro_nome = remover_acentos(nome_separado[0])
    ultimo_nome = remover_acentos(nome_separado[-1])

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

    # Resposta do chamado
    apresentar(descobrir_data())

    # Cria o usuário ou endereço de e-mail
    if escolha == 1:
        print(f'Usuário: {criar_usuario(primeiro_nome, ultimo_nome)}')
    elif escolha == 2:
        print(f'E-mail: {criar_usuario(primeiro_nome, ultimo_nome)}@barbacena.mg.gov.br')

    # Cria a senha
    senha_criada = criar_senha(iniciais, formatar_data(descobrir_data()))
    print(f'Senha: {senha_criada}')
    print()

    # Saudação final
    print("""Crie uma nova senha seguindo os critérios de segurança:
- A senha deve conter pelo menos 8 caracteres.
- Deve possuir, no mínimo, uma letra maiúscula.
- Deve conter, no mínimo, uma letra minúscula.
- Deve incluir, pelo menos, um número ou caracter especial (por exemplo, @, #, $, etc.).
Após definir a nova senha, confirme a alteração.""")
    print()
    print('Att...')
    print()

finally:
    exibir_linha()
    print('Fim da execução!')
    exibir_linha()