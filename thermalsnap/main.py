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

        #button2 = tk.Button(self, text="Page Two",
        #                    command=lambda: controller.show_frame(PageTwo))
        #button2.pack()


    # def initialize(self, master):
    #     LOGIN_MESSAGE = "Login with a gmail account below\n to send email or continue as a guest"
    #     self.label = tk.Label(master, text="Welcome to SnakeSnap!", bg = "white",
    #                           fg = "firebrick3", font = ("arial", 30, "bold"), anchor = "center").grid(row=1, column=1)
    #     self.message = tk.Label(master,
    #                             text= LOGIN_MESSAGE, bg = "white",
    #                             font = ("arial", 18, "bold")).grid(row=2, column=1)
    #     self.emailLabel = tk.Label(master, text = "Email", bg = "white", fg = "black", font = ("arial", 20, "bold")).grid(row=3)
    #     self.emailLabel = tk.Label(master, text = "password", bg = "white", fg = "black", font = ("arial", 20, "bold")).grid(row=4)
    #     self.email = tk.Entry(master).grid(row=3, column=1)
    #     self.password = tk.Entry(master).grid(row=4, column=1)
    #     self.close_button = tk.Button(master, text="Quit",
    #                                   command=master.quit).grid(row=5, column=1)
    #     self.login_button = tk.Button(master, text="Login").grid(row=5)


# class LoginPage(tk.Frame):
#     """inherits from base app. Called to start the app.
#     login with a gmail username and password
#     """

#     def __init__(self,master, winsize, loginwinsize):
#         master = BaseApp.__init__(self, master, winsize, loginwinsize)
#         self.root_login = tk.Toplevel()
#         self.hidden = True
#         self.master.withdraw()
#         self.root_login.focus_set()
#         self.root_login.configure(background='grey92')
#         self.root_login.resizable(width=False, height=False)
#         self.root_login.geometry(loginwinsize)
#         self.root_login.title('Login')
#         self.log_btnFont = tkinter.font.Font(family="Lucida Grande", size=10)
#         self.log_btnTxtColor = "grey22"
#         self.log_btnTxtColor_active = "white"
#         self.master.email = tk.Entry(self.root_login).grid(row=3, column=1)
#         self.master.password = tk.Entry(self.root_login).grid(row=4, column=1)
#         self.close_button = tk.Button(self.root_login, text="Quit",
#                                       command=self.master.quit).grid(row=5, column=1)
#         self.login_button = tk.Button(self.root_login, text="Login").grid(row=5, column=0)

#     def login(self):
#         """accept user input, reveal main window
#         """
#         pass

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
