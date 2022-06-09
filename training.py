import fight as ft


#$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"

for x in range(5):
    ft.fight(1, 2, mode="Training", engine_choices=[x] * 10)


