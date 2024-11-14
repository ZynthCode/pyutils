import tkinter as tk

class EscapeForConstVariable:
    def __init__(self, parent):
        self.parent = parent

        self.input_label = tk.Label(parent, text="Input Markdown Text")
        self.input_label.pack(anchor="nw")

        input_frame = tk.Frame(parent)
        input_frame.pack(fill="both", expand=True)

        self.input_box = tk.Text(input_frame, wrap="none")
        self.input_box.pack(side="left", fill="both", expand=True)

        self.input_vscroll = tk.Scrollbar(input_frame, command=self.input_box.yview, orient="vertical")
        self.input_vscroll.pack(side="right", fill="y")
        self.input_box.configure(yscrollcommand=self.input_vscroll.set)

        self.input_hscroll = tk.Scrollbar(parent, command=self.input_box.xview, orient="horizontal")
        self.input_hscroll.pack(fill="x")
        self.input_box.configure(xscrollcommand=self.input_hscroll.set)

        self.input_box.bind("<KeyRelease>", self.escape_text)
        self.input_box.bind("<Control-a>", self.select_all_if_needed)

        self.output_label = tk.Label(parent, text="Escaped Text for Const Variable")
        self.output_label.pack(anchor="nw")

        output_frame = tk.Frame(parent)
        output_frame.pack(fill="both", expand=True)

        self.output_box = tk.Text(output_frame, wrap="none", state="disabled")
        self.output_box.pack(side="left", fill="both", expand=True)

        self.output_vscroll = tk.Scrollbar(output_frame, command=self.output_box.yview, orient="vertical")
        self.output_vscroll.pack(side="right", fill="y")
        self.output_box.configure(yscrollcommand=self.output_vscroll.set)

        self.output_hscroll = tk.Scrollbar(parent, command=self.output_box.xview, orient="horizontal")
        self.output_hscroll.pack(fill="x")
        self.output_box.configure(xscrollcommand=self.output_hscroll.set)

        self.copy_button = tk.Button(parent, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

        self.escape_text()

    def escape_text(self, event=None):
        input_text = self.input_box.get("1.0", tk.END).strip()
        
        escaped_text = input_text.replace("\\", "\\\\") \
                                 .replace("`", "\\`") \
                                 .replace("```", "\\`\\`\\`")

        self.output_box.config(state="normal")
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, escaped_text)
        self.output_box.config(state="disabled")

    def copy_to_clipboard(self):
        escaped_text = self.output_box.get("1.0", tk.END).strip()
        self.parent.clipboard_clear()
        self.parent.clipboard_append(escaped_text)

    def select_all_if_needed(self, event=None):
        # Check if `CTRL+A` is not automatically selecting all, then do it manually
        if self.input_box.tag_ranges("sel") == ():
            self.input_box.tag_add("sel", "1.0", "end")
        return "break"  # To avoid propagating the event further if already handled
