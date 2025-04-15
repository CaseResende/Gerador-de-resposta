import flet as ft


def main(pagina: ft.Page):
    pagina.theme_mode = ft.ThemeMode.DARK

    menu = ft.Container(
        col=12,
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            col=12,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.Text(
                    col=12,
                    value='Qual é o assunto do chamado?',
                    color=ft.colors.WHITE,
                    size=18,
                ),
                ft.Row(
                    col=12,
                    controls=[
                        ft.ElevatedButton(
                            col=6,
                            text='AD'
                        ),
                        ft.ElevatedButton(
                            col=6,
                            text='E-mail'
                        ),
                    ]
                )
            ]
        )
    )

    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                menu
            ]
        )
    )


    pagina.add(layout)
ft.app(target=main)