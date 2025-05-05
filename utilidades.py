import unicodedata
from datetime import datetime


def descobrir_data():
    """
    -> Descobre a data atual do sistema
    :return: data_atual: Data atual do sistema
    """
    data_atual = datetime.now()

    return data_atual


def formatar_data(data):
    """
    -> Formata a data para usar somente dia e mês
    :param data: Data a ser formatada
    :return: data_formatada: Data formatada
    """
    data_formatada = data.strftime('%d%m')

    return data_formatada


def remover_acentos(texto):
    """
    -> Remove os acentos de um texto
    :param texto: String a ser normalizada
    :return: String sem acentos
    """
    return ''.join(
        letra for letra in unicodedata.normalize('NFD', texto)
        if unicodedata.category(letra) != 'Mn'
    )


def apresentar(data):
    """
    -> Exibe uma saudação com base no horário
    :param data: Data de referência
    :return: Saudação formatada
    """
    if data.hour < 12:
        saudacao = 'Bom dia,'
    else:
        saudacao = 'Boa tarde,'

    return f'\n{saudacao}\n\n'


def criar_usuario(primeiro_nome, ultimo_nome):
    """
    -> Cria o usuário no formato primeiro_nome.ultimo_nome
    :param primeiro_nome: Primeiro nome
    :param ultimo_nome: Último nome
    :return: Usuário criado
    """
    usuario = f'{primeiro_nome}.{ultimo_nome}'

    return usuario


def criar_senha(iniciais, data):
    """
    -> Cria a senha no formato Iniciais#DDMM
    :param iniciais: Lista de iniciais do nome
    :param data: Data atual
    :return: Senha criada
    """
    return ''.join(iniciais) + f'#{data}'


def mostrar_saudacao_final():
    """
    -> Exibe uma mensagem de saudação final com orientações para nova senha
    :return: Mensagem de saudação final
    """
    return(
    'Crie uma nova senha seguindo os critérios de segurança:\n'
    ' - A senha deve conter pelo menos 8 caracteres.\n'
    ' - Deve possuir, no mínimo, uma letra maiúscula.\n'
    ' - Deve conter, no mínimo, uma letra minúscula.\n'
    ' - Deve incluir, pelo menos, um número ou caracter especial (por exemplo, @, #, $, etc.).\n'
    'Após definir a nova senha, confirme a alteração.\n\n'    
    'Att...\n\n'
    )
