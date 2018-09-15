from pydub import AudioSegment  #pydub for audio processing
from scipy.io.wavfile import read  #wavfile.read for import wav-file
from scipy import signal  # scipy for signalprocessing
import numpy as np  # numpy as options for complex arrays
import xlsxwriter  # exporting excel files
from scipy.signal import get_window  # differen windows for fourier transformation


def trigger1():  # def a filter detecting an [ha] sound

    a3size = 100
    b3size = 100

    a3true = 0
    b3true = 0

    a3 = np.ndarray(shape=(a3size + 2,), dtype=int)   # array erstellung
    b3 = np.ndarray(shape=(b3size + 2,), dtype=int)   # array erstellung

    x3 = 0
    for r3 in range(0, a3size + 1):

        a3[r3+1] = x3 + 100      # filter from 0 + 100 to 200 (a3size = 100)
        x3 = x3 + 1

    a3[0] = 324  # Value to exceed

    for t3 in range(0, t.size):  # iterrativ detection of sound
        s3 = 0
        for aa3 in range(1, a3.size):   # itterativ ueber alle elemente des array ausser 0
            s3 += matrix[t3, a3[aa3]]  # summation of values

        if s3 >= a3[0]:  # case of detection
            a3true = 1
            x3 = 0
            for r3 in range(0, a3size + 1):
                a3[r3 + 1] = x3 + 100  # filter from 0 + 100 to 200 (b3size = 100)
                x3 = x3 + 1

            a3[0] = 324  # Value to exceed

            for t33 in range(0, t.size):  # iterrativ detection of sound
                s33 = 0
                for bb33 in range(1, b3.size):  # itterativ ueber alle elemente des array ausser 0
                    s33 += matrix[t3, b3[bb33]]  # summation of values

                if s33 >= b3[0]:  # case of detection
                    b3true = 1
                    break
            break

    if a3true > 0 and b3true > 0:
        twert[0] = t3
    return twert[0]


inputaudio = read("audio.wav")  # lesen des WAV-files

audio = np.array(inputaudio[1], dtype=float)  # inputaudio in ndarray audio transformieren

f, t, Sxx = signal.spectrogram(audio, window=get_window('hamming', 1000), noverlap=500)  # spektrogramm bilden

print(t/100)  # printing timesteps in ms
print(t.shape)  # number of timesteps


matrix = np.ndarray(shape=(t.size, f.size), dtype=float, order='F')  # generating horizontal t and vertical f array
maxwert = 0
twert = np.ndarray(shape=(6,), dtype=float)

#print(matrix.shape)

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


workbook = xlsxwriter.Workbook('audiodata.xlsx')  # export excel file
worksheet = workbook.add_worksheet()
for t4 in range(0, t.size):
    for f4 in range(0, f.size):
        worksheet.write((f.size - f4), t4, matrix[t4, f4])
workbook.close()

trigger1()  # calling function to detect sound [ha]

# setting t values to 0
twert[0] = 0
twert[1] = 0
twert[2] = 0
twert[3] = 0
twert[4] = 0
twert[5] = 0

newaudio = AudioSegment.from_wav("audio.wav")  # reread audiofile

silence = AudioSegment.silent(duration=250)  # silence between audiosamples/slices

# cutting audio into slices
tt1 = newaudio[:twert[1]]
firstslice = tt1[-(twert[1]-twert[0]):]

tt2 = newaudio[:twert[3]]
secondslice = tt2[-(twert[3]-twert[2]):]

tt3 = newaudio[:twert[5]]
thirddslice = tt3[-(twert[5]-twert[4]):]

finalaudio = silence + firstslice + silence + secondslice + silence + thirddslice + silence  # arange slices

finalaudio.export("Ausgabe.wav", format="wav")  # export wav file
