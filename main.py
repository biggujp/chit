import flet as ft

def main(page: ft.Page):
    page.title = "TJCalc App by BIGGUSAN"
    
    dd = ft.DropdownM2(
        label="กรุณาเลือกแรงดันไฟฟ้า",
    options=[
        ft.dropdownm2.Option("1P100V"),
        ft.dropdownm2.Option("3P200V"),   
        ],
    )
    tb1 = ft.TextField(label="กรอกค่า KW")
    tb2 = ft.TextField(label="ค่ากระแสที่ทำคำนวนได้", read_only=True, value="0.0")
    tb3 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
    tb4 = ft.TextField(label="With an icon", icon=ft.Icons.EMOJI_EMOTIONS)
    page.add(dd,tb1,tb2,tb3,tb4)


ft.app(main)

