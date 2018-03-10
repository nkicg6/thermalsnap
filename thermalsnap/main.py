#! /usr/bin/python3
# main tkinter app

import tkinter as tk


class WelcomePage:

    def __init__(self, master):
        self.master = master
        master.title("SnakeSnap v0.1-dev")
        master.geometry("600x500")
        master.configure(background = "white")
        self.master = master
        self.initialize(master)

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


if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry('600x500')
    snakesnap = WelcomePage(root)
    root.mainloop()
