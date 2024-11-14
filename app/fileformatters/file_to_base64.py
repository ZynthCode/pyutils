import tkinter as tk
from tkinter import filedialog, messagebox
import base64

try:
    from tkinterdnd2 import DND_FILES  # used for drag-and-drop support
except ImportError:
    raise ImportError("Please install tkinterdnd2: `pip install tkinterdnd2`")

class FileToBase64:
    def __init__(self, parent):
        self.parent = parent

        self.drag_label = tk.Label(parent, text="Drag and Drop File Here or Click to Select", relief="solid", padx=10, pady=30)
        self.drag_label.pack(fill="x", pady=10)
        self.drag_label.bind("<Button-1>", self.select_file)

        self.parent.drop_target_register(DND_FILES)
        self.parent.dnd_bind('<<Drop>>', self.drop_file)

        self.output_label = tk.Label(parent, text="Base64 Encoded Text")
        self.output_label.pack(anchor="nw")

        output_frame = tk.Frame(parent)
        output_frame.pack(fill="both", expand=True)

        self.output_box = tk.Text(output_frame, wrap="none", state="normal")  
        self.output_box.pack(side="left", fill="both", expand=True)

        self.output_vscroll = tk.Scrollbar(output_frame, command=self.output_box.yview, orient="vertical")
        self.output_vscroll.pack(side="right", fill="y")
        self.output_box.configure(yscrollcommand=self.output_vscroll.set)

        self.output_hscroll = tk.Scrollbar(parent, command=self.output_box.xview, orient="horizontal")
        self.output_hscroll.pack(fill="x")
        self.output_box.configure(xscrollcommand=self.output_hscroll.set)

        self.copy_button_default = tk.Button(parent, text="Copy to Clipboard (Default)", command=self.copy_to_clipboard_default)
        self.copy_button_default.pack(pady=5)

        self.copy_button_single_line = tk.Button(parent, text="Copy to Clipboard (One Line)", command=self.copy_to_clipboard_single_line)
        self.copy_button_single_line.pack(pady=5)

        self.clear_button = tk.Button(parent, text="Clear", command=self.clear_output)
        self.clear_button.pack(pady=5)

        self.save_button = tk.Button(parent, text="Save to File", command=self.save_to_file)
        self.save_button.pack(pady=5)

    def select_file(self, event=None):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.encode_file_to_base64(file_path)

    def drop_file(self, event):
        file_path = event.data.strip("{}")  
        if file_path:
            self.encode_file_to_base64(file_path)

    def encode_file_to_base64(self, file_path):
        with open(file_path, "rb") as file:
            encoded_content = base64.b64encode(file.read()).decode("utf-8")

        formatted_encoded_content = "\n".join(encoded_content[i:i+50] for i in range(0, len(encoded_content), 50))

        self.output_box.config(state="normal")
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, formatted_encoded_content)
        self.output_box.config(state="normal") 

    def copy_to_clipboard_default(self):
        formatted_text = self.output_box.get("1.0", tk.END).strip()
        self.parent.clipboard_clear()
        self.parent.clipboard_append(formatted_text)

    def copy_to_clipboard_single_line(self):
        single_line_text = self.output_box.get("1.0", tk.END).replace("\n", "").strip()
        self.parent.clipboard_clear()
        self.parent.clipboard_append(single_line_text)

    def clear_output(self):
        self.output_box.delete("1.0", tk.END)

    def save_to_file(self):
        base64_content = self.output_box.get("1.0", tk.END).replace("\n", "").strip()
        try:
            decoded_content = base64.b64decode(base64_content)
            file_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("All Files", "*.*")])
            if file_path:
                with open(file_path, "wb") as file:
                    file.write(decoded_content)
                messagebox.showinfo("Success", f"File saved successfully to {file_path}")
        except base64.binascii.Error:
            messagebox.showerror("Error", "Invalid base64 content. Please ensure the content is correctly formatted.")
