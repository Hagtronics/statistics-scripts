"""
Based on the information on: X Bar - Moving-Range Charts

    "Understanding Variation - The Key To Managing Chaos"
    Donald J. Wheeler, 1993, SPC Press, 1993

Also see: Wheeler, D J,
    https://www.qualitydigest.com/inside/quality-insider-column/individual-charts-done-right-and-wrong.html

Total freeware, but remember this was: Written by an infinite number of Monkeys,
in an infinite amount of time, SO BEWARE as Monkeys have no idea how to type.

Written for,
    python 3.9.9
    matplotlib 3.5.1
"""

import os
import statistics as st
import matplotlib.pyplot as plt
import csv
import tkinter as tk
from tkinter import filedialog


# ===== Get file name from user dialog ========================================
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
file_name = os.path.basename(file_path)


# ===== Let 'er rip! ==========================================================
plt.close('all')
input_data = []
range_data = []


# open file for reading, and read data in
with open(file_path) as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        input_data.append(float(row[0]))


# Moving Range calculation
for i in range(1, len(input_data), 1):
    delta = abs(input_data[i] - input_data[i - 1])
    range_data.append(delta)


# X Bar, UCLr, UCL & LCL Calculations
N = len(input_data)

x_bar = st.mean(input_data)
x_bar_l = [x_bar] * N

r_bar = st.mean(range_data)
r_bar_l = [r_bar] * N

ucr = 3.268 * r_bar
ucr_l = [ucr] * N

ucl = x_bar + (2.66 * r_bar)
ucl_l = [ucl] * N

lcl = x_bar - (2.66 * r_bar)
lcl_l = [lcl] * N

# 1st Range value is undefined, fix it, so it won't plot
range_data.insert(0, float('nan'))


# ===== Plotting ==============================================================

# Set plot size for all plots (1000x700 Pixels)
plt.rcParams['figure.figsize'] = [10, 7]

# Plot Histogram
hist_bins = 15  # With lots of data, 15 bins is enough

plt.figure()
plot_title = "Histogram - " + file_name

plt.hist(input_data, bins=hist_bins)
plt.title(plot_title, fontsize=18, loc='center')
plt.xlabel("Measured Value", fontsize=14)
plt.ylabel("Number of Occurrences", fontsize=14)
plt.tight_layout()
plt.grid()


# Plot XmR Chart
plt.figure()
plot_title = "XmR - " + file_name

plt.subplot(2, 1, 1)
plt.plot(input_data)
plt.plot(x_bar_l, '--')
plt.plot(ucl_l)
plt.plot(lcl_l)
plt.title(plot_title, fontsize=18)
plt.ylabel("Measured Value", fontsize=14)
plt.grid()
plt.tight_layout()

plt.subplot(2, 1, 2)
plt.plot(range_data)
plt.plot(r_bar_l, '--')
plt.plot(ucr_l)
plt.xlabel("Measured Sequence ->", fontsize=14)
plt.ylabel("Moving Range", fontsize=14)
plt.tight_layout()
plt.grid()


# Show them all now (only once)
plt.show()

# ===== Fini ==================================================================
