import tkinter as tk
from tkinter import filedialog
# from syntax_tree import Tokenizer


class CodeEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Code Editor")
        self.file_path = None

        # Create the menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # Create the File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Create the text widget
        self.text_widget = tk.Text(self.master)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Create the button frame
        button_frame = tk.Frame(self.master)
        button_frame.pack()

        # Create the buttons
        open_button = tk.Button(
            button_frame, text="Open", command=self.open_file)
        lex_button = tk.Button(
            button_frame, text="Lexical Analyzer", command=self.lexical_analysis)
        syntax_button = tk.Button(
            button_frame, text="Syntax Analyzer", command=self.syntax_analysis)
        semantics_button = tk.Button(
            button_frame, text="Semantics Analyzer", command=self.semantics_analysis)
        intermediate_button = tk.Button(
            button_frame, text="Intermediate Code Generator", command=self.intermediate_code_generator)
        target_button = tk.Button(
            button_frame, text="Target Code Generator", command=self.target_code_generator)

        # Pack the buttons
        open_button.pack(side=tk.LEFT, padx=5, pady=5)
        lex_button.pack(side=tk.LEFT, padx=5, pady=5)
        syntax_button.pack(side=tk.LEFT, padx=5, pady=5)
        semantics_button.pack(side=tk.LEFT, padx=5, pady=5)
        intermediate_button.pack(side=tk.LEFT, padx=5, pady=5)
        target_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the output frame
        output_frame = tk.Frame(self.master)
        output_frame.pack(fill=tk.BOTH, expand=True)

        # Create the output label
        output_label = tk.Label(output_frame, text="Output:")
        output_label.pack(side=tk.TOP, pady=5)

        # Create the output text widget
        self.output_text = tk.Text(output_frame)
        self.output_text.pack(fill=tk.BOTH, expand=True)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            with open(file_path, "r") as f:
                file_contents = f.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, file_contents)

    def lexical_analysis(self):
        return

    def semantics_analysis(self):
        return

    def syntax_analysis(self):
        return

    def intermediate_code_generator(self):
        return

    def target_code_generator(self):
        return


if __name__ == "__main__":
    root = tk.Tk()
    editor = CodeEditor(root)
    root.mainloop()
