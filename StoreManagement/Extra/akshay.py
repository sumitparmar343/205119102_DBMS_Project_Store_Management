class Application:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        # frames
        self.left = Frame(master, width=900, height=768, bg='white')
        self.left.pack(side=LEFT)



root = Tk
b = Application(root)

root.geometry("1366x768+0+0")
root.mainloop()