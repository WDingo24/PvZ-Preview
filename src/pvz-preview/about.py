import structs.abstracts

from typing import Any

import tkinter as tk
from tkinter import ttk

@structs.abstracts.singleton
class About(tk.Toplevel):
    def __init__(self, cnf: dict={}, **kwargs) -> None:
        kwargs = cnf or kwargs
        super().__init__(**kwargs)

        self.iconbitmap("assets/icon.ico")
        self.title("About")
        self.resizable(False, False)

        ttk.Label(self, text="Version: 0.1.25").pack()
        ttk.Button(self, text="License", command=lambda: License(master=self)).pack()

@structs.abstracts.singleton
class License(tk.Toplevel):
    def __init__(self, cnf: dict={}, **kwargs) -> None:
        kwargs = cnf or kwargs
        super().__init__(**kwargs)

        self.iconbitmap("assets/icon.ico")
        self.title("GNU General Public License | Version 3")
        self.resizable(False, False)

        field = tk.Text(self, width=80)
        with open("assets/LICENSE", "r") as file:
            [field.insert(f"{i}.0", line) for i, line in enumerate(file, 1)]
        field.pack()

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=field.yview)
        field.config(yscrollcommand=scrollbar.set, state="disabled")
        scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")