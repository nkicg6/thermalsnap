#! /usr/bin/python3
# main tkinter app

import tkinter as tk
import tkinter.font
from tkinter import ttk, messagebox


class BaseApp:

    def __init__(self, master, winsize, loginwinsize):
        self.master = master
        self.master.title("SnakeSnap v0.1-dev")
        self.master.geometry(winsize)
        self.master.configure(background = "white")
        #self.startLoginWindow = LoginWindow(self)
        self.initialize(master)
        self.gmail = None
        self.password = None


    def initialize(self, master):
        LOGIN_MESSAGE = "Login with a gmail account below\n to send email or continue as a guest"
        self.label = tk.Label(master, text="Welcome to SnakeSnap!", bg = "white",
                              fg = "firebrick3", font = ("arial", 30, "bold"), anchor = "center").grid(row=1, column=1)
        self.message = tk.Label(master,
                                text= LOGIN_MESSAGE, bg = "white",
                                font = ("arial", 18, "bold")).grid(row=2, column=1)
        self.emailLabel = tk.Label(master, text = "Email", bg = "white", fg = "black", font = ("arial", 20, "bold")).grid(row=3)
        self.emailLabel = tk.Label(master, text = "password", bg = "white", fg = "black", font = ("arial", 20, "bold")).grid(row=4)
        self.email = tk.Entry(master).grid(row=3, column=1)
        self.password = tk.Entry(master).grid(row=4, column=1)
        self.close_button = tk.Button(master, text="Quit",
                                      command=master.quit).grid(row=5, column=1)
        self.login_button = tk.Button(master, text="Login").grid(row=5)

    def greet(self):
        print("Greetings")



class LoginWindow(BaseApp):

    def __init__(self,master, winsize, loginwinsize):
        BaseApp.__init__(self, master, winsize, loginwinsize)
        self.root_login = tk.Toplevel()
        self.master.withdraw()
        self.root_login.configure(background='grey92')
        self.root_login.resizable(width=False, height=False)
        self.root_login.title('Login')
        self.root_login.bind_all("<Mod2-q>", self.master.quit)
        self.log_btnFont = tkinter.font.Font(family="Lucida Grande", size=10)
        self.log_btnTxtColor = "grey22"
        self.log_btnTxtColor_active = "white"
        self.email = tk.Entry(master).grid(row=3, column=1)
        self.password = tk.Entry(master).grid(row=4, column=1)
        self.close_button = tk.Button(master, text="Quit",
                                      command=master.quit).grid(row=5, column=1)
        self.login_button = tk.Button(master, text="Login").grid(row=5)



## constants
winsize = "600x500"
loginwinsize = "300x250"

if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry('600x500')
    #snakesnap = BaseApp(root, winsize, loginwinsize)
    snakesnap = LoginWindow(root, winsize, loginwinsize)
    root.mainloop()
