import tkinter as tk

root = tk.Tk()
root.title("Pac-Man")

canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

# Рисуем тело Пакмана (желтый круг с "вырезанным" ртом)
canvas.create_arc(50, 50, 250, 250, start=30, extent=300, fill="yellow", outline="yellow")

# Глаз Пакмана
canvas.create_oval(170, 80, 190, 100, fill="black")

root.mainloop()
