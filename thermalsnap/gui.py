# gui
import os
import Tkinter as tk
import ttk
#from Tkinter import ttk # had to change for python2 crap with opencv
import thermalfunctions

## constants

winsize = "900x500+0+0"
loginwinsize = "900x500+0+0"
TITLE_FONT =("Arial", 25)
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
            "home_dir" : self.make_dir_structure(),
            "password" : tk.StringVar(),
            "message" : tk.StringVar(),
            # current picture user
            "picture_user_name": tk.StringVar(),
            # current image name
            "current_image_name": None,
            # current user email address
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

    def make_dir_structure(self):
        """makes the dir structure
        """
        top_level_dir = os.path.join(os.path.expanduser("~"),
                                     "Desktop", "snakesnap-photos")
        if not os.path.isdir(top_level_dir):
            print("making dir {} structure for images".format(top_level_dir))
            os.makedirs(top_level_dir)
            return top_level_dir
        else:
            print("home directory {} exists.".format(top_level_dir))
            return top_level_dir


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
        email.grid(row=1, column=0,padx=0, pady=10)
        email_entry.grid(row=1, column=1, columnspan=2, padx=0, pady=10)
        password.grid(row=2,column=0, padx=10, pady=10)
        password_entry.grid(row=2, column=1, columnspan=2, padx=0, pady=10)
        login_button.grid(row=3, column=1)
        quit_button.grid(row=4, column=1)

    def login_command(self):
        """set the variables, then show the main page
        """
        #print(self.controller.shared_data["username"].get())
        #print(self.controller.shared_data["password"].get())
        self.controller.show_frame(MainPage)

    def logout(self):
        # not working
        pass
        #self.controller.email_entry.delete(0,END)
        #self.controller.show_frame(LoginPage)
        #LoginPage.password_entry.delete(0,END)


class MainPage(LoginPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.login = LoginPage
        self.thermal = thermalfunctions.ThermalFunctions(parent, controller)

        # buttons and forms

        main_label = tk.Label(self, text="Welcome!", font=TITLE_FONT)
        main_label.grid(row=0, column=2,columnspan=3, pady=10,padx=10)
        logout_button = ttk.Button(self, text="Logout",
                            command= lambda: controller.show_frame(LoginPage))


        user_email_label = tk.Label(self, text="Email address", font=LABEL_FONT)
        user_name_label = tk.Label(self, text="Name", font=LABEL_FONT)
        user_email = tk.Entry(self, textvariable=self.controller.shared_data["picture_user_email"])
        user_name = tk.Entry(self, textvariable=self.controller.shared_data["picture_user_name"])
        start_thermal = ttk.Button(self, text="Snakevision", command = self.thermal.start_thermal)
        stop_thermal = ttk.Button(self, text="Stop snakevision", command = self.thermal.stop_thermal)
        snap_thermal = ttk.Button(self, text="Take picture", command = self.thermal.take_picture)
        email_previous_picture = ttk.Button(self, text="email picture", command = self.thermal.email_picture)

        # button and form positioning
        logout_button.grid(row=5, column=1)
        user_name_label.grid(row=1, column=1, columnspan=1, padx=10,pady=10)
        user_name.grid(row=1, column=2, columnspan=2, padx=10,pady=10)
        user_email_label.grid(row=2, column=1, columnspan=1, padx=10,pady=10)
        user_email.grid(row=2, column=2, columnspan=2, padx=10,pady=10)
        start_thermal.grid(row=3, column=1, columnspan=1, padx=10,pady=10)
        stop_thermal.grid(row=3, column=2, columnspan=1, padx=10,pady=10)
        snap_thermal.grid(row=3, column=3, columnspan=1, padx=10,pady=10)
        email_previous_picture.grid(row=3, column=4,columnspan=1, padx=10,pady=10)
