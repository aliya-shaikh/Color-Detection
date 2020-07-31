from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
from random import randrange

root = Tk()
root.title("Color Detector")
root.geometry("1350x700+0+0")

def open():
	label.config(text = "You selected : " + var.get())
	label.pack()
	if var.get() == "Image":
		button1 = Button(root,text="Browse a file",command=imagebutton)
		button1.pack()
	if var.get() == "Video":
		button2 = Button(root,text='Browse a file',command=videobutton)
		button2.pack()
	if var.get() == "Webcam":
		button3 = Button(root,text='Start',command=webacambutton)
		button3.pack()

def imagebutton():
	imagefile = filedialog.askopenfilename(initialdir ='/',title='Select A File',filetypes=(("jpeg", "*.jpg",".png"),("All Files","*.*")))
	img = cv2.imread(imagefile)
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	low_red = np.array([161,155,84])
	high_red = np.array([179, 255, 255])
	red_mask = cv2.inRange(hsv_img,low_red,high_red)
	red = cv2.bitwise_and(img,img,mask=red_mask)
	low_blue = np.array([94, 80, 2])
	high_blue = np.array([126, 255, 255])
	blue_mask = cv2.inRange(hsv_img,low_blue,high_blue)
	blue = cv2.bitwise_and(img,img,mask=blue_mask)
	low_green = np.array([25, 52, 72])
	high_green = np.array([102, 255, 255])
	green_mask = cv2.inRange(hsv_img,low_green,high_green)
	green = cv2.bitwise_and(img,img,mask=green_mask)
	winname = "Color Detector"
	cv2.namedWindow(winname)
	cv2.moveWindow(winname, 40,30)
	cv2.imshow(winname,img)
	cv2.imshow('Red', red)
	cv2.imshow('Green',green)
	cv2.imshow('Blue', blue)
	cv2.waitKey()

def videobutton():
	videofile = filedialog.askopenfilenames(initialdir='/',title='Select A File',filetypes=[("all video format", ".mp4"),("all video format", ".flv"),("all video format", ".avi")])
	video = cv2.VideoCapture(videofile)
	while True:
		successful_frame_read,frame = video.read()
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		low_red = np.array([161,155,84])
		high_red = np.array([179, 255, 255])
		red_mask = cv2.inRange(hsv_frame, low_red, high_red)
		red = cv2.bitwise_and(frame, frame, mask=red_mask)
		low_blue = np.array([94, 80, 2])
		high_blue = np.array([126, 255, 255])
		blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
		blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
		low_green = np.array([25, 52, 72])
		high_green = np.array([102, 255, 255])
		green_mask = cv2.inRange(hsv_frame, low_green, high_green)
		green = cv2.bitwise_and(frame, frame, mask=green_mask)
		cv2.imshow("Frame", frame)
		cv2.imshow("Red", red)
		cv2.imshow("Blue", blue)
		cv2.imshow("Green", green)
		key = cv2.waitKey(1)
		if key == 27:
			break

def webacambutton():
	webcam = cv2.VideoCapture(0)
	while True:
		successful_frame_read,frame = webcam.read()
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		low_red = np.array([161,155,84])
		high_red = np.array([179, 255, 255])
		red_mask = cv2.inRange(hsv_frame, low_red, high_red)
		red = cv2.bitwise_and(frame, frame, mask=red_mask)
		low_blue = np.array([94, 80, 2])
		high_blue = np.array([126, 255, 255])
		blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
		blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
		low_green = np.array([25, 52, 72])
		high_green = np.array([102, 255, 255])
		green_mask = cv2.inRange(hsv_frame, low_green, high_green)
		green = cv2.bitwise_and(frame, frame, mask=green_mask)
		cv2.imshow("Frame", frame)
		cv2.imshow("Red", red)
		cv2.imshow("Blue", blue)
		cv2.imshow("Green", green)
		key = cv2.waitKey(1)
		if key == 27:
			break  

name = Label(root,text ="CHOOSE ONE")
name.pack()
var = StringVar(root)
var.set("Image")

option = OptionMenu(root, var, "Image", "Video", "Webcam")
option.pack()

button = Button(root, text="Ok",command=open)
button.pack()

label = Label(root,text="You selected")
label.pack()

root.mainloop()