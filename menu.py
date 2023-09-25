from tkinter import Tk, Label, Button, Frame, BOTH
import inverse
import multi
import trans
import add

gui_menu = Tk()
gui_menu.geometry('300x220')
gui_menu.title('Menu')
gui_menu.resizable(False, False)
frame_menu = Frame(gui_menu,background = '#99FFFF' ,highlightbackground='black', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)


def exit_program():
    gui_menu.destroy()

class Menu:
    def __init__(self, root):

        label = Label(frame_menu, background='#99FFFF', text="Chọn phép toán:", pady=10, font=('arial', 10, 'bold'))
        inv = Button(frame_menu, text="Phép nghịch đảo", padx=100, pady=5, command=inverse.Inverse )  # Điều hướng tới trang chứa phép nghịch đảo
        ad = Button(frame_menu, text="Add", padx=140, pady=5, command=add.Add)  # Điều hướng tới trang chứa phép cộng
        tran = Button(frame_menu, text="Phép chuyển đổi", padx=140, pady=5,  command=trans.Trans)  # Điều hướng tới trang chứa phép chuyển đổi
        mlt = Button(frame_menu, text="Phép nhân", padx=140, pady=5, command=multi.Multi)  # Điều hướng tới trang chứa phép nhân
        thoat = Button(frame_menu,background ='#DD0000' , text="Thoát", padx=130, pady=5, command=exit_program)


        label.pack()
        inv.pack()
        mlt.pack()
        ad.pack()
        tran.pack()
        thoat.pack()