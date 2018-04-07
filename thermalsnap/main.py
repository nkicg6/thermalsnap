#! /usr/bin/python3
# main tkinter app

import tkinter as tk
import tkinter.font
from tkinter import ttk, messagebox


class BaseApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SnakeSnap v0.1-dev")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
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
        # tk labels for stuff with entry points
        mainlabel = tk.Label(self, text="Welcome, please login with a gmail account below",
                         font=TITLE_FONT)
        email = tk.Label(self, text="gmail username", font=LABEL_FONT)
        password = tk.Label(self, text="gmail password", font=LABEL_FONT)
        email_entry = tk.Entry(self)
        password_entry = tk.Entry(self, show="*")
        # tk buttons with callbacks
        login_button = ttk.Button(self, text="Login to snakesnap",
                            command=lambda: controller.show_frame(MainPage))

        quit_button = ttk.Button(self, text="Quit", command=self.quit)
        # positioning labels and entry points.
        mainlabel.grid(row=0, columnspan=3, padx = 10, pady=10)
        email.grid(row=1, padx=10, pady=10)
        email_entry.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        password.grid(row=2, padx=10, pady=10)
        password_entry.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
        login_button.grid(row=3, column=1)
        quit_button.grid(row=3, column=2)




class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SnakeSnap v0.1-dev", font=TITLE_FONT)
        label.pack(pady=10,padx=10)

        logout_button = ttk.Button(self, text="Logout",
                            command=lambda: controller.show_frame(LoginPage))
        logout_button.pack()

## constants
winsize = "600x500"
loginwinsize = "300x250"
TITLE_FONT =( "Arial", 25)
LABEL_FONT = ("Arial", 14)
if __name__ == '__main__':
    #root = tk.Tk()
    #root.geometry('600x500')
    #snakesnap = BaseApp(root, winsize, loginwinsize)
    snakesnap = BaseApp()
    snakesnap.mainloop()
