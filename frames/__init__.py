import os
import sys

# Ottieni la cartella corrente (dove si trova lo script app.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Aggiungi il percorso relativo \tkinter\pomodoro_timer\frames
new_directory = os.path.join(current_directory)

# Aggiungi la nuova directory al percorso di ricerca dei moduli
sys.path.append(new_directory)

try:
    from timer import Timer
    print("Modulo Timer importato con successo")
except ImportError as e:
    print(f"Errore Modulo Timer: {e}")

try:
    from settings import Settings
    print("Modulo Settings importato con successo")
except ImportError as e:
    print(f"Errore Modulo Settings: {e}")


