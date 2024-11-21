import tkinter as tk
from tkinter import messagebox
from xml.dom.minidom import parseString

class XMLBeautifier:
    def __init__(self, parent):
        self.parent = parent

        self.input_label = tk.Label(parent, text="Input or Beautified XML")
        self.input_label.pack()

        self.text_area = tk.Text(parent, height=20, width=50)
        self.text_area.pack()

        self.beautify_button = tk.Button(parent, text="Beautify XML", command=self.beautify_xml)
        self.beautify_button.pack()

        self.copy_button = tk.Button(parent, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

        self.clear_button = tk.Button(parent, text="Clear", command=self.clear_text)
        self.clear_button.pack()


    def clear_text(self):
        self.text_area.delete("1.0", tk.END)


    def beautify_xml(self):
        input_text = self.text_area.get("1.0", tk.END).strip()
        try:
            dom = parseString(input_text)
            beautified_text = dom.toprettyxml(indent="  ")
            beautified_text = "\n".join([line for line in beautified_text.splitlines() if line.strip()])

            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, beautified_text)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to beautify XML: {e}")

    def copy_to_clipboard(self):
        beautified_text = self.text_area.get("1.0", tk.END).strip()
        if beautified_text:
            self.parent.clipboard_clear()
            self.parent.clipboard_append(beautified_text)
        else:
            messagebox.showwarning("Warning", "No content to copy.")
