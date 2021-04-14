from tkinter import *
from pytube import YouTube
import os

def ten():
    name = str(os.getlogin())
    save_path = "C:\\Users\\"+name+"\\Downloads"
    use_link = "https://www.y2mate.com/youtube/"+link.get()[32:43]
    Label(window1, text="You can also copy and paste this link in your browser to download via Website interface", bg="#506680", fg="black", font=('Arial 9 bold')).place(x=100,y=230)

    ent = Entry(window1, state='readonly', readonlybackground='yellow', fg='black')
    var = StringVar()
    var.set(use_link)
    ent.config(textvariable=var, relief='flat', width=41, font=('Helvetica 15'))
    ent.place(x=120, y=250)

    rohit_varma = Label(window1, text="Loved my software?? Please follow me on Instagram -> [i_rohit_varma]\n Youtube -> [Circuit Jet] & Github -> [amrav-tihor]\n- made by Rohit Varma for open source\n\nYour downloaded video is in path: '"+save_path+"' !!", bg="#506680", fg="black", font=('Helvetica 13 bold')).place(x=70, y=290)

    video = YouTube("https://youtu.be/"+link.get()[32:43]).streams.filter(res="1080p").first().download(save_path)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
def seven():
    name = str(os.getlogin())
    save_path = "C:\\Users\\"+name+"\\Downloads"
    use_link = "https://www.y2mate.com/youtube/"+link.get()[32:43]
    Label(window1, text="You can also copy and paste this link in your browser to download via Website interface", bg="#506680", fg="black").place(x=114,y=230)
    ent = Entry(window1, state='readonly', readonlybackground='yellow', fg='black')
    var = StringVar()
    var.set(use_link)
    ent.config(textvariable=var, relief='flat', width=39, font=('Helvetica 15'))
    ent.place(x=120, y=250)

    rohit_varma = Label(window1, text="Loved my software?? Please follow me on Instagram -> [i_rohit_varma]\n Youtube -> [Circuit Jet] & Github -> [amrav-tihor]\n- made by Rohit Varma for open source\n\nYour downloaded video is in path: '"+save_path+"' !!", bg="#506680", fg="black", font=('Helvetica 13 bold')).place(x=70, y=290)

    video = YouTube("https://youtu.be/"+link.get()[32:43]).streams.filter(res="720p").first().download(save_path)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def four():
    name = str(os.getlogin())
    save_path = "C:\\Users\\"+name+"\\Downloads"
    use_link = "https://www.y2mate.com/youtube/"+link.get()[32:43]
    Label(window1, text="You can also copy and paste this link in your browser to download via Website interface", bg="#506680", fg="black").place(x=114,y=230)

    ent = Entry(window1, state='readonly', readonlybackground='yellow', fg='black')
    var = StringVar()
    var.set(use_link)
    ent.config(textvariable=var, relief='flat', width=39, font=('Helvetica 15'))
    ent.place(x=120, y=250)

    rohit_varma = Label(window1, text="Loved my software?? Please follow me on Instagram -> [i_rohit_varma]\n Youtube -> [Circuit Jet] & Github -> [amrav-tihor]\n- made by Rohit Varma for open source\n\nYour downloaded video is in path: '"+save_path+"' !!", bg="#506680", fg="black", font=('Helvetica 13 bold')).place(x=70, y=290)

    video = YouTube("https://youtu.be/"+link.get()[32:43]).streams.filter(res="480p").first().download(save_path)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def three():
    name = str(os.getlogin())
    save_path = "C:\\Users\\"+name+"\\Downloads"
    use_link = "https://www.y2mate.com/youtube/"+link.get()[32:43]
    Label(window1, text="You can also copy and paste this link in your browser to download via Website interface", bg="#506680", fg="black").place(x=114,y=230)

    ent = Entry(window1, state='readonly', readonlybackground='yellow', fg='black')
    var = StringVar()
    var.set(use_link)
    ent.config(textvariable=var, relief='flat', width=39, font=('Helvetica 15'))
    ent.place(x=120, y=250)

    rohit_varma = Label(window1, text="Loved my software?? Please follow me on Instagram -> [i_rohit_varma]\n Youtube -> [Circuit Jet] & Github -> [amrav-tihor]\n- made by Rohit Varma for open source\n\nYour downloaded video is in path: '"+save_path+"' !!", bg="#506680", fg="black", font=('Helvetica 13 bold')).place(x=70, y=290)

    video = YouTube("https://youtu.be/"+link.get()[32:43]).streams.filter(res="360p").first().download(save_path)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def one():
    name = str(os.getlogin())
    save_path = "C:\\Users\\"+name+"\\Downloads"
    use_link = "https://www.y2mate.com/youtube/"+link.get()[32:43]
    Label(window1, text="You can also copy and paste this link in your browser to download via Website interface", bg="#506680", fg="black").place(x=114,y=230)

    ent = Entry(window1, state='readonly', readonlybackground='yellow', fg='black')
    var = StringVar()
    var.set(use_link)
    ent.config(textvariable=var, relief='flat', width=39, font=('Helvetica 15'))
    ent.place(x=120, y=250)

    rohit_varma = Label(window1, text="Loved my software?? Please follow me on Instagram -> [i_rohit_varma]\n Youtube -> [Circuit Jet] & Github -> [amrav-tihor]\n- made by Rohit Varma for open source\n\nYour downloaded video is in path: '"+save_path+"' !!", bg="#506680", fg="black", font=('Helvetica 13 bold')).place(x=70, y=290)

    video = YouTube("https://youtu.be/"+link.get()[32:43]).streams.filter(res="144p").first().download(save_path)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def first():
    global window1, link
    name = str(os.getlogin())
    window1 = Tk()
    window1.geometry('700x400')
    window1.title("Rohit's YT Downloader")
    window1.configure(bg="#506680")
    link = StringVar()
    title = Label(window1, text="***Welcome to my Youtube video Downloader***", font=('Arial 18 bold underline'), bg="#506680", fg="cyan").pack(pady=10)
    text1 = Label(window1, text="Hey "+name+", Please enter the link of the video you want to download below\nCTRL+V to paste", bg="#506680", fg="black", font=('Arial 12 bold')).pack(pady=10)
    link_entry = Entry(window1, text="Enter Link here!!!", bg="#081B33", borderwidth=5, bd="5", fg="white", justify="left", width="69", font=('Helvetica 12'), textvariable=link).pack()
    button1 = Button(window1, text="1080P", width=10, font=('Arial 13'), bg="red", fg="white", command=ten).place(x=60,y=165)
    button2 = Button(window1, text="720P", width=10, font=('Arial 13'), bg="#CC3333", fg="white", command=seven).place(x=180,y=165)
    button3 = Button(window1, text="480P", width=10, font=('Arial 13'), bg="gold", fg="black", command=four).place(x=300,y=165)
    button4 = Button(window1, text="360P", width=10, font=('Arial 13'), bg="lime", fg="black", command=three).place(x=420,y=165)
    button5 = Button(window1, text="144P", width=10, font=('Arial 13'), bg="green", fg="black", command=one).place(x=540,y=165)
    window1.mainloop()


first()