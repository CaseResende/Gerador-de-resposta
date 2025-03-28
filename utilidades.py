def descobrir_data():
    from datetime import datetime

    data_atual = datetime.now()

    return data_atual


def formatar_data(data):
    from  time import strftime

    data_formatada = data.strftime('%d%m')

    return data_formatada


def apresentar(data):

    print()
    if data.hour < 12:
        print('Bom dia,')
    else:
        print('Boa tarde,')
    print()

def exibir_linha():
    print('-' * 60)

