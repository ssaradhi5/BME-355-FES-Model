from sklearn.preprocessing import scale
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import os
from scipy.signal import hilbert, savgol_filter


def EMG_envelope():
    """
    EMG envelope created from experimental data
    """
    ta = []
    freq = []
    for path, dirs, files in os.walk('./EMG Raw Data'):
        for file in files:
            x = loadmat(os.path.join(path, file))
            ta.append(x['s']['Data'][0][0]['EMG'][0][0][0])
            freq.append(x['s']['EMGFreq'][0][0][0][0])
            print(file)
    ta = np.array(ta)
    freq = np.array(freq)
    signals = []
    minimum = len(ta[0])
    for i, data in enumerate(ta):
        signal = np.abs((data))
        signal = savgol_filter(signal, 15, 3)
        if minimum > len(signal):
            minimum = len(signal)
        signals.append(signal)
        print(len(signal))

    signals = np.array(signals)
    for i, signal in enumerate(signals):
        signals[i] = signals[i][50:minimum]

    signal_mean = signals.mean(axis=0)
    X = scale(signal_mean, axis=0, with_mean=True, with_std=True, copy=True)
    # X=X.mean(axis=0)
    X = (X-min(X))/(max(X)-min(X))
    plt.plot(X)
    plt.show()

    np.savetxt('EMG_data.csv', X, delimiter=",")


if __name__ == "__main__":
    EMG_envelope()
