from tkinterdnd2 import TkinterDnD  
import tkinter as tk
from tkinter import ttk
from app.textformatters.escape_for_const_variable import EscapeForConstVariable
from app.textformatters.multiline_to_single_line import MultiLineToSingleLine
from app.fileformatters.file_to_base64 import FileToBase64

class MultiToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Selector")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        oneliner_frame = tk.Frame(self.notebook)
        MultiLineToSingleLine(oneliner_frame)
        self.notebook.add(oneliner_frame, text="Oneliner Formatter")

        escape_frame = tk.Frame(self.notebook)
        EscapeForConstVariable(escape_frame)
        self.notebook.add(escape_frame, text="Escape for Const Variable") 

        file_to_base64_frame = tk.Frame(self.notebook)
        FileToBase64(file_to_base64_frame)
        self.notebook.add(file_to_base64_frame, text="File to Base64")


if __name__ == "__main__":
    root = TkinterDnD.Tk() 
    app = MultiToolApp(root)

    root.update_idletasks()
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
    root.attributes("-type", "dialog")

    root.mainloop()
