import os
import tkinter as tk
from tkinter import ttk
from collections import deque
import pygame

#inizializza pygame per suonare suoni
pygame.mixer.init()

class Timer(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.controller = controller
        pomodoro_time = controller.pomodoro.get()
        #imposta il tempo di default del pomodoro
        self.current_time = tk.StringVar(value=f"{pomodoro_time}")
        
        self.current_timer_label = tk.StringVar(value=self.controller.timer_schedule[0])
        self.timer_running = False
        self.timer_decrement_job = None

        timer_description = ttk.Label(
            self,
            textvariable=self.current_timer_label
        )

        timer_description.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10, 0))

        settings_button = ttk.Button(
            self,
            text="Settings",
            command=show_settings,
            style="PomodoroButton.TButton",
            cursor="hand2"
        )
        settings_button.grid(row=0, column=1, sticky="E", padx=10, pady=(10, 0))

        timer_frame = ttk.Frame(self, height="100", style="Timer.TFrame")
        timer_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")

        timer_counter = ttk.Label(
            timer_frame,
            textvariable=self.current_time,
            style="TimerText.TLabel"
        )

        #posiziona il timer al centro del frame 
        timer_counter.place(relx=0.5, rely=0.5, anchor="center")

        button_container = ttk.Frame(self, padding=10, style="Background.TFrame")
        button_container.grid(row=2, column=0, columnspan=2, sticky="EW")
        button_container.columnconfigure((0, 1, 2), weight=1)

        self.start_button = ttk.Button(
            button_container,
            text="Start",
            command=self.start_timer,
            cursor="hand2",
            style="PomodoroButton.TButton"
        )

        self.start_button.grid(row=0, column=0, sticky="EW")

        self.stop_button = ttk.Button(
            button_container,
            text="Stop",
            command=self.stop_timer,
            cursor="arrow",
            state="disabled",
            style="PomodoroButton.TButton"
        )

        self.stop_button.grid(row=0, column=1, sticky="EW", padx=(5, 0))

        reset_button = ttk.Button(
            button_container,
            text="Reset",
            command=self.reset_timer,
            cursor="hand2",
            style="PomodoroButton.TButton"
        )

        reset_button.grid(row=0, column=2, sticky="EW", padx=(5, 0))

        self.decrement_time()

    def decrement_time(self):
        # Ottieni il percorso della cartella corrente del file
        current_directory = os.path.dirname(__file__)

        # Salire di una cartella
        parent_directory = os.path.dirname(current_directory)

        # Aggiungere il percorso del file audio
        path_alarm = os.path.join(parent_directory, 'assets/loud_alarm_sound.mp3')

        # Ottieni l'attuale tempo in stringa
        current_time = self.current_time.get()
        
        #converti current_time in stringa e modifica il . in :
        current_time = current_time.replace(".", ":")

        # Verifica se il timer è in esecuzione e non è a 00:00
        if self.timer_running and current_time != "00:00":
            pygame.mixer.music.stop()

            # Converti il tempo in float (in minuti) e calcola i secondi
            minutes, seconds = map(int, current_time.split(":"))
            total_seconds = minutes * 60 + seconds  # Converti tutto in secondi

            # Sottrai un secondo
            total_seconds -= 1

            # Se il tempo è ancora valido, converti di nuovo in MM:SS
            if total_seconds >= 0:
                minutes = total_seconds // 60  # Ottieni i minuti
                seconds = total_seconds % 60   # Ottieni i secondi

                # Imposta il nuovo tempo formattato come MM:SS
                self.current_time.set(f"{minutes:02d}:{seconds:02d}")

                # Aggiorna il timer ogni secondo
                self.timer_decrement_job = self.after(1000, self.decrement_time)

        elif self.timer_running and current_time == "00:00":
            # Suona l'allarme alla fine del timer
            pygame.mixer.music.load(path_alarm)
            pygame.mixer.music.play()

            # Ruota la coda per il prossimo timer
            self.timer_schedule.rotate(-1)
            next_up = self.timer_schedule[0]

            # Aggiorna l'etichetta del timer corrente
            self.current_timer_label.set(next_up)

            # Reimposta il tempo in base al prossimo timer
            if next_up == "Pomodoro":
                self.current_time.set(f"{self.controller.pomodoro.get()}")
            elif next_up == "Short Break":
                self.current_time.set(f"{self.controller.short_break.get()}")
            elif next_up == "Long Break":
                self.current_time.set(f"{self.controller.long_break.get()}")

            # Ricomincia il decremento ogni secondo
            self.timer_decrement_job = self.after(1000, self.decrement_time)


    def start_timer(self):
        self.timer_running = True
        #disabilita il bottone start
        self.start_button["state"] = "disabled"
        self.start_button["cursor"] = "arrow"
        #abilita il bottone stop
        self.stop_button["state"] = "enabled"
        self.stop_button["cursor"] = "hand2"
        self.decrement_time()

    def stop_timer(self):
        self.timer_running = False
        #disabilita il bottone stop
        self.stop_button["state"] = "disabled"
        self.stop_button["cursor"] = "arrow"
        #abilita il bottone start
        self.start_button["state"] = "enabled"
        self.start_button["cursor"] = "hand2"

        if self.timer_decrement_job:
            #ferma il timer
            self.after_cancel(self.timer_decrement_job)
            self.timer_decrement_job = None

    def reset_timer(self):
        self.stop_timer()
        pomodoro_time = self.controller.pomodoro.get()
        #ripristina il timer con il tempo di default del pomodoro e vai al primo timer della coda
        self.timer_schedule = deque(self.controller.timer_order)
        self.current_timer_label.set(self.controller.timer_schedule[0])
        self.current_time.set(f"{pomodoro_time}")
