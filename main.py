import flet as ft

def main(page: ft.Page):
    page.title = "TJCalc App by BIGGUSAN"

    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        page.update()

    t = ft.Text(value="0")

    dd = ft.DropdownM2(
    label="กรุณาเลือกแรงดันไฟฟ้า",
    options=[
        ft.dropdownm2.Option("1"),
        ft.dropdownm2.Option("3"),   
        ],
    )
    tb1 = ft.TextField(label="กรอกค่า KW")
    tb2 = ft.TextField(label="ค่ากระแสที่ทำคำนวนได้", read_only=True, value={t})
    tb3 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
    tb4 = ft.TextField(label="With an icon", icon=ft.Icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    page.add(dd,tb1,tb2,tb3,tb4,b)


ft.app(main)

