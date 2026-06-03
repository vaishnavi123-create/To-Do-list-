from tkinter import *
root = Tk()
root.title("My First GUI")
root.geometry("400x500")
def show_text():
    task = task_entry.get()
    listbox.insert(END, task)
    task_entry.delete(0,END)
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
def clear_all():
    listbox.delete(0,END)
label = Label(root, text="TO-DO LIST",font=("Arial", 20))
label.pack()
task_entry = Entry(root, width=30,font=("Arial", 14))
task_entry.pack(pady=10)
button = Button(root, text="Add Task", command=show_text)
button.pack()
delete_button = Button(root,text="Delete Task", command=delete_task)
delete_button.pack()
clear_button = Button(root,text="Clear All", command=clear_all)
clear_button.pack()
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack()
listbox = Listbox(root, width=35,height=10)
listbox.pack()
root.mainloop()
