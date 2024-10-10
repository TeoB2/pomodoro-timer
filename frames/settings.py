import tkinter as tk
from tkinter import ttk

class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        # Configurazione delle righe e colonne
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        # Container per le impostazioni
        settings_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )
        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        # Etichetta e campo di input per Pomodoro
        self.create_label_input(
            settings_container,
            label_text="Pomodoro: ",
            variable=controller.pomodoro,
            row=0,
            min_value=0,
            max_value=7200,  # 7200 secondi = 120 minuti
        )

        # Etichetta e campo di input per Long Break
        self.create_label_input(
            settings_container,
            label_text="Long Break: ",
            variable=controller.long_break,
            row=1,
            min_value=1,
            max_value=60,
        )

        # Etichetta e campo di input per Short Break
        self.create_label_input(
            settings_container,
            label_text="Short Break: ",
            variable=controller.short_break,
            row=2,
            min_value=1,
            max_value=30,
        )

        # Aggiungi padding a tutti i widget nel container delle impostazioni
        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Contenitore per i pulsanti
        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        # Pulsante per tornare al timer
        timer_button = ttk.Button(
            button_container,
            text="← Back",
            command=show_timer,
            style="PomodoroButton.TButton",
            cursor="hand2"
        )
        timer_button.grid(column=0, row=0, sticky="EW", padx=2)

    def create_label_input(self, container, label_text, variable, row, min_value, max_value):
        """
        Funzione per creare un'etichetta e uno Spinbox in modo ripetitivo.
        """
        # Creazione dell'etichetta
        label = ttk.Label(
            container,
            text=label_text,
            style="LightText.TLabel"
        )
        label.grid(row=row, column=0, sticky="W")

        # Creazione dello Spinbox
        spinbox = ttk.Spinbox(
            container,
            from_=min_value,
            to=max_value,
            increment=1,
            justify="center",
            textvariable=variable,
            width=10
        )
        spinbox.grid(row=row, column=1, sticky="EW")
        spinbox.focus()  # Imposta il focus sul primo Spinbox
