from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Image Based Captcha")

bottomFrame = Frame(root)
bottomFrame.place(y = 140) 






def showImg():

        load0= Image.open('/Users/abhilashyadav/Desktop/GUI/placeholder\(img\)/yo\ \(1\).png')
        render0 = ImageTk.PhotoImage(load0)
        img0= Label(image = render0)
        img0.image = render0
        img0.place(x = 0, y = 0)

        text1 = Label(text = 'Identify Cake' + '\n'+ 'Among These', font='Helvetica 18 bold')
        text1.place(x = 140)



        # text = Label(bottomFrame, text = 'Identify CAKES')
        # text.grid(row = 0)
        

        def onclick(args):
            if(args['relief'] == SUNKEN):
                args.config(relief = RAISED, borderwidth = 1, highlightthickness = 1)
            else:
                args.config(relief = SUNKEN, borderwidth = 3, highlightthickness = 3)

        
        load = Image.open('C:\\Users\\Paradise\\Desktop\\Trespass\\GUI\\images\\yo (9).jpg')
        render = ImageTk.PhotoImage(load)
        img = Button(bottomFrame, image = render, command =lambda:onclick(img), highlightcolor = 'blue', highlightbackground = 'red')
        img.image = render
        img.grid(row = 1, column = 0)



        load1 = Image.open('/Users/abhilashyadav/Desktop/GUI/images/yo%20(1).jpg')
        render1 = ImageTk.PhotoImage(load1)

        img1 = Button(bottomFrame, image = render1, command =lambda:onclick(img1))
        img1.image = render1
        img1.grid(row = 1, column = 1)
        
        load2 = Image.open('/Users/abhilashyadav/Desktop/GUI/images/yo%20(2).jpg')
        render2 = ImageTk.PhotoImage(load2)

        img2= Button(bottomFrame, image = render2, command =lambda:onclick(img2))
        img2.image = render2
        # img.place(x=0, y=0)
        img2.grid(row = 1, column = 2)
        
        load3 = Image.open('/Users/abhilashyadav/Desktop/GUI/images/yo%20(3).jpg')
        render3 = ImageTk.PhotoImage(load3)

        img3 = Button(bottomFrame, image = render3, command =lambda:onclick(img3))
        img3.image = render3
        # img.place(x=0, y=0)
        img3.grid(row = 2, column = 0)
        
        load4 = Image.open('C:\\Users\\Paradise\\Desktop\\Trespass\\GUI\\images\\yo (4).jpg')
        render4 = ImageTk.PhotoImage(load4)

        img4 = Button(bottomFrame, image = render4, command =lambda:onclick(img4))
        img4.image = render4
        # img.place(x=0, y=0)
        img4.grid(row = 2, column = 1)
        
        load5 = Image.open('C:\\Users\\Paradise\\Desktop\\Trespass\\GUI\\images\\yo (5).jpg')
        render5 = ImageTk.PhotoImage(load5)

        img5 = Button(bottomFrame, image = render5, command =lambda:onclick(img5))
        img5.image = render5
        # img.place(x=0, y=0)
        img5.grid(row = 2, column = 2)
        
        load6 = Image.open('C:\\Users\\Paradise\\Desktop\\Trespass\\GUI\\images\\yo (6).jpg')
        render6 = ImageTk.PhotoImage(load6)

        img6 = Button(bottomFrame, image = render6, command =lambda:onclick(img6))
        img6.image = render6
        # img.place(x=0, y=0)
        img6.grid(row = 3, column = 0)
        
        load7 = Image.open('C:\\Users\\Paradise\\Desktop\\Trespass\\GUI\\images\\yo (7).jpg')
        render7 = ImageTk.PhotoImage(load7)

        img7 = Button(bottomFrame, image = render7, command =lambda:onclick(img7))
        img7.image = render7
        # img.place(x=0, y=0)
        img7.grid(row = 3, column = 1)

        load8 = Image.open('C:\\Users\\Paradise\\Desktop\\Trespass\\GUI\\images\\yo (8).jpg')
        render8 = ImageTk.PhotoImage(load8)

        img8 = Button(bottomFrame, image = render8, command =lambda:onclick(img8))
        img8.image = render8
        # img.place(x=0, y=0)
        img8.grid(row = 3, column = 2)


        def verifyC():
            if((img1['relief'] == SUNKEN) and (img4['relief'] == SUNKEN) and (img5['relief'] == SUNKEN) and (img8['relief'] == SUNKEN) and (img['relief'] == SUNKEN) and (img2['relief'] == RAISED) and (img3['relief'] == RAISED) and (img6['relief'] == RAISED) and (img7['relief'] == RAISED)):
                # print("YO")
                window = Tk()
                window.geometry("300x100")
                text = Label(window, text = 'You are redirected to the' +'\n' + 'next page, plz wait', font='Helvetica 18 bold')
                text.pack()
                button1 = Button(window, text = 'Close', command = window.destroy)
                button1.pack() 
                

            else:
                window = Tk()
                window.geometry("200x100")
                text = Label(window, text = "You are a bot!", font='Helvetica 18 bold')
                text.pack()
                button1 = Button(window, text = 'Close', command = window.destroy)
                button1.pack() 





                

        verify = Button(bottomFrame, text = "VERIFY", borderwidth = 10, highlightthickness = 10, bg = 'dodgerblue2', command = verifyC)
        verify.grid(row = 4, column = 2)






menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New")
filemenu.add_command(label = "Show Images", command = showImg)
filemenu.add_command(label = 'Skip to Next')
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy)

menubar.add_cascade(label = 'File', menu = filemenu)


root.config(menu = menubar)


root.mainloop()