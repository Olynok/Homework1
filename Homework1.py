import tkinter as tk
settings = {
    'color': '#f53b0c',
}
window = tk.Tk()

window.title('My Homework1')
window.geometry('1000x400')
window.minsize(300, 300)
window.maxsize(1000, 1000)
window.resizable(True, True)

label1 = tk.Label(text='Добрий вечір! Я Михайло. Це моє перше завдання.', fg=settings['color'], font=("Comic Sans MS", 32))
label1.pack()
window.mainloop()