import tkinter as tk

class MultiLineToSingleLine:
    def __init__(self, parent):
        self.parent = parent

        self.input_label = tk.Label(parent, text="Input Text")
        self.input_label.pack()

        self.input_box = tk.Text(parent, height=10, width=50)
        self.input_box.pack()
        self.input_box.bind("<KeyRelease>", self.format_text)

        self.output_label = tk.Label(parent, text="Formatted Output")
        self.output_label.pack()

        self.output_box = tk.Text(parent, height=10, width=50)
        self.output_box.pack()
        self.output_box.config(state="disabled") 

        self.copy_button = tk.Button(parent, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()


        self.format_text()

    def format_text(self, event=None):
        input_text = self.input_box.get("1.0", tk.END).strip()
        lines = input_text.splitlines()
        formatted_text = "\\n".join(lines) if len(lines) > 1 else input_text

        self.output_box.config(state="normal")  
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, formatted_text)
        self.output_box.config(state="disabled")  

    def copy_to_clipboard(self):
        formatted_text = self.output_box.get("1.0", tk.END).strip()
        self.parent.clipboard_clear()
        self.parent.clipboard_append(formatted_text)