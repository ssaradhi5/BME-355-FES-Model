import numpy as np
import matplotlib.pyplot as plt


def trapezoid(offset_time=120, slope=0.1, max_value=1, directory="trapezoid.csv"):
    """
    :params: offset_time -> numbers of points needed to reach max
    :params: slope -> increasing/decreasing slope
    :params: max_value -> constant value at max
    :params: directory
    :return output: trapezoidal function 
    """
    step_size = 1

    time_tomax = offset_time
    offset_time_adjusted = offset_time/step_size
    time_tomax = int(time_tomax/step_size)
    offset_time = int(offset_time/step_size)

    times = np.arange(0, offset_time_adjusted+(time_tomax*2), step_size)
    output = np.zeros((times.shape))
    slope_array = np.linspace(0, max_value, 120)
    decrease_slope = np.linspace(max_value, 0, 119)
    print(slope_array.shape)

    output[0:time_tomax] = slope_array
    output[time_tomax: (offset_time + time_tomax)] = max_value

    output[offset_time + time_tomax: -1] = decrease_slope

    print(output.shape)
    plt.plot(output)
    plt.show()

    np.savetxt(directory, output, delimiter=',')


def resample_emg(directory='EMG_data.csv'):
    """
    Resample EMG to 360 time points
    :params: CSV directory
    """
    emg = np.genfromtxt(directory, delimiter=',')

    emg_new = emg[::2]
    emg_new = emg[0:360]

    plt.subplot(2, 2, 1)

    plt.plot(emg)
    plt.subplot(2, 2, 2)
    plt.plot(emg_new)
    # plt.show()

    print(emg_new.shape)

    directory = directory+'_resampled.csv'
    np.savetxt(directory, emg_new, delimiter=',')


if __name__ == "__main__":
    trapezoid(offset_time=120, slope=0.2, max_value=0.5)
