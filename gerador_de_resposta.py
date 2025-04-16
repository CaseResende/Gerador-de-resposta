from utilidades import *

def gerar_texto_resposta(escolha: str, nome_completo: str) -> str:
    resposta = ''
    iniciais = []
    nome_completo = nome_completo.strip().lower()
    nome_separado = nome_completo.split()

    primeiro_nome = remover_acentos(nome_separado[0])
    ultimo_nome = remover_acentos(nome_separado[-1])

    resposta += 'Nome formatado: '

    for indice, nome in enumerate(nome_separado):
        resposta += nome.capitalize() + ' '
        if indice == 0:
            iniciais.append(nome[0].upper())
        else:
            iniciais.append(nome[0])

    resposta += '\n'

    data = descobrir_data()
    resposta += apresentar(data)

    if escolha == 'AD':
        resposta += f'Usuário: {criar_usuario(primeiro_nome, ultimo_nome)}\n'
    elif escolha == 'E-mail':
        resposta += f'E-mail: {criar_usuario(primeiro_nome, ultimo_nome)}@barbacena.mg.gov.br\n'

    senha = criar_senha(iniciais, formatar_data(data))
    resposta += f'Senha: {senha}\n\n'
    resposta += mostrar_saudacao_final()


    return resposta
