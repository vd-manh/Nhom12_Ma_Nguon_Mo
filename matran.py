from tkinter import Tk, Label, Button, Frame

class Menu1:
    def __init__(self, root):
        self.gui_menu = root
        self.gui_menu.geometry('250x180')
        self.gui_menu.title('Menu')
        self.gui_menu.resizable(False, False)
        self.frame_menu = Frame(self.gui_menu, background='#99FFFF', highlightbackground='black', highlightthickness=1)
        self.frame_menu.pack(fill='both', expand=True, padx=5, pady=5)

        label = Label(self.frame_menu, background='#99FFFF', text="Chọn phép toán:", pady=10, font=('arial', 10, 'bold'))
        tinhtoan = Button(self.frame_menu, text="Tính toán", padx=130, pady=20)
        matran = Button(self.frame_menu, text="Ma trận", padx=140, pady=20, command=self.open_menu2)


        label.pack()
        tinhtoan.pack()
        matran.pack()


    def open_menu2(self):
        self.gui_menu.withdraw()  # Ẩn cửa sổ chính
        import menu
        menu.Menu(self.gui_menu)  # Mở cửa sổ 2 và chuyển đối tượng root của cửa sổ 1 sang cửa sổ 2

    
