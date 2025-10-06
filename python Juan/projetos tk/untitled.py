import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota_texto = entry_nota.get()
    try:
        nota = float(nota_texto)
        if nota >= 10:
            messagebox.showinfo("Resultado", "Parabéns, nota máxima!")
        elif nota >= 9:
            messagebox.showinfo("Resultado", "Quase perfeito")
        elif nota >= 7:
            messagebox.showinfo("Resultado", "Aprovado")
        elif nota >= 5:
            messagebox.showinfo("Resultado", "Recuperação")
        else:
            messagebox.showinfo("Resultado", "Reprovado com nota baixa")
    except ValueError:
        messagebox.showerror("Erro", "Digite uma nota válida.")

root = tk.Tk()
root.title("Verificador de Nota")
root.geometry("400x220")
root.configure(bg="#ffffff")

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=150)

tk.Label(frame, text="Digite a nota:", font=("Arial", 14), bg="#ffffff").pack(pady=(15,5))
entry_nota = tk.Entry(frame, font=("Arial", 12), justify="center")
entry_nota.pack(pady=5)

tk.Button(frame, text="Verificar", font=("Arial", 12), bg="#4caf50", fg="white", command=verificar_nota).pack(pady=15)

root.mainloop()