#! /usr/bin/python3
# main tkinter app

import tkinter as tk


class WelcomePage:
    def __init__(self, master):
        self.master = master
        master.title("SnakeSnap v0.1-dev")
        master.geometry("600x500")
        master.configure(background = "white")
        self.label = tk.Label(master, text="Welcome to SnakeSnap!", bg = "white",
                              fg = "firebrick3", font = ("arial", 20, "bold"))
        self.message = tk.Label(master,
                                text="Login with a gmail account below\n to send email or continue as a guest", bg = "white", font = ("arial", 14, "bold"))
        self.label.grid(columnspan=1)
        self.message.grid(columnspan=3)
        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=2)
        self.close_button = tk.Button(master, text="Close",
                                      command=master.quit)
        self.close_button.grid(row=2, column=2)

    def greet(self):
        print("Greetings")


if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry('600x500')
    snakesnap = WelcomePage(root)
    root.mainloop()
