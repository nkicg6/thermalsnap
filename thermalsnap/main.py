#! /usr/bin/python3
# main tkinter app
from gui import BaseApp
# super helpful https://stackoverflow.com/questions/33646605/how-to-access-variables-from-different-classes-in-tkinter

if __name__ == '__main__':
    #root = tk.Tk()
    #root.geometry('600x500')
    #snakesnap = BaseApp(root, winsize, loginwinsize)
    snakesnap = BaseApp()
    snakesnap.mainloop()
