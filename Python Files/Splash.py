from tkinter import *
import tkinter.font as font

class SplashScreen(Frame):

    intro_lbl = strt_btn = splash_canvas = None
    path_to_bg_image = "..\Images\minimalist-clean-wavy-white-background-design_6689-121.png"
    welcome_text = "Welcome to your ERA"

    root = None # This is a reference to your main GUI window


    def __init__(self, **kwargs):

        self.root = kwargs['master']
        super().__init__(**kwargs)

        titleFont = font.Font(family="Times New Roman", size=50, weight="bold")
        loginFont = font.Font(family="Times New Roman", size=30, weight="bold")
        
        # Background Image of the App
        self.root.bgimg = bgimg = PhotoImage(file=self.path_to_bg_image)

        # Canvas for splash_screen frame
        self.splash_canvas = Canvas(self, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.splash_canvas.pack(fill=BOTH, expand=True)
        self.splash_canvas.create_image(0, 0, image=bgimg, anchor=NW)

        self.intro_lbl = Label(self.splash_canvas, text=self.welcome_text, font=titleFont, fg="#F6D000", bg="white")
        self.intro_lbl.place(relx=0.5, rely=0.405, anchor=CENTER)

        self.strt_btn = Button(self.splash_canvas, text="Start", command=self.start, font=loginFont, fg="#F6D000", bg="white", bd=0, highlightthickness=0)
        self.strt_btn.configure(activebackground="white", activeforeground="#F6D000")
        self.strt_btn.place(relx=0.5, rely=0.55, anchor=CENTER)


    def start(self):
        # Go to next screen - Login
        print("Starting app...")
        self.root.event_generate("<<StartERA>>")


        
