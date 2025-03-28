def descobrir_data():
    """
    -> Descobre a data atual do sistema
    :return: data_atual: Data atual do sistema
    """
    from datetime import datetime

    data_atual = datetime.now()

    return data_atual


def formatar_data(data):
    """
    -> Formata a data para usar somente dia e mês
    :param data: Data a ser formatada
    :return: Data formatada
    """
    from  time import strftime

    data_formatada = data.strftime('%d%m')

    return data_formatada


def apresentar(data):
    """
    -> Exibe uma saudação com base no horário
    :param data: Data de referência
    :return: Sem retorno
    """
    print()
    if data.hour < 12:
        print('Bom dia,')
    else:
        print('Boa tarde,')
    print()

def exibir_linha():
    """
    -> Exibe uma linha separadora
    :return: sem retorno
    """
    print('-' * 60)
