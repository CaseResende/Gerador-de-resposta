import flet as ft
from gerador_de_resposta import gerar_texto_resposta


def main(pagina: ft.Page):
    pagina.theme_mode = ft.ThemeMode.LIGHT
    pagina.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Campos
    opcao_menu = ft.Dropdown(
        border_color=ft.colors.LIGHT_BLUE,
        label='Opção',
        hint_text='Selecione...',
        options=[
            ft.dropdown.Option('AD'),
            ft.dropdown.Option('E-mail')
        ],
        width=300
    )

    nome_completo = ft.TextField(
        border_color=ft.colors.LIGHT_BLUE,
        label='Nome completo',
        autofocus=True,
        width=300
    )

    # Mensagem de erro
    mensagem_erro = ft.Text(
        value='',
        color=ft.colors.RED,
        size=14
    )

    resposta_texto = ft.Text(
        value='',
        color=ft.colors.BLACK,
        size=14,
        selectable=True
    )

    resposta_gerada = ft.Container(
        bgcolor=ft.colors.GREY_100,
        padding=ft.padding.all(20),
        border_radius=10,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[resposta_texto]
        )
    )

    # Botão com validação
    def gerar_resposta(e):
        nome = nome_completo.value.strip()
        opcao = opcao_menu.value

        if not nome or not opcao:
            mensagem_erro.value = "Preencha todos os campos obrigatórios."
        else:
            mensagem_erro.value = ""
            resposta_texto.value = gerar_texto_resposta(opcao, nome)


        pagina.update()

    botao_resposta = ft.ElevatedButton(
        col=6,
        text='Gerar resposta',
        on_click=gerar_resposta
    )

    # Menu
    menu = ft.Container(
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value='Qual é o assunto do chamado?',
                    color=ft.colors.BLACK,
                    size=18,
                ),
                ft.ResponsiveRow(
                    col=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[opcao_menu]
                )
            ]
        )
    )

    # Nome
    nome = ft.Container(
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text(value='Nome completo'),
                nome_completo,
                mensagem_erro,
                ft.ResponsiveRow(controls=[botao_resposta])
            ]
        )
    )

    # Box principal
    layout = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        margin=ft.margin.all(30),
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=200, color=ft.colors.LIGHT_BLUE),
        content=ft.ResponsiveRow(controls=[menu, nome, resposta_gerada])
    )

    # Adição à página
    pagina.add(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                layout
            ]
        )
    )

ft.app(target=main)
