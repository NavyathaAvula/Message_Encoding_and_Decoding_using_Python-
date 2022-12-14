from tkinter import *
from tkinter import messagebox
/*base64 module provides a function to encode the binary data to ASCII characters and decode that ASCII characters back to binary data.*/
import base64
import os

def decrypt():
   passward=code.get()
    
   if passward=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#b2ebcc")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="ENCRYPT",font="arial",fg="white",bg="#b2ebcc").place(x=10,y=0)
        text2=Text(screen2,font="Rpbote 10" , bg="white" ,relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

   elif passward=="":
        messagebox.showerror("encryption","Input Password")

   elif passward !="1234":
        messagebox.showerror("encryption","Invalid Password")

def encrypt():        
   passward=code.get()
    
   if passward=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#b2ebcc")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="DECRYPT",font="arial",fg="white",bg="#b2ebcc").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10" , bg="white" ,relief=GROOVE, wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

   elif passward=="":
        messagebox.showerror("encryption","Input Password")

   elif passward !="1234":
        messagebox.showerror("encryption","Invalid Password")




def main_screen():

   global screen
   global code
   global text1
   
   screen=Tk()
   screen.geometry("375x398")

   screen.title("Encryption And Decryption-navayatha")

   def reset():
      code.set("")
      text1.delete(1.0,END)

   Label(text="Enter text for encryption or decryption" ,fg="black" ,font=("calbri",13)).place(x=10,y=10)
   text1=Text(font="Robot 20" ,bg="white" ,relief=GROOVE,wrap=WORD,bd=0)
   text1.place(x=10,y=50,width=355,height=100)

   Label(text="Enter key for encryption or decryption" ,fg="black" ,font=("calbri",13)).place(x=10,y=170)

   code=StringVar()
   Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)


   Button(text="ENCRYPT",height="2",width=23,bg="#b2ebcc",fg="black",bd=0,command=decrypt).place(x=10,y=250)
   Button(text="DECRYPT",height="2",width=23,bg="#b2ebcc",fg="black",bd=0,command=encrypt).place(x=200,y=250)
   Button(text="RESET",height="2",width=50,bg="#b2ebcc",fg="black",bd=0,command=reset).place(x=10,y=300)
   

   screen.mainloop()
main_screen()


   
        
