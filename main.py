from pydub import AudioSegment
from scipy.io.wavfile import read
from scipy import signal
import numpy as np

inputaudio = read("audio.wav")

audio = np.array(inputaudio[1], dtype=float) # a in inputaudio wechseln

f, t, Sxx = signal.spectrogram(audio)

#matrix = np.zeros(t, f)  # vgl Sxx[f,t]
#matrix = np.ndarray((129, 122), np.zeros())
matrix = np.ndarray(shape=(t.size, f.size),  dtype=float, order='F')



"""maxwert = np.zeros(t)  # fuer jeden t wert wird ein maxwert gespeichert

for n1 in range(0, t):  #schleife um maxwert zu bestimmen

    a = 0

    for m1 in range(0, f):
        if Sxx[m1, n1] > a:
            a = Sxx[m1, n1]

    print (a)


for n2 in range(0, t):  #uebertrag matrix mit division des maxwert (wertebereich 0-1)
    for m2 in range(0, f):
        x1 = matrix[n2, m2]
        x2 = maxwert[m2]
        Sxx[m2, n2] = x1/x2


for n3 in range(0, t): #bestimmung des H lautes
    for m3 in range(0, f):  #analog array bauen zum vergleich


for n3 in range(0, t):  # bestimmung des S lautes
    for m3 in range(0, f):


for n3 in range(0, t):  # bestimmung des D lautes
    for m3 in range(0, f):
"""