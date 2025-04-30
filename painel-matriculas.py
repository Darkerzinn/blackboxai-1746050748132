import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_NAME = "students.db"

class RoxynApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Roxyn")
        self.geometry("600x400")
        self.configure(bg="#2d2d30")  # dark gray background

        self.setup_db()
        self.create_widgets()
        self.load_students()

    def setup_db(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT NOT NULL UNIQUE,
                nome TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def create_widgets(self):
        # Title label
        title = tk.Label(self, text="Roxyn - Student Registration", bg="#2d2d30", fg="#9b59b6", font=("Segoe UI", 16, "bold"))
        title.pack(pady=10)

        # Frame for inputs
        input_frame = tk.Frame(self, bg="#2d2d30")
        input_frame.pack(pady=10, padx=10, fill="x")

        # Matricula label and entry
        matricula_label = tk.Label(input_frame, text="Matrícula:", bg="#2d2d30", fg="#dcdcdc", font=("Segoe UI", 10))
        matricula_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.matricula_entry = tk.Entry(input_frame, bg="#3e3e42", fg="#dcdcdc", insertbackground="white", relief="flat", font=("Segoe UI", 10))
        self.matricula_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Nome label and entry
        nome_label = tk.Label(input_frame, text="Nome:", bg="#2d2d30", fg="#dcdcdc", font=("Segoe UI", 10))
        nome_label.grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.nome_entry = tk.Entry(input_frame, bg="#3e3e42", fg="#dcdcdc", insertbackground="white", relief="flat", font=("Segoe UI", 10))
        self.nome_entry.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(3, weight=1)

        # Add button
        add_button = tk.Button(self, text="Adicionar", bg="#9b59b6", fg="white", activebackground="#8e44ad", relief="flat", font=("Segoe UI", 10, "bold"), command=self.add_student)
        add_button.pack(pady=10)

        # Treeview for student list
        self.tree = ttk.Treeview(self, columns=("matricula", "nome"), show="headings")
        self.tree.heading("matricula", text="Matrícula")
        self.tree.heading("nome", text="Nome")
        self.tree.column("matricula", width=150, anchor="center")
        self.tree.column("nome", anchor="w")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Style for Treeview
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("Treeview",
                        background="#3e3e42",
                        foreground="#dcdcdc",
                        fieldbackground="#3e3e42",
                        bordercolor="#9b59b6",
                        borderwidth=1,
                        font=("Segoe UI", 10))
        style.map("Treeview", background=[("selected", "#8e44ad")], foreground=[("selected", "white")])
        style.configure("Treeview.Heading",
                        background="#9b59b6",
                        foreground="white",
                        font=("Segoe UI", 10, "bold"))

    def add_student(self):
        matricula = self.matricula_entry.get().strip()
        nome = self.nome_entry.get().strip()
        if not matricula or not nome:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
            return
        try:
            self.cursor.execute("INSERT INTO students (matricula, nome) VALUES (?, ?)", (matricula, nome))
            self.conn.commit()
            self.matricula_entry.delete(0, tk.END)
            self.nome_entry.delete(0, tk.END)
            self.load_students()
        except sqlite3.IntegrityError:
            messagebox.showwarning("Erro", "Matrícula já cadastrada.")

    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.cursor.execute("SELECT matricula, nome FROM students ORDER BY id DESC")
        rows = self.cursor.fetchall()
        for matricula, nome in rows:
            self.tree.insert("", tk.END, values=(matricula, nome))

    def on_closing(self):
        self.conn.close()
        self.destroy()

if __name__ == "__main__":
    app = RoxynApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
