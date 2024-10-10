# Tentativo di importare il modulo Timer
try:
    from frames.timer import MyTimer
    print("Modulo Timer importato con successo")
except ImportError as e:
    print(f"Errore Modulo Timer: {e}")

# Tentativo di importare il modulo Settings
try:
    from frames.settings import Settings
    print("Modulo Settings importato con successo")
except ImportError as e:
    print(f"Errore Modulo Settings: {e}")
