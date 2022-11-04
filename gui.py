from fileinput import filename
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import code
from stegano import lsb 
from randimage import get_random_image, show_array
from tkinter import messagebox
import base64
import matplotlib as mp
from cryptography.fernet import Fernet


root=Tk()
root.title("Lockshield - Hide a Secret Text Message in an Image")
root.geometry ("1280x676")
root.resizable(False, False)
root.configure(bg="#2f4155")
bg = Image.open("E:/FrAgnel/Sem 7/Major project/images/mainbackground.jpg")
bck_end=ImageTk.PhotoImage(bg)
lbl_back=Label(root, image=bck_end)
lbl_back.place(x=0,y=0)

global key 
key = ""

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.*")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage (img)
    lbl.configure(image=img,width=420,height=350)
    lbl.image=img

def Hide():
    messagebox.showinfo("Info","The data has been successfully hidden")
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def generate():
    img_size = (250,250)
    imgarr = get_random_image(img_size)
    mp.image.imsave("randimage.png", imgarr)
    img=Image.open("randimage.png")
    img=ImageTk.PhotoImage(img)
    showimage()

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)
def save():
    messagebox.showinfo("Info","The image has been saved")
    secret.save("Generated_Image.png")

def save_png():
    messagebox.showinfo("Info","The image has been saved")
    secret.save("Generated_Image.png")

def save_jpeg():
    messagebox.showinfo("Info","The image has been saved")
    secret.save("Generated_Image.jpeg")

def save_jpg():
    messagebox.showinfo("Info","The image has been saved")
    secret.save("Generated_Image.jpg")

# def Generate_key():
#     # key is generated
#     key = Fernet.generate_key()
#     label.configure(text=key)

def decrypt():
    password=code.get()
    
    if password == "1234":
        screen2 = Toplevel()
        screen2. title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0, END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg= "#00bd56").place(x=10,y=0)
        text2=Text(screen2,font= "Robote 10",bg= "white" ,relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)

    elif password=="":
        messagebox.showerror("encryption", "Input Password")
    elif password !="1234":
        messagebox.showerror("encryption", "Invalid Password")

def encrypt():
    password=code.get()
    
    if password == "1234":
        screen1 = Toplevel(root2)
        screen1. title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0, END)
        encode_message=message. encode("ascii")
        base64_bytes=base64. b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg= "#ed3833").place(x=10,y=0)
        text2=Text(screen1,font= "Robote 10",bg= "white" ,relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password=="":
        messagebox. showerror("encryption", "Input Password")
    elif password !="1234":
        messagebox.showerror("encryption", "Invalid Password")


def generate():
    global root2
    global code
    global text1

    root2 = Toplevel()
    root2.geometry("375x398")
    root2.title("Lockshield - Hide a Secret Text Message in an Image")
    Label(root2, text="Enter text for encryption and decryption" ,fg= "black", font=("calibri",13)).place(x=10,y=10)
    text1=Text(root2, font="Robote 20" ,bg="white" ,relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(root2, text="Enter secret key for encryption and decryption", fg="black",font=("calibri",13)).place(x=10,y=170)
    code=StringVar()
    Entry(root2, textvariable=code, width=19, bd=0, font=("arial",25),show="*").place(x=10,y=200)

    Button(root2, text= "ENCRYPT", height="2",width=23, bg= "#ed3833" ,fg= "white" ,bd=0, command=encrypt) .place (x=10,y=250)
    Button(root2, text= "DECRYPT",height="2",width=23, bg= "#00bd56" ,fg= "white" ,bd=0, command=decrypt).place (x=200,y=250)
    Button(root2, text= "RESET",height="2",width=50, bg= "#1089ff" ,fg= "white" ,bd=0, command=reset) .place(x=10,y=300)

    #icon
    image_icon=PhotoImage(file="keys.png")
    root2.iconphoto(False, image_icon)
    root2.title("LockShield")
    

    root2.mainloop()

# generate()


#icon
image_icon=PhotoImage(file="images/gear.png")
root. iconphoto(False,image_icon) 

logo=PhotoImage()
Label(root, image=logo, bg="black").place(x=10, y=0)
Label(root,text="LOCKSHIELD", bg="#2d4155",fg="#3ddac3",font="century 25"). place(x=525, y=40)

#first Frame
f=Frame(root, bd=3,bg="black" ,width=500, height=400, relief=GROOVE)
f.place(x=140-25,y=150-50)

lbl=Label(f, fg="black")
lbl.place(x=40,y=10)

#Second Frame
frame2=Frame (root, bd=3,width=500, height=400, bg="white" ,relief=GROOVE)
frame2.place(x=140+500+25, y=150-50)

text1=Text(frame2,font="Robote 20",bg="white", fg="black", relief=GROOVE,wrap=WORD)
text1.place(x=0, y=0,width=500,height=400)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=480,y=0,height=400)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


#third Frame
frame3=Frame (root, bd=3, bg="#3ddac3" ,width=500, height=120, relief=GROOVE)
frame3.place(x=140-25,y=150+400-50)



Button(frame3,text="Generate Image" ,width=12, height=2,font="arial 12 bold", command=generate).place(x=180, y=30)
Button(frame3,text="Open Image" ,width=12, height=2,font="arial 12 bold", command=showimage).place(x=20, y=30)
Button(frame3,text="Save .png" ,width=12,height=1,font="arial 12 bold", command=save_png) .place(x=340, y=0)
Button(frame3,text="Save .jpeg" ,width=12,height=1,font="arial 12 bold", command=save_jpeg) .place(x=340, y=40)
Button(frame3,text="Save .jpg" ,width=12,height=1,font="arial 12 bold", command=save_jpg) .place(x=340, y=80)

Label(frame3,text="Picture, Image, Photo File", bg="#2f4155", fg="white").place(x=20,y=5)
       
#fourth Frame
frame4=Frame(root, bd=3, bg="#3ddac3" ,width=500, height=120, relief=GROOVE)
frame4.place(x=140-25+500+25+25, y=150+400-50)

Button(frame4, text="Hide Data",width=10, height=2, font= "arial 12 bold", command=Hide) .place(x=20, y=5)
Button(frame4, text="Show Data",width=10,height=2,font="arial 12 bold", command=Show) .place(x=165, y=5)
# Button(frame4, text="Use another way",width=15,height=2,font="arial 12 bold", command=Show) .place(x=315, y=30)
Button(frame4, text="Symm key algo",width=15,height=2,font="arial 12 bold", command=generate).place(x=315, y=5)
# Label(frame4,text="Generated Key:",font="arial 12 bold",bg="#2f4155", fg="white") .place(x=20,y=60)
# label = Label(frame4,text="",bg="#2f4155", fg="white", relief=GROOVE) 
# label.place(x=20,y=90)




root.mainloop()