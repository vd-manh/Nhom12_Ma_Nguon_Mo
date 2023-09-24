from tkinter import Tk, Label, Button, Frame
from tkinter.constants import BOTH
import inverse
import multi
import trans
import add

gui_menu = Tk()
gui_menu.geometry('300x230')
gui_menu.title('Menu')
gui_menu.resizable(False, False)
frame_menu = Frame(gui_menu,background = '#99FFFF' ,highlightbackground='black', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)


class Menu:
    def __init__(self):
        label = Label(frame_menu,background = '#99FFFF', text="Chọn phép toán:", pady=10, font=('arial', 10, 'bold'))

        inv = Button(frame_menu, text="Phép nghịch đảo", padx=100, pady=5, command=inverse.Inverse)
        ad = Button(frame_menu, text="Add", padx=140, pady=5, command=add.Add)
        tran = Button(frame_menu, text="Phép chuyển đổi", padx=140, pady=5, command=trans.Trans)
        mlt = Button(frame_menu, text="Phép nhân", padx=140, pady=5, command=multi.Multi)

        label.pack()
        inv.pack()
        mlt.pack()
        ad.pack()
        tran.pack()

        # def on_closing():
        #      if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #         gui_menu.destroy()
        # gui_menu.protocol("WM_DELETE_WINDOW", on_closing)

        gui_menu.mainloop()
