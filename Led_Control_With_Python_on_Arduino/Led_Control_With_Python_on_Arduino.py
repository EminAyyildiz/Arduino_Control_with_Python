import sys
import tkinter as tk
import serial

ser = serial.Serial('/dev/cu.usbserial-10', 9600)

def toggle_led():
    if led_state1.get() == 1:
        ser.write(b'1')
        status_label1.config(text="LED1 ON", bg="green", fg="white")

    else:
        ser.write(b'2')
        status_label1.config(text="LED1 OFF", bg="red", fg="white")

def toggle_led2():
    if led_state2.get() == 1:
        ser.write(b'3')
        status_label2.config(text="LED2 ON", bg="green", fg="white")
    else:
        ser.write(b'4')
        status_label2.config(text="LED2 OFF", bg="red", fg="white")
def toggle_led3():
    if led_state3.get() == 1:
        ser.write(b'5')
        status_label3.config(text="LED3 ON", bg="green", fg="white")
    else:
        ser.write(b'6')
        status_label3.config(text="LED3 OFF", bg="red", fg="white")

def exit_app():
    sys.exit()

root = tk.Tk()
root.title("LED CONTROL")

led_state1 = tk.IntVar(value=0)
led_state2 = tk.IntVar(value=0)
led_state3 = tk.IntVar(value=0)

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

led_label1 = tk.Label(frame_top, text="LED1", font=("times new roman", 15, "bold"))
led_label1.pack(side=tk.LEFT, padx=10)

button_on1 = tk.Radiobutton(frame_top, text="ON", variable=led_state1, value=1, command=toggle_led)
button_on1.pack(side=tk.LEFT, padx=10)

button_off1 = tk.Radiobutton(frame_top, text="OFF", variable=led_state1, value=0, command=toggle_led)
button_off1.pack(side=tk.LEFT, padx=10)

frame_middle = tk.Frame(root)
frame_middle.pack(pady=10)

led_label2 = tk.Label(frame_middle, text="LED2", font=("times new roman", 15, "bold"))
led_label2.pack(side=tk.LEFT, padx=10)

button_on2 = tk.Radiobutton(frame_middle, text="ON", variable=led_state2, value=1, command=toggle_led2)
button_on2.pack(side=tk.LEFT, padx=10)

button_off2 = tk.Radiobutton(frame_middle, text="OFF", variable=led_state2, value=0, command=toggle_led2)
button_off2.pack(side=tk.LEFT, padx=10)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

led_label3 = tk.Label(frame_bottom, text="LED3", font=("times new roman", 15, "bold"))
led_label3.pack(side=tk.LEFT, padx=10)

button_on3 = tk.Radiobutton(frame_bottom, text="ON", variable=led_state3, value=1, command=toggle_led3)
button_on3.pack(side=tk.LEFT, padx=10)

button_off3 = tk.Radiobutton(frame_bottom, text="OFF", variable=led_state3, value=0, command=toggle_led3)
button_off3.pack(side=tk.LEFT, padx=10)

status_label1 = tk.Label(root, text="LED1 OFF", font=("times new roman", 24, "bold"), width=10, relief=tk.RAISED, background="red")
status_label1.pack(pady=15)

status_label2 = tk.Label(root, text="LED2 OFF", font=("times new roman", 24, "bold"), width=10, relief=tk.RAISED, background="red")
status_label2.pack(pady=15)

status_label3 = tk.Label(root, text="LED3 OFF", font=("times new roman", 24, "bold"), width=10, relief=tk.RAISED, background="red")
status_label3.pack(pady=15)

exit_button = tk.Button(root, text="EXIT", command=exit_app, width=15, height=2)
exit_button.pack(pady=10)


root.mainloop()

ser.close()