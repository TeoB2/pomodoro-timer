import tkinter as tk
from tkinter import ttk
from typing import Final

COLOUR_PRIMARY: Final = "#007367"
COLOUR_PRIMARY_HOVER: Final = "#004039"
COLOUR_SECONDARY: Final = "#0A122A"
COLOUR_LIGHT_BACKGROUND: Final = "#f3f8fa"
COLOUR_LIGHT_TEXT: Final = "#A5FFD6"
COLOUR_DARK_TEXT: Final = "#0A122A"

def get_global_style(self):
    style = ttk.Style(self)
    style.theme_use("clam")

    style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
    style.configure("Background.TFrame", background=COLOUR_LIGHT_BACKGROUND)
    style.configure(
        "TimerText.TLabel",
        background=COLOUR_LIGHT_BACKGROUND,
        foreground=COLOUR_DARK_TEXT,
        font="Courier 38"
    )
    style.configure(
        "LightText.TLabel",
        background=COLOUR_PRIMARY,
        foreground=COLOUR_LIGHT_TEXT
    )
    style.configure(
        "PomodoroButton.TButton",
        background=COLOUR_PRIMARY,
        foreground="white",
        borderwidth=2,
        relief="flat"
    )

    style.map(
        "PomodoroButton.TButton",
        background=[("active", COLOUR_PRIMARY_HOVER), ("disabled", COLOUR_LIGHT_TEXT)]
    )

    self["background"] = COLOUR_PRIMARY