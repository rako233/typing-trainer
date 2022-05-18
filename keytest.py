import tkinter as tk

def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, ))
    print(event)

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('DejaVu Sans', 16))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()


