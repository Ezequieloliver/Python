import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.padding = 30

    nome = ft.TextField(label="Nome completo", width=400, autofocus=True)
    email = ft.TextField(label="E-mail", width=400)
    mensagem = ft.TextField(
        label="Mensagem", 
        multiline=True, 
        min_lines=5, 
        max_lines=5, 
        width=400
    )
    
    mensagem_status = ft.Column()

    def enviar_formulario(e):
        if not nome.value:
            nome.error_text = "Por favor, informe seu nome"
            page.update()
            return
        
        if not email.value:
            email.error_text = "Por favor, informe seu e-mail"
            page.update()
            return
            
        if not mensagem.value:
            mensagem.error_text = "Por favor, escreva sua mensagem"
            page.update()
            return

        nome.error_text = None
        email.error_text = None
        mensagem.error_text = None

        dados = {
            "nome": nome.value,
            "email": email.value,
            "mensagem": mensagem.value
        }
        print("Dados do formulário:", dados) 

        mensagem_status.controls.clear()
        mensagem_status.controls.append(
            ft.AlertDialog(
                title=ft.Text("Sucesso!"),
                content=ft.Text("Seu formulário foi enviado com sucesso."),
                open=True
            )
        )
        
        nome.value = ""
        email.value = ""
        mensagem.value = ""
        
        page.update()

    botao_enviar = ft.ElevatedButton(
        text="Enviar Mensagem",
        icon=ft.icons.SEND,
        on_click=enviar_formulario
    )

    form = ft.Column(
        controls=[
            ft.Text("Formulário de Contato", size=24, weight="bold"),
            nome,
            email,
            mensagem,
            botao_enviar,
            mensagem_status
        ],
        spacing=20,
        width=400
    )

    page.add(form)

ft.app(target=main)