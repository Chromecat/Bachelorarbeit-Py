from pydub import AudioSegment
from scipy.io.wavfile import read
from scipy import signal
import numpy as np

inputaudio = read("audio.wav")

audio = np.array(a[1], dtype=float)

f, t, Sxx = signal.spectrogram(audio)

matrix = np.zeros(t, f) #vgl Sxx[f,t]

maxwert = np.zeros(t)

for n in range(0, t):

    a = 0

    for m in range(0, f):
        if Sxx[m, n] < a:
            Sxx[m, n] = a




for i in range(0, t):
    for j in range(0, f):
        Sxx[j, i] = matrix[i, j]

