import tkinter as tk
from tkinter import messagebox, END
import serial
import time

port = '/dev/cu.usbserial-10' # Arduino'nun bağlı olduğu portu doğru şekilde belirtin
baudrate = 9600

ser = serial.Serial(port, baudrate)

kapasite = 5
giris_kapi_acik = False
cikis_kapi_acik = False

def komut_gonder(komut):
    ser.write(komut.encode())

def giris_kapi_ac():
    global giris_kapi_acik
    if not giris_kapi_acik:
        giris_kapi_acik = True
        komut_gonder("GIRIS_AC")
        giris_ac_button.config(state=tk.DISABLED)
        giris_kapat_button.config(state=tk.DISABLED)
        root.after(3000, enable_giris_buttons)

def giris_kapi_kapat():
    global giris_kapi_acik
    if giris_kapi_acik:
        giris_kapi_acik = False
        komut_gonder(f"GIRIS_KAPAT {giris_servo_pin}")
        giris_ac_button.config(state=tk.DISABLED)
        giris_kapat_button.config(state=tk.DISABLED)
        root.after(3000, enable_giris_buttons)

def cikis_kapi_ac():
    global cikis_kapi_acik
    if not cikis_kapi_acik:
        cikis_kapi_acik = True
        komut_gonder(f"CIKIS_AC {cikis_servo_pin}")
        cikis_ac_button.config(state=tk.DISABLED)
        cikis_kapat_button.config(state=tk.DISABLED)
        root.after(3000, enable_cikis_buttons)

def cikis_kapi_kapat():
    global cikis_kapi_acik
    if cikis_kapi_acik:
        cikis_kapi_acik = False
        komut_gonder(f"CIKIS_KAPAT {cikis_servo_pin}")
        cikis_ac_button.config(state=tk.DISABLED)
        cikis_kapat_button.config(state=tk.DISABLED)
        root.after(3000, enable_cikis_buttons)

def enable_giris_buttons():
    giris_ac_button.config(state=tk.NORMAL)
    giris_kapat_button.config(state=tk.NORMAL)

def enable_cikis_buttons():
    cikis_ac_button.config(state=tk.NORMAL)
    cikis_kapat_button.config(state=tk.NORMAL)

def kapasite_guncelle():
    kapasite_label.config(text=f"Kapasite: {kapasite}")

def arac_giris():
    global kapasite
    if kapasite > 0:
        kapasite -= 1
        kapasite_guncelle()
        giris_kapi_ac()
    else:
        messagebox.showwarning("Warning", "İçeride Alan Kalmadı!")

def arac_cikis():
    global kapasite
    if kapasite < 15:
        kapasite += 1
        kapasite_guncelle()
        cikis_kapi_ac()
    else:
        messagebox.showwarning("Warning", "İçeride Araç Kalmadı!")

root = tk.Tk()
root.title("Otopark Sistemi")

giris_servo_pin = 9
cikis_servo_pin = 10

giris_frame = tk.Frame(root, pady=20)
giris_frame.pack()

giris_label = tk.Label(giris_frame, text="Giriş Kapısı")
giris_label.pack()

giris_button_frame = tk.Frame(giris_frame)
giris_button_frame.pack(pady=10)

giris_ac_button = tk.Button(giris_button_frame, text="Aç", command=arac_giris)
giris_ac_button.pack(side=tk.LEFT, padx=10)

giris_kapat_button = tk.Button(giris_button_frame, text="Kapat", command=giris_kapi_kapat)
giris_kapat_button.pack(side=tk.LEFT, padx=10)

cikis_frame = tk.Frame(root, pady=20)
cikis_frame.pack()

cikis_label = tk.Label(cikis_frame, text="Çıkış Kapısı")
cikis_label.pack()

cikis_button_frame = tk.Frame(cikis_frame)
cikis_button_frame.pack(pady=10)

cikis_ac_button = tk.Button(cikis_button_frame, text="Aç", command=arac_cikis)
cikis_ac_button.pack(side=tk.LEFT, padx=10)

cikis_kapat_button = tk.Button(cikis_button_frame, text="Kapat", command=cikis_kapi_kapat)
cikis_kapat_button.pack(side=tk.LEFT, padx=10)

kapasite_label = tk.Label(root, text=f"Kapasite: {kapasite}")
kapasite_label.pack(pady=10)

root.mainloop()
