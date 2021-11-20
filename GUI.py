from tkinter import *
from tkinter import scrolledtext, messagebox, filedialog, Menu, ttk
from os import path
from tkinter.ttk import *

window = Tk()
window.geometry('400x400')
window.title("GUI Demo")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
tab_control.pack(expand=1, fill='both')

lbl = Label(tab1, text="Hello", font=("Arial", 14))
lbl.grid(column=0, row=0, sticky=N+W) #, padx=5, pady=5

input = Entry(tab1,width=10)
input.grid(column=0, row=1, sticky=N+W)
input.focus()

def clicked():
    result = "Result: " + input.get()
    lbl.configure(text=result)
btn = Button(tab1, text="Click Me", command=clicked)
btn.grid(column=1, row=1, sticky=N+W)

combo = Combobox(tab1)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=2, sticky=N+W)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(tab1, text='Choose', var=chk_state)
chk.grid(column=1, row=2, sticky=N+W)
# chk_state = IntVar()
# chk_state.set(0) #uncheck
# chk_state.set(1) #check

selected = IntVar()
rad1 = Radiobutton(tab1,text='First', value=1, variable=selected)
rad2 = Radiobutton(tab1,text='Second', value=2, variable=selected)
rad3 = Radiobutton(tab1,text='Third', value=3, variable=selected)
rad1.grid(column=0, row=3, sticky=N+W)
rad2.grid(column=1, row=3, sticky=N+W)
rad3.grid(column=2, row=3, sticky=N+W)

txt = scrolledtext.ScrolledText(tab2,width=40,height=10)
txt.grid(column=3, row=3, sticky=N+W)
# txt.insert(INSERT,'You text goes here')
# txt.delete(1.0,END)

messagebox.showinfo('Message title','Message content')
# messagebox.showwarning('Message title', 'Message content')  #shows warning message
# messagebox.showerror('Message title', 'Message content')    #shows error message
# res = messagebox.askquestion('Message title','Message content')
# res = messagebox.askyesno('Message title','Message content')
# res = messagebox.askyesnocancel('Message title','Message content')
# res = messagebox.askokcancel('Message title','Message content')
# res = messagebox.askretrycancel('Message title','Message content')

file = filedialog.askopenfilename()
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
# dir = filedialog.askdirectory()
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))


menu = Menu(window)
menu.add_command(label='File')
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
# new_item = Menu(menu, tearoff=0)
# new_item.add_command(label='New', command=clicked)

window.config(menu=menu)
window.mainloop()