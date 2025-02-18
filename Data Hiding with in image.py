from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

win=Tk()
win.geometry("700x480")
win.config(bg="black")

#Button Function
def open_image():
    global open_file
    open_file = filedialog.askopenfilename(title="Select Image", filetypes=(("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")))
    img = Image.open(open_file)
    img = img.resize((250, 220), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lf1.config(image=img)
    lf1.image = img

def hide():
    global hide_msg
    password=code.get()
    if password=="1234":
        msg=text1.get("1.0",END)
        hide_msg=lsb.hide(str(open_file),msg)
        messagebox.showinfo("Success","Your MSG is Hidden Successfully in an image,please save you")
    elif password =="":
        messagebox.showerror("Error","Please Enter Secret Key")
    else:
          messagebox.showerror("Error","Invalid Secret Key")  
          code.set("")

def save_img():
    hide_msg.save("save_file.png")
    messagebox.showinfo("Success","Your Image is Saved Successfully")

def show():
    password=code.get()
    if password=="1234":
        show_msg=lsb.reveal(open_file)
        text1.delete("1.0",END)
        text1.insert(END,show_msg)
    elif password =="":
        messagebox.showerror("Error","Please Enter Secret Key")
    else:
          messagebox.showerror("Error","Invalid Secret Key")  
          code.set("")        

#logo
# logo=PhotoImage(file="images.png")
# Label(win,width=50,height=50,image=logo,bd=0).place(x=60,y=10)

#heading
Label(win,text="Cyber Security",font='imapck 30 bold',bg="black",fg="red").place(x=200,y=21)

#frame 1
f1 = Frame(win,width =250,height=220,bd=5,bg="purple")
f1.place(x=50,y=100)
lf1=Label(f1,bg="purple")
lf1.place(x=0,y=0)

#frame 2
f2 = Frame(win,width =320,height=220,bd=5,bg="white")
f2.place(x=330,y=100)
text1=Text(f2, font="ariel 15 bold",wrap=WORD)
text1.place(x=0,y=0,width=310,height=210)

#Label for secret key
Label(win,text="Enter Secret Key",font="ariel 15 bold",bg="black",fg="white").place(x=270,y=330)

#Entry widget for secret key
code=StringVar()
e=Entry(win, textvariable=code,font="impact 10 bold",bd=2,show="*")
e.place(x=245,y=360)

#buttons
open_button=Button(win,text='Open Image',bg='blue',fg='white',font='ariel 12 bold',cursor='hand2',command=open_image)
open_button.place(x=60,y=417)

save_button=Button(win,text='Save Image',bg='green',fg='white',font='ariel 12 bold',cursor='hand2',command=save_img)
save_button.place(x=190,y=417)

hide_button=Button(win,text='Hide Data',bg='red',fg='white',font='ariel 12 bold',cursor='hand2',command=hide)
hide_button.place(x=380,y=417)

show_button=Button(win,text='Show Data',bg='orange',fg='white',font='ariel 12 bold',cursor='hand2',command=show)
show_button.place(x=510,y=417)

mainloop()  