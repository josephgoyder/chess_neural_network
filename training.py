import fight as ft
from oct2py import octave
import shutil


#$env:path += ";C:\Users\076-jgoyder\AppData\Local\Programs\GNU Octave\Octave-7.1.0\mingw64\bin"
octave = octave.Oct2Py()
for x in range(10):
    octave.mutate(2, 1)
    X, y = ft.fight()
    octave.back_prop(1, X, y, 1)
    shutil.copyfile('/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_1.mat', '/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_2.mat')
    # set dataset 2 to dataset 1


