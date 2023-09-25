from tkinter import Tk
import matran

def main():
    root = Tk()  # Tạo cửa sổ gốc
    menu1 = matran.Menu1(root)
    menu1.gui_menu.mainloop()

if __name__ == '__main__':
    main()
