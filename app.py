import os
import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Timer, Settings
from assets.style import *
from assets.constants import *
from windows import set_dpi_awareness
import ctypes

set_dpi_awareness()

class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        get_global_style(self)

        self.title("Pomodoro Timer")

        try:
            path_image = os.path.join(os.path.dirname(__file__), "assets/icon.png")
            icon = tk.PhotoImage(file=path_image)
            self.iconphoto(True, icon)
        except:
            pass

        try:
            icon_path = os.path.join(os.path.dirname(__file__), "assets/icon.ico")
            self.iconbitmap(icon_path)
            self.set_app_icon(icon_path)
        except:
            pass

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=DEFAULT_VALUE_POMODORO_TIMER_STR)
        self.short_break = tk.StringVar(value=DEFAULT_VALUE_SHORT_BREAK_TIMER_STR)
        self.long_break = tk.StringVar(value=DEFAULT_VALUE_LONG_BREAK_TIMER_STR)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        #deque è una coda che permette di aggiungere e rimuovere elementi da entrambi i lati
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}

        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NESW")
        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame

        self.show_frame(Timer)

    def show_frame(self, container):
        #se è premuto settings metti in pausa il timer
        if container == Settings:
            self.frames[Timer].stop_timer()

        if container == Timer:
           self.frames[Timer].reset_timer()

        frame = self.frames[container]
        frame.tkraise()

    def set_app_icon(self, icon_path):
        #controlla che icon_path sia un file esistente
        if not os.path.isfile(icon_path):
            return False

        # Usa ctypes per cambiare l'icona della barra delle applicazioni
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        hicon = ctypes.windll.user32.LoadImageW(0, icon_path, 1, 32, 32, 0x00000010)
        ctypes.windll.user32.SendMessageW(hwnd, 0x80, 1, hicon)

app = PomodoroTimer()
app.mainloop()