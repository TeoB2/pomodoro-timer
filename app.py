import os
import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import MyTimer, Settings
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
        except Exception as e:
            print(f"Error loading icon: {e}")

        try:
            icon_path = os.path.join(os.path.dirname(__file__), "assets/icon.icon")
            self.iconbitmap(icon_path)
            self.set_app_icon(icon_path)
        except Exception as e:
            print(f"Error loading icon: {e}")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=DEFAULT_VALUE_POMODORO_TIMER_STR)
        self.short_break = tk.StringVar(value=DEFAULT_VALUE_SHORT_BREAK_TIMER_STR)
        self.long_break = tk.StringVar(value=DEFAULT_VALUE_LONG_BREAK_TIMER_STR)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}

        timer_frame = MyTimer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NESW")
        settings_frame = Settings(container, self, lambda: self.show_frame(MyTimer))
        settings_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[MyTimer] = timer_frame
        self.frames[Settings] = settings_frame

        self.show_frame(MyTimer)

    def show_frame(self, container):
        if container == Settings:
            self.frames[MyTimer].stop_timer()

        if container == MyTimer:
            self.frames[MyTimer].reset_timer()

        frame = self.frames[container]
        frame.tkraise()

    def set_app_icon(self, icon_path):
        if not os.path.isfile(icon_path):
            return False

        hwnd = ctypes.windll.user32.GetForegroundWindow()
        hicon = ctypes.windll.user32.LoadImageW(0, icon_path, 1, 32, 32, 0x00000010)
        ctypes.windll.user32.SendMessageW(hwnd, 0x80, 1, hicon)

app = PomodoroTimer()
app.mainloop()