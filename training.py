import fight as ft
from oct2py import octave


#$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"
octave = octave.Oct2Py()
for x in range(10):
    octave.mutate(2, 0.1)
    X, y = ft.fight()
    octave.back_prop(1, X, y, 1)
    # set dataset 2 to what it was before


