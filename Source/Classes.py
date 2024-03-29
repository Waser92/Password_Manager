from tkinter import *
from tkinter import ttk
import subprocess
import os

class MyWindow_base:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberShield")
        self.window.geometry("800x480")
        self.window.minsize(800, 360)
        self.window.iconbitmap("")
        self.window.config(background='#030720')
        self.nom_utilisateur_var = StringVar()
        self.mot_de_passe_var = StringVar()

        # Initialisation of components
        self.frame_top = Frame(self.window, bg='#030720')
        self.frame_center = Frame(self.window, bg='#030720')
        self.frame_bottom = Frame(self.window, bg='#030720')

        # Packaging
        self.frame_top.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_center.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)
        
    def open_Create_account(self):
        script_path = os.path.join("Source", "Create_account_window.py")
        subprocess.Popen(["python", script_path])
        self.window.destroy()

    def open_Connection_window(self):
        script_path = os.path.join("Source", "Connection_window.py")
        subprocess.Popen(["python", script_path])
        self.window.destroy()
        
    def open_Main_window(self):
        script_path = os.path.join("Source", "Main_window.py")
        subprocess.Popen(["python", script_path])
        self.window.destroy()
        
    def open_Entry_window(self):
        script_path = os.path.join("Source", "Entry_window.py")
        subprocess.Popen(["python", script_path])
        self.window.destroy()
    
    