import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate
import re


class CodeEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("C++ - Compiler")
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
        close_button = tk.Button(
            button_frame, text="Close", command=self.close_file)
        lex_button = tk.Button(
            button_frame, text="Lexical Analyzer", command=self.lexical_analysis)
        intermediate_button = tk.Button(
            button_frame, text="Intermediate Code", command=self.intermediate_code_generator)
        
        # Pack the buttons
        open_button.pack(side=tk.LEFT, padx=5, pady=5)
        lex_button.pack(side=tk.LEFT, padx=5, pady=5)
        intermediate_button.pack(side=tk.LEFT, padx=5, pady=5)
        close_button.pack(side=tk.LEFT, padx=5, pady=5)

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

    def close_file(self):
        root.destroy()

    def lexical_analysis(self):
        # Get the contents of the text widget
        code = self.text_widget.get(1.0, tk.END)

        # Define the regular expressions for C++ tokens and their names
        token_patterns = [
            (r"#include\s*<\w+>", "Preprocessor Directive"),
            (r"\busing\s+namespace\s+std;", "Namespace Declaration"),
            (r"\bint\b", "Keyword: int"),
            (r"\bmain\b", "Keyword: main"),
            (r"[a-zA-Z_][a-zA-Z0-9_]*", "Identifier"),
            (r"\d+", "Number"),
            (r"\S", "Symbol"),
        ]

        tokens = {}
        for pattern, name in token_patterns:
            matches = re.findall(pattern, code)
            tokens[name] = set(matches)

        # Clear the output text widget
        self.output_text.delete(1.0, tk.END)

        # Display the results in a tabular format
        output_table = []
        for name, token_set in tokens.items():
            tokens_str = "\n".join(token_set)
            output_table.append([name, tokens_str])

        table_headers = ["Token Type", "Tokens"]
        self.output_text.insert(tk.END, "Lexical Analysis Results:\n")
        self.output_text.insert(
            tk.END, tabulate(
                output_table, headers=table_headers, tablefmt="grid")
        )

    def syntax_analysis(self):
        # Add your syntax analysis code here
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Running syntax analysis...")

    def semantics_analysis(self):
        # Add your semantics analysis code here
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Running semantics analysis...")

    def intermediate_code_generator(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(
            tk.END, "Running intermediate code generator...\n")

        code = self.text_widget.get("1.0", tk.END)
        lines = code.split("\n")

        # Create the quadruples table
        quadruples = []
        next_temp = 1
        for i, line in enumerate(lines):
            tokens = line.strip().split()
            if len(tokens) == 3:
                # Assignment statement
                temp = f"t{next_temp}"
                next_temp += 1
                quadruples.append((tokens[1], tokens[0], tokens[2], temp))
            elif len(tokens) == 5:
                # Arithmetic expression
                temp1 = f"t{next_temp}"
                next_temp += 1
                temp2 = f"t{next_temp}"
                next_temp += 1
                quadruples.append((tokens[2], tokens[1], tokens[3], temp1))
                quadruples.append((tokens[4], temp1, tokens[0], temp2))
            else:
                # Invalid input
                continue

        # Create the triples table
        triples = []
        for i, quad in enumerate(quadruples):
            if i == 0:
                triples.append((quad[0], quad[1], quad[3]))
            else:
                if quad[1] in ["+", "-", "*", "/"]:
                    op = quad[1]
                    x = triples[-1][2]
                    y = quad[2]
                    temp = f"t{next_temp}"
                    next_temp += 1
                    triples.append((op, x, y))
                    triples.append(("=", temp, None))
                else:
                    triples.append((quad[0], quad[1], quad[3]))

        # Create the indirect triples table
        indirect_triples = []
        for i, triple in enumerate(triples):
            if i == 0:
                indirect_triples.append((triple[0], triple[1], None))
                indirect_triples.append(("j", None, triple[2]))
            elif triple[0] == "=":
                indirect_triples.append((triple[0], triple[1], None))
            elif i == len(triples) - 1:
                indirect_triples.append((triple[0], None, triple[1]))
            else:
                indirect_triples.append(
                    (triple[0], indirect_triples[-1][2], triple[1]))

        # Display the tables
        self.output_text.insert(tk.END, "Quadruples Table:\n")
        headers = ["Operator", "Arg1", "Arg2", "Result"]
        table = tabulate(quadruples, headers=headers, tablefmt="presto")
        self.output_text.insert(tk.END, f"{table}\n\n")

        self.output_text.insert(tk.END, "Triples Table:\n")
        headers = ["Operator", "Arg1", "Arg2"]
        table = tabulate(triples, headers=headers, tablefmt="presto")
        self.output_text.insert(tk.END, f"{table}\n\n")

        self.output_text.insert(tk.END, "Indirect Triples Table:\n")
        headers = ["Operator", "True", "False"]
        table = tabulate(
            indirect_triples, headers=headers, tablefmt="presto")
        self.output_text.insert(tk.END, f"{table}\n\n")

    def generate_target_code(self):
        import ast
        import astor

        tree = ast.parse(self)
        new_tree = ast.fix_missing_locations(tree)

        target_code = astor.to_source(new_tree)
        self.output_text.insert(
            tk.END, f"{target_code}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("650x1300")
    editor = CodeEditor(root)
    root.mainloop()
