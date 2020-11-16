import tkinter as tk
import tkinter.font as tkFont


class GUIGame:
    def __init__(self, master):
        self.visible_table = [ ]

class GUISetup:
    def __init__(self, master):
        # Set the Default Values here
        self.size_x = 10
        self.size_y = 10
        self.num_mines = 20

        self.dt_size_x = tk.StringVar()
        self.dt_size_x.set(self.size_x)

        self.dt_size_y = tk.StringVar()
        self.dt_size_y.set(self.size_y)

        self.dt_num_mines = tk.StringVar()
        self.dt_num_mines.set(self.num_mines)

        self.lbl_size_x = tk.Label(master, text="Width: ", font=fontStyle).grid(row=0, column=0, sticky=tk.NSEW)
        self.ent_size_x = tk.Entry(master, font=fontStyle, textvariable = self.dt_size_y).grid(row=0, column=1,
                                                                                               sticky=tk.NSEW)

        self.lbl_size_y = tk.Label(master, text="Height: ", font=fontStyle).grid(row=1, column=0, sticky=tk.NSEW)
        self.ent_size_x = tk.Entry(master, font=fontStyle, textvariable = self.dt_size_x).grid(row=1, column=1,
                                                                                               sticky=tk.NSEW)

        self.lbl_num_mines = tk.Label(master, text="Number of Mines: ", font=fontStyle).grid(row=2, column=0,
                                                                                             sticky=tk.NSEW)
        self.ent_num_mines = tk.Entry(master, font=fontStyle, textvariable = self.dt_num_mines).grid(row=2, column=1,
                                                                                                     sticky=tk.NSEW)

        self.btn_start = tk.Button(master, text="START", font=fontStyle).grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)



if __name__ == "__main__":
    window = tk.Tk()
    window.title("MINE SWEEPER")
    fontStyle = tkFont.Font(family="Lucida Grande", size=13)
    app = GUISetup(window)
    tk.mainloop()
