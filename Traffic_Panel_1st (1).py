from Tkinter import *
import Tkinter
import tkFileDialog
from PIL import Image,ImageTk
import numpy as np
import sys
import tkMessageBox
import cv2
import os
import time
from threading import Timer

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Automatic_Traffic_Monitoring (root)
    root.mainloop()

class Automatic_Traffic_Monitoring:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
                  top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 11 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 13 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 11 -weight bold -slant " \
                 "italic -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman " \

        top.geometry("1920x1000+23+74")
        top.title("Automatic Traffic Monitoring")
        top.configure(background="#8080c0")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.cap = cv2.VideoCapture('video//video2.avi')
        self.cap2 = cv2.VideoCapture('video//video2.avi')
        self.cap3 = cv2.VideoCapture('video//video2.avi')
        self.cap4 = cv2.VideoCapture('video//video2.avi')
        self.count=0
        self.count2=0
        self.count3=0
        self.count4=0
        self.activesignal=1
        self.limit=10
        self.counting=0
        self.flag=0
        image = Image.open("signalimages/greenlight1.png")
        self.greenlogo = ImageTk.PhotoImage(image)
        imagered = Image.open("signalimages/redlight1.png")
        self.redlogo = ImageTk.PhotoImage(imagered)
        self.car_cascade = cv2.CascadeClassifier('cascade_classifier/cars3.xml')

        self.menubar = Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.36, rely=0.03, height=31, width=487)
        self.Label1.configure(activebackground="#8000ff")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#ffffff")
        self.Label1.configure(background="#8080c0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Traffic Monitoring Project''')

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.44, relheight=0.53, relwidth=0.97)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1855)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.01, rely=0.19, height=261, width=287)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#808080")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(width=287)

        self.Label10 = Label(self.Frame1)
        self.Label10.place(relx=0.02, rely=0.02, height=31, width=117)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font=font9)
        self.Label10.configure(foreground="#ff0000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''ROAD 1''')

        self.Label11 = Label(self.Frame1)
        self.Label11.place(relx=0.27, rely=0.02, height=31, width=117)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font=font9)
        self.Label11.configure(foreground="#ff0000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''ROAD 2''')

        self.Label12 = Label(self.Frame1)
        self.Label12.place(relx=0.52, rely=0.02, height=31, width=117)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font=font9)
        self.Label12.configure(foreground="#ff0000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''ROAD 3''')

        self.Label13 = Label(self.Frame1)
        self.Label13.place(relx=0.76, rely=0.02, height=31, width=117)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font=font9)
        self.Label13.configure(foreground="#ff0000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''ROAD 4''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.26, rely=0.19, height=261, width=287)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#808080")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.51, rely=0.19, height=261, width=287)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#808080")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.76, rely=0.19, height=261, width=287)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#808080")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.06, rely=0.03, height=42, width=118)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''START''')
        self.Button1.configure(width=118)
        self.Button1.configure(command=self.start)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.05, rely=0.11, relheight=0.32, relwidth=0.89)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=1715)

        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.06, rely=0.08, height=181, width=87)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#808080")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(width=87)

        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.29, rely=0.08, height=181, width=87)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#808080")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(width=87)

        self.Label8 = Label(self.Frame2)
        self.Label8.place(relx=0.57, rely=0.08, height=181, width=87)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#808080")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(width=87)

        self.Label9 = Label(self.Frame2)
        self.Label9.place(relx=0.82, rely=0.09, height=181, width=87)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#808080")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(width=87)

        self.Label14 = Label(self.Frame2)
        self.Label14.place(relx=0.03, rely=0.1, height=31, width=57)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#ffffff")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font=font12)
        self.Label14.configure(foreground="#ff0000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''0''')
        self.Label14.configure(width=57)

        self.Label15 = Label(self.Frame2)
        self.Label15.place(relx=0.25, rely=0.1, height=31, width=57)
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(background="#ffffff")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(font=font12)
        self.Label15.configure(foreground="#ff0000")
        self.Label15.configure(highlightbackground="#d9d9d9")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(text='''0''')

        self.Label16 = Label(self.Frame2)
        self.Label16.place(relx=0.53, rely=0.1, height=31, width=57)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(font=font12)
        self.Label16.configure(foreground="#ff0000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''0''')

        self.Label17 = Label(self.Frame2)
        self.Label17.place(relx=0.78, rely=0.1, height=31, width=57)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(background="#ffffff")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(font=font12)
        self.Label17.configure(foreground="#ff0000")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(text='''0''')

    def start(self):

       self.road1()
       self.road2()
       self.road3()
       self.road4()
       self.controlunit()

    def road1(self):
        #print self.cap.isOpened()
        # Trained XML classifiers describes some features of some object we want to detect



        ret, frames = self.cap.read()

        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # Detects cars of different sizes in the input image
        cars = self.car_cascade.detectMultiScale(gray, 1.1, 1)

        # To draw a rectangle in each cars
        i = 0
        for (x, y, w, h) in cars:
            i = i + 1
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.putText(frames, str(i), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
        self.count=i
        i = 0

        b, g, r = cv2.split(frames)
        img = cv2.merge((r, g, b))
        im = Image.fromarray(img)
        logo = ImageTk.PhotoImage(image=im)
        self.Label2.configure(compound=Tkinter.CENTER, image=logo)
        self.Label2.image = logo
        self.Label2.after(1000, self.road1)

        # cv2.imshow('video2', frames)

        # Wait for Esc key to stop


        # De-allocate any associated memory usage
        #cv2.destroyAllWindows()

    def road2(self):
        #print self.cap2.isOpened()
        # Trained XML classifiers describes some features of some object we want to detect



        ret, frames = self.cap2.read()

        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # Detects cars of different sizes in the input image
        cars = self.car_cascade.detectMultiScale(gray, 1.1, 1)

        # To draw a rectangle in each cars
        i = 0
        for (x, y, w, h) in cars:
            i = i + 1
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.putText(frames, str(i), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
        self.count2=i
        i = 0

        b, g, r = cv2.split(frames)
        img = cv2.merge((r, g, b))
        im = Image.fromarray(img)
        logo = ImageTk.PhotoImage(image=im)
        self.Label3.configure(compound=Tkinter.CENTER, image=logo)
        self.Label3.image = logo
        self.Label3.after(1000, self.road2)

        # cv2.imshow('video2', frames)

        # Wait for Esc key to stop


        # De-allocate any associated memory usage
        #cv2.destroyAllWindows()

    def road3(self):
        #print self.cap3.isOpened()
        # Trained XML classifiers describes some features of some object we want to detect



        ret, frames = self.cap3.read()

        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # Detects cars of different sizes in the input image
        cars = self.car_cascade.detectMultiScale(gray, 1.1, 1)

        # To draw a rectangle in each cars
        i = 0
        for (x, y, w, h) in cars:
            i = i + 1
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.putText(frames, str(i), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
        self.count3=i
        i = 0

        b, g, r = cv2.split(frames)
        img = cv2.merge((r, g, b))
        im = Image.fromarray(img)
        logo = ImageTk.PhotoImage(image=im)
        self.Label4.configure(compound=Tkinter.CENTER, image=logo)
        self.Label4.image = logo
        self.Label4.after(1000, self.road3)

        # cv2.imshow('video2', frames)

        # Wait for Esc key to stop


        # De-allocate any associated memory usage
        #cv2.destroyAllWindows()

    def road4(self):
        #print self.cap4.isOpened()
        # Trained XML classifiers describes some features of some object we want to detect



        ret, frames = self.cap4.read()

        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # Detects cars of different sizes in the input image
        cars = self.car_cascade.detectMultiScale(gray, 1.1, 1)

        # To draw a rectangle in each cars
        i = 0
        for (x, y, w, h) in cars:
            i = i + 1
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.putText(frames, str(i), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
        self.count4=i
        i = 0

        b, g, r = cv2.split(frames)
        img = cv2.merge((r, g, b))
        im = Image.fromarray(img)
        logo = ImageTk.PhotoImage(image=im)
        self.Label5.configure(compound=Tkinter.CENTER, image=logo)
        self.Label5.image = logo
        self.Label5.after(1000, self.road4)

        # cv2.imshow('video2', frames)

        # Wait for Esc key to stop


        # De-allocate any associated memory usage
        #cv2.destroyAllWindows()

    def controlunit(self):

        if self.flag==0:
            if self.activesignal==1:
                if self.count>=0 and self.count<=4:
                    self.limit=10
                else:
                    self.limit=20
            elif self.activesignal==2:
                if self.count2>=0 and self.count2<=4:
                    self.limit=10
                else:
                    self.limit=20
            elif self.activesignal==3:
                if self.count3>=0 and self.count3<=4:
                    self.limit=10
                else:
                    self.limit=20
            elif self.activesignal==4:
                if self.count4>=0 and self.count4<=4:
                    self.limit=10
                else:
                    self.limit=20
            self.flag=1


        if self.activesignal==1:
            self.Label6.configure(compound=Tkinter.CENTER, image=self.greenlogo)
            self.Label6.image = self.greenlogo
            self.Label7.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label7.image = self.redlogo
            self.Label8.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label8.image = self.redlogo
            self.Label9.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label9.image = self.redlogo
            self.Label14.config(text=self.counting)
            self.Label15.config(text='0')
            self.Label16.config(text='0')
            self.Label17.config(text='0')
            self.counting=self.counting+1
            if self.counting==self.limit:
                self.counting=0
                self.activesignal=2
                self.flag=0


        elif self.activesignal==2:
            self.Label6.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label6.image = self.redlogo
            self.Label7.configure(compound=Tkinter.CENTER, image=self.greenlogo)
            self.Label7.image = self.greenlogo
            self.Label8.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label8.image = self.redlogo
            self.Label9.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label9.image = self.redlogo
            self.Label14.config(text='0')
            self.Label15.config(text=self.counting)
            self.Label16.config(text='0')
            self.Label17.config(text='0')
            self.counting = self.counting + 1
            if self.counting == self.limit:
                self.counting = 0
                self.activesignal = 3
                self.flag = 0

        elif self.activesignal == 3:
            self.Label6.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label6.image = self.redlogo
            self.Label7.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label7.image = self.redlogo
            self.Label8.configure(compound=Tkinter.CENTER, image=self.greenlogo)
            self.Label8.image = self.greenlogo
            self.Label9.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label9.image = self.redlogo
            self.Label14.config(text='0')
            self.Label15.config(text='0')
            self.Label16.config(text=self.counting)
            self.Label17.config(text='0')
            self.counting = self.counting + 1
            if self.counting == self.limit:
                self.counting = 0
                self.activesignal = 4
                self.flag = 0

        elif self.activesignal == 4:
            self.Label6.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label6.image = self.redlogo
            self.Label7.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label7.image = self.redlogo
            self.Label8.configure(compound=Tkinter.CENTER, image=self.redlogo)
            self.Label8.image = self.redlogo
            self.Label9.configure(compound=Tkinter.CENTER, image=self.greenlogo)
            self.Label9.image = self.greenlogo
            self.Label14.config(text='0')
            self.Label15.config(text='0')
            self.Label16.config(text='0')
            self.Label17.config(text=self.counting)
            self.counting = self.counting + 1
            if self.counting == self.limit:
                self.counting = 0
                self.activesignal = 1
                self.flag = 0

        self.Label1.after(1000, self.controlunit)


if __name__ == '__main__':
    vp_start_gui()

