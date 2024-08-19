import tkinter as tk
def evaluate(event):
    result_label.config(text=str(eval(entry.gat())))
root = tk.Tk()
root.title("Calculadora Simples")
entry = tk.Entry(root)
entry.bind("<Return>", evaluate)
entry.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.geometry("250x80")
root.mainloop()