from tkinter import Tk, ttk

class Confirm():
    def __init__(self, finished:str = "sem_nome"):
        self.finished:str = finished
        self.status: str
        self.root = Tk()
        self._build()
        self.root.mainloop()
        
    def _build(self):
        f1 = ttk.Frame(self.root)
        f1.pack(padx=10, pady=10)

        f2 = ttk.Frame(f1)
        f2.pack()

        l1 = ttk.Label(f2, text=f"O processo {self.finished} terminou.")
        l1.pack()

        l2 = ttk.Label(f2, text=f"Deseja continuar para o próximo?")
        l2.pack()

        f3 = ttk.Frame(f1)
        f3.pack()

        b1 = ttk.Button(f3, text="Continuar", command=self.set_continue)
        b1.pack()

        b2 = ttk.Button(f3, text="Abortar", command=self.set_abort)
        b2.pack()
        ...
        
    def set_continue(self):
        self.status = "continue"
        self.root.destroy()
        
    def set_abort(self):
        self.status = "abort"
        self.root.destroy()
