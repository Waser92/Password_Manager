import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string
import subprocess
import json
import os
from Classes import MyWindow_base
from Gestion_data_user import GestionUserData


class MyWindow_Main(MyWindow_base, GestionUserData):
    def __init__(self):
        # Appeler le constructeur de la classe parente
        super().__init__()

        # Création des composants
        self.create_widgets()
        self.liste_identifiants = []
        self.liste_mots_de_passe = []
        
        self.username = self.have_current_username()

        # Nouvelle instance de GestionUserData avec le nom d'utilisateur actuel
        self.user_data_manager = GestionUserData(self.username)

    def create_widgets(self):
        self.create_title()
        self.create_deconnection_button()
        self.create_subtitle()
        self.create_buttons()
        
    
    def create_title(self):
        label_title = tk.Label(self.frame_top, text="\nGestionnaire de Mots de passe", font=("Courrier", 40), bg='#030720', fg='white')
        label_title.pack()

    def create_deconnection_button(self):
        bouton_deconnecter = tk.Button(self.frame_top, text="Déconnecter", command=self.deconnection)
        bouton_deconnecter.pack(pady=10, ipadx=10, ipady=10)

    def create_subtitle(self):
        label_subtitle = tk.Label(self.frame_top, text="Vous pouvez maintenant enregistrer vos \n informations de connexion en toute sécurité.", font=("Courrier", 25), bg='#030720', fg='white')
        label_subtitle.pack()

    def create_buttons(self):
        # Bouton Chercher
        self.bouton_chercher = tk.Button(self.frame_bottom, text="Chercher dans mes données", command=self.open_Research_window)
        self.bouton_chercher.pack(pady=10, ipadx=20, ipady=10)

        # Bouton Ajouter
        self.bouton_ajouter = tk.Button(self.frame_bottom, text="Ajouter", command=self.ajouter_mot_de_passe)
        self.bouton_ajouter.pack(pady=10, ipadx=20, ipady=10)

    def ajouter_mot_de_passe(self):
        # Fenêtre pour saisir les informations du mot de passe
        nouvelle_fenetre = tk.Toplevel(self.frame_center)
        nouvelle_fenetre.title("Ajouter")

        # Site
        self.entry_site = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        self.entry_site.insert(0, "Site ")
        self.entry_site.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_site.grid(row=0, column=1, padx=10, pady=5)
        self.entry_site.bind("<FocusIn>", lambda event, widget=self.entry_site: self.clear_entry(event, widget))
        self.entry_site.bind("<FocusOut>", lambda event, widget=self.entry_site: self.restore_default_text(event, widget))

        # Email
        self.entry_email = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)
        self.entry_email.insert(0, "Email ")
        self.entry_email.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_email.bind("<FocusIn>", lambda event, widget=self.entry_email: self.clear_entry(event, widget))
        self.entry_email.bind("<FocusOut>", lambda event, widget=self.entry_email: self.restore_default_text(event, widget))

        # Mot de passe
        self.entry_password = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        self.entry_password.grid(row=2, column=1, padx=10, pady=5)
        self.entry_password.insert(0, "Mot de passe")
        self.entry_password.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_password.bind("<FocusIn>", lambda event, widget=self.entry_password: self.clear_entry(event, widget))
        self.entry_password.bind("<FocusOut>", lambda event, widget=self.entry_password: self.restore_default_text(event, widget))

        # Identifiant
        self.entry_identifiant = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        self.entry_identifiant.grid(row=3, column=1, padx=10, pady=5)
        self.entry_identifiant.insert(0, "Identifiant")
        self.entry_identifiant.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_identifiant.bind("<FocusIn>", lambda event, widget=self.entry_identifiant: self.clear_entry(event, widget))
        self.entry_identifiant.bind("<FocusOut>", lambda event, widget=self.entry_identifiant: self.restore_default_text(event, widget))


        bouton_valider = tk.Button(nouvelle_fenetre, text="Valider", command=lambda: self.valider_mot_de_passe(
        self.entry_site.get(), self.entry_email.get(), self.entry_identifiant.get(), self.entry_password.get(), nouvelle_fenetre))
        bouton_valider.grid(row=4, column=0, columnspan=2, pady=10)

    def deconnection(self):
        # Appel de la fonction pour supprimer les informations utilisateur
        self.delete_current_user_data()

        # Ouverture de la fenêtre d'entrée
        self.open_Entry_window()

    def delete_current_user_data(self):
        try:
            with open('current_user.json', 'w') as file:
                file.truncate(0)  # Efface tout le contenu du fichier
        except Exception as e:
            messagebox.showinfo("Erreur de suppression", f"Une erreur s'est produite lors de la suppression : {str(e)}")

    def open_Research_window(self):
            script_path = os.path.join("Source", "Research_window.py")
            subprocess.Popen(["python", script_path])

    def have_current_username(self):
        try:
            with open('current_user.json', 'r') as file:
                user_data = json.load(file)
                current_username = user_data.get("username")
            return current_username
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return None

    def valider_mot_de_passe(self, site, email, identifiant, mot_de_passe, fenetre):
        if site and identifiant and mot_de_passe:
            # ...
            # Enregistrez les données dans le fichier JSON utilisateur spécifique
            data_to_save = {
                'entry_site': site,
                'entry_email': email,
                'entry_identifiant': identifiant,
                'entry_password': mot_de_passe
            }
            self.user_data_manager.save_user_data(data_to_save)
            fenetre.destroy()

            messagebox.showinfo("Succès", "Mot de passe ajouté avec succès.")
        else:
            messagebox.showinfo("Attention", "Veuillez remplir tous les champs obligatoires.")

    
    def clear_entry(self, event, widget):
        initial_text = widget.get()

        if initial_text == "Site " or initial_text == "Email " or initial_text == "Identifiant" or initial_text == "Mot de passe":
            widget.delete(0, tk.END)
            widget.config(fg='black')  # Changer la couleur du texte en noir

    def restore_default_text(self, event, widget):
        if not widget.get():
            initial_text = "Site " if widget == self.entry_site else "Email " if widget == self.entry_email else "Identifiant" if widget == self.entry_identifiant else "Mot de passe"
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair

# Display
app = MyWindow_Main()
app.window.mainloop()