import tkinter
from tkinter import messagebox
import brain


def gui():
    dark = "#541a1d"
    white = "#fefefe"
    square = 50
    board_color = ["#ffce9e", "#d18b47"]

    queen = tkinter.PhotoImage(file="queen.png")
    global page_number
    page_number = 0

    def restart():
        global board
        global next_button
        global retry_button
        global solution_info
        try:
            board.destroy()
            next_button.destroy()
            retry_button.destroy()
            solution_info.destroy()
        except NameError:
            pass
        gui()

    def place_queen():
        global page_number
        global position_set
        global n
        global board
        global queen_list
        global next_button
        global solution_info
        try:
            solution_info.destroy()
        except NameError:
            pass
        solution_info = tkinter.Label(text=f"Solution {page_number + 1} of {len(position_set)}", bg=dark, fg=white)
        solution_info.grid(row=2, column=0, pady=(10, 1))
        required_list = position_set[page_number]
        next_button.config(text="Next")
        for i in range(0, n):
            try:
                board.delete(queen_list[i])
            except (IndexError, NameError):
                pass
        queen_list = []
        for i in range(0, n):
            row, column = i, required_list[i]
            row = (row * 50) + 25
            column = (column * 50) + 25
            image = board.create_image(column, row, image=queen)
            queen_list.append(image)
        page_number = (page_number + 1) % (len(position_set))

    def buttons():
        global next_button
        next_button = tkinter.Button(text="Start", bg=dark, fg=white, relief="ridge", width=20, command=place_queen)
        next_button.grid(row=3, column=0, pady=(10, 10))
        global retry_button
        retry_button = tkinter.Button(text="Reset", bg=dark, fg=white, relief="ridge", width=20, command=restart)
        retry_button.grid(row=4, column=0, pady=(10, 10))

    def n_queen():
        global n
        n = n_queen_entry.get()
        try:
            n = int(n)
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter natural number values")
            return
        else:
            if n < 1:
                messagebox.showerror(title="Error",
                                     message="Please enter integers only between 1 and 8 (both inclusive)")
                return
            if n > 8:
                messagebox.showerror(title="Error",
                                     message="Please enter integers only between 1 and 8 (both inclusive)")
                return
        try:
            n_queen_label.destroy()
            n_queen_entry.destroy()
            n_queen_button.destroy()
        except NameError:
            pass
        global board
        board = tkinter.Canvas(width=n * square, height=n * square, bg=white, highlightthickness=0)
        board.grid(row=1, column=0)
        for y in range(0, n):
            for x in range(0, n):
                color = board_color[(x + y) % 2]
                board.create_rectangle(x * square, y * square, (x + 1) * square, (y + 1) * square, fill=color)
        global position_set
        position_set = brain.main(n)
        if len(position_set) == 0:
            messagebox.showinfo(title="Result", message="No Queen placement possible!")
            restart()
            return
        buttons()
        return

    logo = tkinter.Label(text="N-Queen Problem", font=("Century Schoolbook", 14), fg=white, bg=dark)
    logo.grid(row=0, column=0, pady=(1, 10), columnspan=2)

    n_queen_label = tkinter.Label(text="Enter the number of queens:", fg=white, bg=dark)
    n_queen_entry = tkinter.Entry(width=2, justify='center')
    n_queen_entry.grid(row=1, column=1)
    n_queen_label.grid(row=1, column=0)

    n_queen_button = tkinter.Button(text="Solve", relief="ridge", width=20, bg=dark, fg=white, command=n_queen)
    n_queen_button.grid(row=2, column=0, pady=(10, 10), columnspan=2)
