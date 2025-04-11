import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    
    def add_task(e):
        if task_input.value:
            task_item = ft.Checkbox(
                value=False,
                label=task_input.value,
                on_change=lambda e: toggle_task(e, task_item)
            )
            
            tasks_list.controls.append(task_item)
            
            task_input.value = ""
            
            page.update()
    
    def toggle_task(e, task_item):
        page.update()
    
    task_input = ft.TextField(
        hint_text="Digite uma tarefa...",
        width=300,
        autofocus=True,
        on_submit=add_task
    )
    
    add_button = ft.ElevatedButton(
        text="Adicionar",
        on_click=add_task
    )
    
    tasks_list = ft.Column()
    
    page.add(
        ft.Row(
            controls=[
                task_input,
                add_button
            ],
            alignment="center"
        ),
        ft.Divider(),
        tasks_list
    )

ft.app(target=main)