from pydub import AudioSegment
from scipy.io.wavfile import read
from scipy import signal
import numpy as np
import xlsxwriter

inputaudio = read("audio.wav")  # lesen des WAV-files

audio = np.array(inputaudio[1], dtype=float)  # inputaudio in ndarray audio transformieren

f, t, Sxx = signal.spectrogram(audio, fs=0.44)  # spektrogramm bilden

print(f*100000)
#print(t)
#print(t.shape)

#print(Sxx.shape)
#print(Sxx.dtype)

matrix = np.ndarray(shape=(t.size, f.size), dtype=float, order='F')  # ndarray erstellen matrix[t,f] vgl Sxx[f,t]

print(matrix.shape)
print(matrix.dtype)

maxwert = np.ndarray(shape=(t.size,), dtype=float)  # ndarray erstellen maxwert

#print(maxwert.shape)
#print(maxwert.dtype)

for t0 in range(0, t.size):  # erste itteration arrays mit 0 fuellen
    maxwert[t0] = 0
    for f0 in range(0, f.size):
        matrix[t0, f0] = 0

for t1 in range(0, t.size):  # zweite itteration um maxwert zu bestimmen

    a = 0

    for f1 in range(0, f.size):
        if Sxx[f1, t1] > a:
            a = Sxx[f1, t1]
    maxwert[t1] = a

#    print (a)
#    print (n1)


for t2 in range(0, t.size):  # dritte itteration mit uebertrag und normierung auf wertebereich (0-1)
    for f2 in range(0, f.size):
        x1 = Sxx[f2, t2]
        x2 = maxwert[t2]
        if x2 == 0:
            matrix[t2, f2] = 0
        else:
            matrix[t2, f2] = x1 / x2

#        print(matrix[t2, f2].round(4))


workbook = xlsxwriter.Workbook('audio.xlsx')  # in excel schreiben
worksheet = workbook.add_worksheet()
for t3 in range(0, t.size):
    for f3 in range(0, f.size):
        worksheet.write((f.size - f3), t3, matrix[t3, f3])
workbook.close()

"""
bereich bestimmung der laute 

s0 = np.ndarray(shape=(6), dtype=float) #schnittarray 1. wert anfang 2. wert stop usw.

a3 = np.ndarray(shape=(x), dtype=int)   # array erstellung 
a3[0] = 2342                            # erster wert = summe
a3[1] = 1                               # welche arrayelemente summiert werden sollen
a3[2] = 2
a3[3] = 3
a3[4] = 4
a3[5] = 5
a3[6] = 6
a3[7] = 7
a3[8] = 8
a3[9] = 9

for t3 in range(0, t.size): # bestimmung des H lautes
    for f3 in range(0, f.size):
        print("t3")
        
a4 = np.ndarray(shape=(x), dtype=int)   # array erstellung 
a4[0] = 2342                            # erster wert = summe
a4[1] = 1                               # welche arrayelemente summiert werden sollen
a4[2] = 2
a4[3] = 3
a4[4] = 4
a4[5] = 5
a4[6] = 6
a4[7] = 7
a4[8] = 8
a4[9] = 9

for t4 in range(0, t.size):  # bestimmung des S lautes
    for f4 in range(0, f.size):
        print("t4")
        
a5 = np.ndarray(shape=(x), dtype=int)   # array erstellung 
a5[0] = 2342                            # erster wert = summe
a5[1] = 1                               # welche arrayelemente summiert werden sollen
a5[2] = 2
a5[3] = 3
a5[4] = 4
a5[5] = 5
a5[6] = 6
a5[7] = 7
a5[8] = 8
a5[9] = 9

for t5 in range(0, t.size):  # bestimmung des D lautes
    for f5 in range(0, f.size):
        print("t5")
        

"""