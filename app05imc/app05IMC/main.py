import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor="yellow"
    
    txtPeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="Ingresa tu altura")
    lblIMCV=ft.Text("Tu IMC es de: ")
    
    img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
    page.add(
        ft.Column(
            Controls=[
                txtPeso,txtAltura,lblIMCV
            ],alignment="CENTER")
        ft.Row(
            Controls=[
                img
            ],alignment="CENTER")
        ft.Row(
            controls=[
                btnCalcular,btnLimpiar
            ],alignment="CENTER")
    )
    
    
    
    
    
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)
    



ft.app(main)
