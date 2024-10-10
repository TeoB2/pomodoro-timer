# Pomodoro timer
Software for a Pomodoro Timer 🍅

The Pomodoro Timer is a tool used to apply the Pomodoro Technique, which divides work into customizable intervals, typically 25 minutes, followed by short breaks. In this software, you can adjust the length of both work intervals and breaks, tailoring the duration to your needs, instead of following only the standard times. This helps improve focus and time management in a flexible way.


For execute code install all pip dependences:
```
pip install pygame
```
```
pip install pillow
```

For create a .exe file
```
pip install pyinstaller
```
```
pyinstaller .\app.py --clean --add-data="assets;assets" --add-data="frames;frames" --onefile --windowed --name pomodoro-timer --icon=assets/icon.ico   
```

See the .exe file in folder into dist/pomodoro-timer.exe

You can download file .exe from git, if when you open the .exe file Windows Defender reveals an unsafe program is because the code is not encrypted as it is the same code present in the repository. Please continue as the code is not malicious 😊
