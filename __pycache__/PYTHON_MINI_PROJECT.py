from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
from tkinter.constants import END

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_des.get()
    masg=Sor_txt.get(1.0,END)
    textget=change(text = masg, src=s , dest=d)
    des_txt.delete(1.0,END)
    des_txt.insert(END,textget)

root = Tk()
root.title(" GOOGLE TRANSLATOR ")
root.geometry("500x700")
root.config(bg='orange')

lab_txt = Label(root,text="Translator",font=("Time New Roman ",40,"bold"),bg="pink")
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root)
frame2=frame.pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Time New Roman ",20,"bold"),fg="black",bg="orange")
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt = Text(frame2,font=("Time New Roman ",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame2,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")

button_change = Button(frame2,text="Translate",relief=RAISED ,command = data)
button_change.place(x=170,y=300,height=40,width=150)

comb_des = ttk.Combobox(frame2,value=list_text)
comb_des.place(x=330,y=300,height=40,width=150)
comb_des.set("English")

lab_txt = Label(root,text="Destination Text",font=("Time New Roman ",20,"bold"),fg="black",bg="orange")
lab_txt.place(x=100,y=360,height=20,width=300)

des_txt = Text(frame2,font=("Time New Roman ",20,"bold"),wrap=WORD)
des_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()

