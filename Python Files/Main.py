from tkinter import *
from Splash import *

root = Tk()
root.geometry("1000x650")
root.configure(bg="white")

def goto_next_screen(*args):
    args[1].pack_forget()
    args[2].pack()
        

splash_screen = SplashScreen(master=root, background="blue")
splash_screen.pack()

login_screen = Frame(root)
login_label = Label(login_screen, text="Logging in...")
login_label.pack()



root.bind("<<StartERA>>", lambda event, prev_screen = splash_screen, next_screen = login_screen: goto_next_screen(event, prev_screen, next_screen))

root.mainloop()
