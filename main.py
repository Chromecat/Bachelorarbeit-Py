from pydub import AudioSegment  #pydub for audio processing
from scipy.io.wavfile import read  #wavfile.read for import wav-file
from scipy import signal  # scipy for signalprocessing
import numpy as np  # numpy as options for complex arrays
import xlsxwriter  # exporting excel files
from scipy.signal import get_window  # differen windows for fourier transformation

sound = "audio.wav"


def trigger1():  # def a filter detecting an [ha] sound

    filtersize = 20
    correctiontime = -15
    duration = 200

    boolean = 0

    filterarray = np.ndarray(shape=(filtersize + 2,), dtype=int)   # array erstellung

    offset = 0
    for runtimefillingarray in range(0, filtersize + 1):

        filterarray[runtimefillingarray+1] = offset
        offset = offset + 1

    filterarray[0] = 2  # Value to exceed

    for runtimetime in range(0, t.size):  # iterrativ detection of sound
        summoffrequencys = 0
        for runtimefilterarray in range(1, filterarray.size):   # itterativ ueber alle elemente des array ausser 0
            summoffrequencys += matrix[runtimetime, filterarray[runtimefilterarray]]  # summation of values

        if summoffrequencys >= filterarray[0]:  # case of detection
            boolean = 1
            print(summoffrequencys)
            print(runtimetime)
            break

    if boolean > 0:
        twert[0] = (runtimetime + correctiontime) * 5
        twert[1] = twert[0] + duration
    return twert[0]


inputaudio = read(sound)  # lesen des WAV-files

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

# end spectrogram converting

"""workbook = xlsxwriter.Workbook('audiodata.xlsx')  # export excel file
worksheet = workbook.add_worksheet()
for t4 in range(0, t.size):
    for f4 in range(0, f.size):
        worksheet.write((f.size - f4), t4, matrix[t4, f4])
workbook.close()"""

# end excel export

# setting t values to 0
twert[0] = 0
twert[1] = 0
twert[2] = 500
twert[3] = 700
twert[4] = 0
twert[5] = 0

trigger1()  # calling function to detect sound [ha]

newaudio = AudioSegment.from_wav(sound)  # reread audiofile

silence = AudioSegment.silent(duration=250)  # silence between audiosamples/slices

# cutting audio into slices
tt1 = newaudio[:twert[1]]
firstslice = tt1[-(twert[1]-twert[0]):]

tt2 = newaudio[:twert[3]]
secondslice = tt2[-(twert[3]-twert[2]):]

tt3 = newaudio[:twert[5]]
thirddslice = tt3[-(twert[5]-twert[4]):]

finalaudio = silence + firstslice + silence + firstslice + silence + firstslice + silence  # arange slices

finalaudio.export("Probandoutput.wav", format="wav")  # export wav file
