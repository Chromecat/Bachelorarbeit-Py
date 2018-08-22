from pydub import AudioSegment
from scipy.io.wavfile import read
from scipy import signal
import numpy as np

inputaudio = read("audio.wav")

audio = np.array(inputaudio[1], dtype=float) # a in inputaudio wechseln

f, t, Sxx = signal.spectrogram(audio)

print(Sxx.shape)
print(Sxx.dtype)

matrix = np.ndarray(shape=(t.size, f.size), dtype=float, order='F')

print(matrix.shape)
print(matrix.dtype)

maxwert = np.ndarray(shape=(t.size,), dtype=float)

print(maxwert.shape)
print(maxwert.dtype)

for t0 in range(0, t.size):  # uebertrag matrix mit division des maxwert (wertebereich 0-1)
    maxwert[t0] = 0.000001
    for f0 in range(0, f.size):
        matrix[t0, f0] = 0.000001

for t1 in range(0, t.size):  # schleife um maxwert zu bestimmen

    a = 0

    for f1 in range(0, f.size):
        if Sxx[f1, t1] > a:
            a = Sxx[f1, t1]

#    print (a)
#    print (n1)


for t2 in range(0, t.size):  # uebertrag matrix mit division des maxwert (wertebereich 0-1)
    for f2 in range(0, f.size):
        x1 = Sxx[f2, t2]
        x2 = maxwert[f2]
        matrix[t2, f2] = x1/x2

        print(matrix[f2, t2].round(3))


"""
n = t 
m = f 

for n3 in range(0, t.size): # bestimmung des H lautes
    for m3 in range(0, f.size):  # analog array bauen zum vergleich
        print("n3")

for n4 in range(0, t.size):  # bestimmung des S lautes
    for m4 in range(0, f.size):
        print("n4")

for n5 in range(0, t.size):  # bestimmung des D lautes
    for m5 in range(0, f.size):
        print("n5")
        
"""
