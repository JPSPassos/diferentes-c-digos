import tkinter as tk

janela = tk.Tk()
janela.title('Calculadora Simples')

entrada_var = tk.StringVar()
display = tk.Entry(
    janela,
    textvariable= entrada_var,
    font = ('Arial', 16),
    justify='right'
)
display.pack(fill='both', padx=10, pady=10)

tk.Button(janela, text="7", command=lambda: entrada_var.set(entrada_var.get()+"7")).pack(side="left")
tk.Button(janela, text="8", command=lambda: entrada_var.set(entrada_var.get()+"8")).pack(side="left")
tk.Button(janela, text="9", command=lambda: entrada_var.set(entrada_var.get()+"9")).pack(side="left")
tk.Button(janela, text="/", command=lambda: entrada_var.set(entrada_var.get()+"/")).pack(side="left")

tk.Button(janela, text="4", command=lambda: entrada_var.set(entrada_var.get()+"4")).pack(side="left")
tk.Button(janela, text="5", command=lambda: entrada_var.set(entrada_var.get()+"5")).pack(side="left")
tk.Button(janela, text="6", command=lambda: entrada_var.set(entrada_var.get()+"6")).pack(side="left")
tk.Button(janela, text="*", command=lambda: entrada_var.set(entrada_var.get()+"*")).pack(side="left")

tk.Button(janela, text="1", command=lambda: entrada_var.set(entrada_var.get()+"1")).pack(side="left")
tk.Button(janela, text="2", command=lambda: entrada_var.set(entrada_var.get()+"2")).pack(side="left")
tk.Button(janela, text="3", command=lambda: entrada_var.set(entrada_var.get()+"3")).pack(side="left")
tk.Button(janela, text="-", command=lambda: entrada_var.set(entrada_var.get()+"-")).pack(side="left")

tk.Button(janela, text="0", command=lambda: entrada_var.set(entrada_var.get()+"0")).pack(side="left")
tk.Button(janela, text=".", command=lambda: entrada_var.set(entrada_var.get()+"." )).pack(side="left")

tk.Button(janela, text='=', command=lambda: entrada_var.set(str(eval(entrada_var.get())))).pack(side='left')
tk.Button(janela, text='+', command=lambda: entrada_var.set(entrada_var.get()+'+')).pack(side='left')
tk.Button(janela, text='C', command=lambda: entrada_var.set('')).pack(side='left')

janela.mainloop()