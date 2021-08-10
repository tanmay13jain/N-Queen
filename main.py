import tkinter
import gui

dark = "#541a1d"

window = tkinter.Tk()
window.title("N-Queen Problem")
window.config(padx=50, pady=50, bg=dark)

logo = tkinter.PhotoImage(file="logo.png")
window.iconphoto(False, logo)

gui.gui()
window.mainloop()
