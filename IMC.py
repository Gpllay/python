import flet as ft

#Formula IMC:
# peso / altura ** 2

#Criar a Intreface
#pegar os dados da interface 
#realizar o calculor
#retonar resultado alterando a interface



def main(page: ft.Page):
    page.title = "IMC"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    

    Peso = ft.TextField(label="Qual o Seu peso: ", suffix_text="kg", max_length=6,)
    Altura=ft.TextField(label="Qual a Sua Altura:", suffix_text="m", max_length=4,)

    Resultado = ft.Text("", size=40)
    

    #IMC = int(Peso.value) / int(Altura.value) ** 2

    #print(IMC)

    def teste(e):
        PesoV = float(Peso.value)
        AlturaV = float(Altura.value)
        print(AlturaV)
        print(PesoV)

        IMC = PesoV / AlturaV ** 2
        print(IMC)
        
        if IMC < 17:
            print("Muito abaixo do Peso")
            Resultado.value = "Você esta Muito abaixo do Peso"
            
        elif IMC >= 17 and IMC < 18.49:
            print("Abaixo do Peso")
            Resultado.value = "Você esta Abaixo do Peso"

        elif IMC >= 18.5 and IMC < 24.99:
            print("Peso Normal")
            Resultado.value = "Seu Peso esta Normal"

        elif IMC >= 25 and IMC < 29.99:
            print("Acima do Peso")
            Resultado.value = "Você esta Acima do Peso"

        elif IMC >= 30 and IMC < 34.99:
            print("Obesidade I")
            Resultado.value = "Você esta com Obesidade I"
        elif IMC >= 35 and IMC < 39.99:
            print("Obesidade II (Severa)")
            Resultado.value = "Você esta com Obesidade II (Severa)"

        elif IMC > 40:
            print("Obesidade III (Mórbida)")
            Resultado.value = "Você esta com Obesidade III (Mórbida)"

        page.update()
    page.add(
        ft.Container(
            ft.Column([
                ft.Container(
                    ft.Text("Calcular IMC", size=40, color=ft.colors.WHITE, text_align=ft.alignment.center),
                    alignment=ft.alignment.top_center
                ),

                ft.Container(
                    Resultado,
                    alignment=ft.alignment.center
                ),

                ft.Text(" "),
                ft.Row([
                    ft.Container(
                        ft.Text(" OBS: Digite somente numeros e utilize . no lucar de , ", color=ft.colors.RED_400, size=16,),
                        border_radius=30,
                        bgcolor=ft.colors.WHITE60,
                        width=400,
                        height=28,
                        padding=1,
                        alignment=ft.alignment.center_left,
                    ),
                ],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    Peso,
                    Altura,
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text(" "),
                ft.Row([
                    ft.ElevatedButton("Calcular", on_click=teste, scale=2),
                ],alignment=ft.MainAxisAlignment.CENTER),
                
            ], alignment=ft.MainAxisAlignment.CENTER),
            
            width=750,
            height=500,
            bgcolor=ft.colors.BLUE,
            border_radius=20,
            padding=20,
            alignment=ft.alignment.top_center,

        ),
        

    )
ft.app(target=main)