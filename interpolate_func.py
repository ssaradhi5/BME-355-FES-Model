import matplotlib as plt
import numpy as np
import csv
import matplotlib.pyplot as plt


def interpolateData(filePath, dataLength):
    data = []
    interData = []

    with open('Raw External Data/' + filePath) as file:
        plots = csv.reader(file, delimiter=',')
        for row in plots:
            data.append(float(row[1]))

    data = np.array(data)

    lenData = len(data)

    time = 0.36

    # recreating the x-coordinates of the data points into same time range
    xp = np.linspace(0, time, lenData)

    # interpolate data for 360 points (1 point = 1 ms)
    xAxis = np.linspace(0, time, dataLength)

    interData = np.interp(xAxis, xp, data)

    with open('InterpolatedData/' +filePath +'_interpolated.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        for i in range(len(interData)):
            filewriter.writerow([xAxis[i], interData[i]])

    arr = np.genfromtxt('InterpolatedData/'+filePath +
                        '_interpolated.csv', delimiter=',')
    return arr[:, 1]

# fileNames = ['x1_ext_data', 'x2_ext_data', 'x3_ext_data', 'x4_ext_data']

interpolateData('x1_ext_data.csv', 360)
interpolateData('x2_ext_data.csv', 360)
interpolateData('x3_ext_data.csv', 360)
interpolateData('x4_ext_data.csv', 360)

