# gui

import tkinter as tk
import tkinter.font
from tkinter import ttk, messagebox
from thermalfunctions import ThermalFunctions

## constants

winsize = "600x500"
loginwinsize = "300x250"
TITLE_FONT =( "Arial", 25)
LABEL_FONT = ("Arial", 14)

class BaseApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SnakeSnap v0.1-dev")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.shared_data = {
            "username" : tk.StringVar(),
            "password" : tk.StringVar(),
            "message" : tk.StringVar(),
            "picture_user_name": tk.StringVar(),
            "current_image_name": tk.StringVar(),
            "picture_user_email": tk.StringVar(),
        }

        self.frames = {}
        self.geometry(winsize)
        self.configure(background="white")
        self.gmail = None
        self.password = None
        for f in (LoginPage, MainPage):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        # tk labels for stuff with entry points
        mainlabel = tk.Label(self, text="Welcome, please login with a gmail account below",
                         font=TITLE_FONT)
        email = tk.Label(self, text="gmail username", font=LABEL_FONT)
        password = tk.Label(self, text="gmail password", font=LABEL_FONT)
        email_entry = tk.Entry(self, textvariable=self.controller.shared_data["username"])
        password_entry = tk.Entry(self, show="*", textvariable=self.controller.shared_data["password"])

        # tk buttons with callbacks

        login_button = ttk.Button(self, text="Login to snakesnap",
                            command=self.login_command)
        quit_button = ttk.Button(self, text="Quit", command=self.quit)

        # positioning labels and entry points.

        mainlabel.grid(row=0, columnspan=3, padx = 10, pady=10)
        email.grid(row=1, columnspan=2,padx=0, pady=10)
        email_entry.grid(row=1, column=2, columnspan=2, padx=0, pady=10)
        password.grid(row=2, columnspan=2, padx=10, pady=10)
        password_entry.grid(row=2, column=2, columnspan=2, padx=0, pady=10)
        login_button.grid(row=3, column=1)
        quit_button.grid(row=4, column=1)

    def login_command(self):
        """set the variables, then show the main page
        """
        #print(self.controller.shared_data["username"].get())
        #print(self.controller.shared_data["password"].get())
        self.controller.show_frame(MainPage)


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        main_label = tk.Label(self, text="Welcome!", font=TITLE_FONT)
        main_label.grid(row=0,columnspan=3, pady=10,padx=10)
        logout_button = ttk.Button(self, text="Logout",
                            command= self.logout)#lambda: controller.show_frame(LoginPage))
        logout_button.grid(row=1)
        thermal = ThermalFunctions(parent, controller)

    def logout(self):
        # not working
        pass
        #self.controller.email_entry.delete(0,END)
        self.controller.show_frame(LoginPage)
        #LoginPage.password_entry.delete(0,END)
