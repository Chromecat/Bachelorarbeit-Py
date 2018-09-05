from pydub import AudioSegment
from scipy.io.wavfile import read
from scipy import signal
import numpy as np
import xlsxwriter
from scipy.signal import get_window

inputaudio = read("audio1.wav")  # lesen des WAV-files

audio = np.array(inputaudio[1], dtype=float)  # inputaudio in ndarray audio transformieren

f, t, Sxx = signal.spectrogram(audio, window=get_window('hamming', 1000), noverlap=500)  # spektrogramm bilden

#print(f*100000)
print(t/100000)
print(t.shape)

#print(Sxx.shape)
#print(Sxx.dtype)

matrix = np.ndarray(shape=(t.size, f.size), dtype=float, order='F')  # ndarray erstellen matrix[t,f] vgl Sxx[f,t]
maxwert = 0
twert = np.ndarray(shape=(6,), dtype=float)

print(matrix.shape)
print(matrix.dtype)

#maxwert = np.ndarray(shape=(t.size,), dtype=float)  # ndarray erstellen maxwert


#print(maxwert.shape)
#print(maxwert.dtype)

#for t0 in range(0, t.size):  # erste itteration arrays mit 0 fuellen
#    for f0 in range(0, f.size):
#        matrix[t0, f0] = 0

for t1 in range(0, t.size):  # itteration um maxwert zu bestimmen

    for f1 in range(0, f.size):
        if Sxx[f1, t1] > maxwert:
            maxwert = Sxx[f1, t1]

for t2 in range(0, t.size):  # itteration mit uebertrag und normierung auf wertebereich (0-1)
    for f2 in range(0, f.size):
        x1 = Sxx[f2, t2]
        x2 = maxwert
        if x2 == 0:
            matrix[t2, f2] = 0
        else:
            matrix[t2, f2] = x1 / x2

"""
workbook = xlsxwriter.Workbook('audio4data.xlsx')  # in excel schreiben
worksheet = workbook.add_worksheet()
for t3 in range(0, t.size):
    for f3 in range(0, f.size):
        worksheet.write((f.size - f3), t3, matrix[t3, f3])
workbook.close()
"""


# bereich bestimmung der laute a3 fuer t3
a3size = 100

a3 = np.ndarray(shape=(a3size + 2,), dtype=int)   # array erstellung muss die groesse besitze

x3 = 0
for r3 in range(0, a3size + 1):    # hier berreich des filters bauen

    a3[r3+1] = x3 + 100
    x3 = x3 + 1

    print (a3)

a3[0] = 324

for t3 in range(0, t.size):  # bestimmung des H lautes
    s3 = 0
    for aa3 in range(0, a3.size):
        s3 = s3 + matrix[t3, a3[aa3]]
    
    if s3 >= a3[0]:
        twert[0] = t3
        break

if twert[0] > 0:
    print ("twert")
    print (twert[0])


"""


#    for f3 in range(0, f.size):
#        print("t3")
        
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





#    for f4 in range(0, f.size):
#        print("t4")
        
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





#    for f5 in range(0, f.size):
#        print("t5")
        



newaudio = AudioSegment.from_wav("audio.wav")

silence = AudioSegment.silent(duration=250)

t1 = newaudio[:twert[1]]
firstslice = t1[-(twert[1]-twert[0]):]

t2 = newaudio[:twert[3]]
secondslice = t1[-(twert[3]-twert[2]):]

t3 = newaudio[:twert[5]]
thirddslice = t1[-(twert[5]-twert[4]):]

finalaudio = silence + firstslice + silence + secondslice + silence + thirddslice + silence

finalaudio.export("Ausgabe.wav", format="wav")

"""