from tkinter import Tk, Label, Button
import tkinter as tk
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130)
#initializing tkinter window
root=tk.Tk()
def onbutton_click():
    te_xt=text_box.get(1.0,'end-1c')
    print(te_xt)
    engine.say(te_xt)
    engine.runAndWait()
#set title
root.title("Text to Speech")
root.geometry("1000x2000")
text_box = tk.Text(root)
text_box.pack()
tk.Button(root,text="Speak",command = onbutton_click,width=10,height=3).pack()
tk.Button(root,text="Quit",command=root.quit,width=6,height=3).pack()


root.mainloop()
