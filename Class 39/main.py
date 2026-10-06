#text editor
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
#set up window
window = Tk()
window.title("text editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def open_file():
    filepath = askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    textarea.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text=input_file.read()
        textarea.insert(END,text)
        input_file.close()
    window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension="txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = textarea.get(1.0, END)
        output_file.write(text)
        window.title(f"Text Editor - {filepath}")



#add widgets
textarea = Text(window)
frame1 = Frame(window,relief=RAISED,bd=2)
buttonopen = Button(frame1,text="open",command=open_file)
buttonsave = Button(frame1,text="save as",command=save_file)
buttonopen.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
buttonsave.grid(row=1,column=0,sticky="ew",padx=5)
frame1.grid(row=0,column=0,sticky="ns")
textarea.grid(row=0,column=1,sticky="nsew")
window.mainloop()