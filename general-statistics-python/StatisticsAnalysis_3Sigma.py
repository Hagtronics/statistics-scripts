"""
Simple 3 Sigma Statistical Analysis Of A 1 Column array of numbers
read in via a CSV file.

Total freeware, but: Written by an infinite number of Monkeys,
in an infinite amount of time, SO BEWARE as Monkeys have no idea how to type.

Written for,
    python 3.9.9
    matplotlib 3.5.1
"""

import os
import statistics as st
import csv
import tkinter.filedialog
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

# ===== User Setup Options ================================================

# Sigma value to use for calculating Upper and Lower Control Limit Lines
SIGMA_LIMITS = 3.0  # Usually 3.0 Sigma

# Number of Bins for the histogram plot
HIST_BINS = 15  # With lots of data, 15 bins is enough


# ===== Get file name from user dialog ========================================
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
file_name = os.path.basename(file_path)


# ===== Let 'er rip! ==========================================================
plt.close('all')
input_data = []


# Open file for reading, and read data in
with open(file_path) as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        input_data.append(float(row[0]))


# X Bar, UCL & LCL Calculations
N = len(input_data)

x_bar = st.mean(input_data)
x_bar_l = [x_bar] * N

std_dev = st.stdev(input_data)

ucl = x_bar + (SIGMA_LIMITS * std_dev)
ucl_l = [ucl] * N

lcl = x_bar - (SIGMA_LIMITS * std_dev)
lcl_l = [lcl] * N


# ===== Calculate Trend Line ===============================================
x_values = np.linspace(1, N, N)
input_data_np = np.array(input_data)
z = np.polyfit(x_values, input_data_np, 1)
p = np.poly1d(z)
trend_points = p(x_values)


# ===== Plotting ==============================================================

# Set plot size for all plots (1000x700 Pixels)
plt.rcParams['figure.figsize'] = [10, 7]

# Plot Histogram
plt.figure()
plot_title = "Histogram - " + file_name
plt.hist(input_data, bins=HIST_BINS)
plt.title(plot_title, fontsize=18, loc='center')
plt.xlabel("Measured Value", fontsize=14)
plt.ylabel("Number of Occurrences", fontsize=14)
plt.tight_layout()
plt.grid()


# Plot XmR Chart
plt.figure()
plot_title = "Statistical Analysis - " + file_name
plt.plot(input_data)
plt.plot(x_bar_l, '--')      # Mean = Dashed
plt.plot(trend_points, ':')     # Trend = Dash Dot
plt.plot(ucl_l)
plt.plot(lcl_l)
plt.title(plot_title, fontsize=18)
plt.ylabel("Measured Value", fontsize=14)
plt.grid()
plt.tight_layout()



# Show them all now (only once)
plt.show()

# ===== Fini ==================================================================
