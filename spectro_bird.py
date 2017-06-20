import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

rate, audio = wavfile.read('golden_winged_.wav')

f, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(audio)
ax1.set_title('Audio signal')

Pxx, freqs, bins, im = ax2.specgram(audio, cmap=plt.cm.gray)
ax2.set_title('Spectrogram')

plt.show()
