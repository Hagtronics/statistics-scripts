"""
Simple 3 Sigma Statistical Analysis Of A 1 Column array of numbers
read in via a CSV file.

Total freeware, but beware: Written by an infinite number of Monkeys,
in an infinite amount of time, SO BEWARE as Monkeys have no idea how to type,
so this is probably full of issues.

Written for and tested with,
    Win10 21H2
    python 3.9.9
    matplotlib 3.5.1
    PySimpleGUI 4.57.0

Requires,
    FHD Display - At least 1900 x 1080
    
Version History:
    22Apr22 - First Release - Steve Hageman
"""

from pathlib import PurePath
import statistics as st
import csv
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import FreeSimpleGUI as sg


# ===== Designer Setup Options ================================================

# Plot size (Global)
X_SIZE = 1800
Y_SIZE = 650


# ===== Global Data ============================================================
input_data = []
plot_ucl_flag = True
plot_lcl_flag = True
plot_mean_flag = True
plot_trend_flag = True

plot_hucl_flag = True
plot_hlcl_flag = True
plot_hmean_flag = True
plot_hbins_auto_flag = True
plot_hbins_number = 15

plot_ucl_sigma = 3
plot_lcl_sigma = 3

file_name = ""

# ===== Global Setup ==========================================================
# This is for the file dialog in main()
# root = tk.Tk()
# root.withdraw()

# ===== Helpers ===============================================================
def shorter_path(path, appx_len=20):
    """Breaks a long filepath into a smaller chunk for display purposes.

    Args:
        path (string): The full path + filename to shorten
        appx_len (int, optional): Approximate limit of the preamble string length.
        The return string WILL be longer than this.
        Defaults to 20.

    Returns:
        str: Shortened path string for display.
    """
    if not path:
        return path

    parts = list(PurePath(path).parts)

    path = PurePath(parts[0])
    for part in parts[1:-1]:
        path /= part
        if len(str(path)) >= appx_len:
            path /= " ... "
            break
    if len(parts) > 1:
        path /= parts[-1]
    return path

# ===== Helpers ===============================================================
def is_file_data_ok(file):
    """Verifies that the data file is readable

    Args:
        file (string): Path & file to the file to import

    Returns:
        bool: True if data was read in correctly
    """
    global input_data
    input_data = []

    try:
        with open(file) as csvDataFile:
            csvReader = csv.reader(csvDataFile)

            for row in csvReader:
                input_data.append(float(row[0]))
        is_ok = True
    except:
        is_ok = False
    finally:
        return is_ok


def is_valid_positive_float(in_val):
    """Validates the floating point inputs

    Args:
        in_val (string): The string to check

    Returns:
        bool: True if the string can be converted to a valid float
    """
    try:
        _ = float(in_val)
    except:
        return False

    if float(in_val) < 0.0:
        return False

    return True


# ===== Plotting Routines =====================================================
def plot_statistics():
    """Plots the Statistics Graph
    """
    global input_data
    global file_name
    global plot_ucl_flag
    global plot_lcl_flag
    global plot_mean_flag
    global plot_trend_flag
    global plot_ucl_sigma
    global plot_lcl_sigma

    plt.figure(1)
    plt.figure(1).clear()

    fig = plt.gcf()
    DPI = fig.get_dpi()

    # -------------------------------
    # you have to play with this size to reduce the movement
    # error when the mouse hovers over the figure, it's close to canvas size
    fig.set_size_inches(X_SIZE / float(DPI), Y_SIZE / float(DPI))
    ax = plt.subplot(1, 1, 1)

    if len(input_data) > 1:
        # X Bar, UCL & LCL Calculations
        N = len(input_data)

        x_bar = st.mean(input_data)

        std_dev = st.stdev(input_data)

        ucl = x_bar + (float(plot_ucl_sigma) * std_dev)

        lcl = x_bar - (float(plot_lcl_sigma) * std_dev)

        # ===== Calculate Trend Line ===============================================
        x_values = np.linspace(1, N, N)
        input_data_np = np.array(input_data)
        z = np.polyfit(x_values, input_data_np, 1)
        p = np.poly1d(z)
        trend_points = p(x_values)

        ax.plot(input_data)
               
        if plot_ucl_flag is True:
            ax.hlines(y=ucl, xmin=0, xmax=N, colors='orange', linestyles='solid')

        if plot_lcl_flag is True:
            ax.hlines(y=lcl, xmin=0, xmax=N, colors='green', linestyles='solid')
            
        if plot_mean_flag is True:
            ax.hlines(y=x_bar, xmin=0, xmax=N, colors='red', linestyles='--')

        if plot_trend_flag is True:
            ax.plot(trend_points, color='blue', linestyle=":")  # Trend = Dash Dot

    plt.title("Statistics Plot - " + file_name, fontsize=18)
    plt.xlabel("Sample", fontsize=14)
    plt.ylabel("Measurement", fontsize=14)
    plt.grid()
    plt.tight_layout()

    # Instead of plt.show()
    draw_figure_w_toolbar(
        window["fig_cv1"].TKCanvas, fig, window["controls_cv1"].TKCanvas
    )


def plot_histogram():
    """Plots the Histogram Graph
    """
    global file_name
    global plot_hbins_number

    plt.figure(2)
    plt.figure(2).clear()

    fig = plt.gcf()
    DPI = fig.get_dpi()
    # -------------------------------
    # you have to play with this size to reduce the movement
    # error when the mouse hovers over the figure, it's close to canvas size
    fig.set_size_inches(X_SIZE / float(DPI), Y_SIZE / float(DPI))
    ax = plt.subplot(1, 1, 1)

    # bins='auto' - Uses the maximum of the Sturges and Freedman-Diaconis bin choice
    if plot_hbins_auto_flag == True:
        (n, bins, patches) = ax.hist(input_data, bins='auto')
    else:
        (n, bins, patches) = ax.hist(input_data, bins=plot_hbins_number)
    
    # print(f"n={n}")         # This is the number of hits in each bin
    # print(f"bins={bins}")   # This is the center value of each bin
    # print(f"patches={patches}") # This is an object reference
    
    # n[x] is the number in each bin
    max_vert_scale = np.max(n)

    #ax.vlines(-10, 0, 100)
    
    
    if len(input_data) > 1:
        # X Bar, UCL & LCL Calculations
        x_bar = st.mean(input_data)

        std_dev = st.stdev(input_data)

        ucl = x_bar + (float(plot_ucl_sigma) * std_dev)

        lcl = x_bar - (float(plot_lcl_sigma) * std_dev)
    
        if plot_hucl_flag is True:
            ax.vlines(ucl, 0, max_vert_scale, colors='orange')
    
        if plot_hlcl_flag is True:
            ax.vlines(lcl, 0, max_vert_scale, colors='green')
            
        if plot_hmean_flag is True:
            ax.vlines(x_bar, 0, max_vert_scale, colors='red', linestyles='--')
    
    plt.title("Histogram Plot - " + file_name, fontsize=18)
    plt.xlabel("Measurement", fontsize=14)
    plt.ylabel("Number of Occurrences", fontsize=14)
    plt.grid()
    plt.tight_layout()

    # Instead of plt.show()
    draw_figure_w_toolbar(
        window["fig_cv2"].TKCanvas, fig, window["controls_cv2"].TKCanvas
    )


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    """Puts the Matplotlib Toolbar on the Graph Tab - A helper function
    """
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side="right", fill="both", expand=1)


class Toolbar(NavigationToolbar2Tk):
    """Internal Helper for the Plot Toolbars
    """
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


# ===== GUI Layout Setup ======================================================

# Statistics Graph Tab
tab1_layout = [
    [
        sg.Text("Display Options:", size=(12, 1)),
        sg.Checkbox(
            "Upper Control Limit",
            key="-UCL-",
            size=(15, 1),
            default=True,
            enable_events=True,
        ),
        sg.Checkbox(
            "Lower Control Limit",
            key="-LCL-",
            size=(15, 1),
            default=True,
            enable_events=True,
        ),
        sg.Checkbox(
            "Mean", key="-Mean-", size=(6, 1), default=True, enable_events=True
        ),
        sg.Checkbox(
            "Trend", key="-Trend-", size=(15, 1), default=True, enable_events=True
        ),
    ],
    [sg.Canvas(key="controls_cv1")],
    [
        sg.Column(
            layout=[[sg.Canvas(key="fig_cv1", size=(500 * 2, 400))]],
            background_color="#DAE0E6",
            pad=(0, 0),
        )
    ],
]

# Histogram Graph Tab
tab2_layout = [
    [
        sg.Text("Display Options:", size=(12, 1)),
        sg.Checkbox(
            "Upper Control Limit",
            key="-HUCL-",
            size=(15, 1),
            default=True,
            enable_events=True,
        ),
        sg.Checkbox(
            "Lower Control Limit",
            key="-HLCL-",
            size=(15, 1),
            default=True,
            enable_events=True,
        ),
        sg.Checkbox(
            "Mean", key="-HMean-", size=(9, 1), default=True, enable_events=True
        ),
        sg.Text("Histogram Bins: ", size=(12, 1)),
        sg.Checkbox(
            "Auto", key="-HBinsAuto-", size=(4, 1), default=True, enable_events=True
        ),
        sg.Spin(
            [i for i in range(5, 100)],
            initial_value=15,
            key="-HBins-",
            size=(4, 1),
            enable_events=True,
            disabled=True
        ),
    ],
    [sg.Canvas(key="controls_cv2")],
    [
        sg.Column(
            layout=[[sg.Canvas(key="fig_cv2", size=(500 * 2, 400))]],
            background_color="#DAE0E6",
            pad=(0, 0),
        )
    ],
]

tab_group_layout = [
    [
        sg.Tab("Statistics Plot", tab1_layout, key="-PlotStat-"),
        sg.Tab("Histogram Plot", tab2_layout, key="-PlotHist-"),
    ]
]

# Main Window Layout
layout = [
    [sg.Text("Import Data File:")],
    [
        sg.Button("Import Data File", key="-File-"),
        sg.Text("File: ", size=(3, 1)),
        sg.Text("(No file imported)", key="-FilePath-", size=(70, 1)),
    ],
    [sg.HorizontalSeparator()],
    [
        sg.Text("Upper Sigma Limit ", size=(18, 1)),
        sg.InputText("3.0", key="-USL-", size=(10, 1)),
    ],
    [
        sg.Text("Lower Sigma Limit ", size=(18, 1)),
        sg.InputText("3.0", key="-LSL-", size=(10, 1)),
        sg.Button("Apply New Limits", key="-RePlot-", size=(13, 1)),
    ],
    [sg.HorizontalSeparator()],
    [sg.TabGroup(tab_group_layout, enable_events=True, key="-TABGROUP-")],
]

# Window Constructor
window = sg.Window(
    "Statistics Calculator",
    layout,
    default_element_size=(15, 1),
    text_justification="l",
    auto_size_text=False,
    auto_size_buttons=False,
    keep_on_top=False,
    grab_anywhere=False,
    default_button_element_size=(14, 1),
    location=(25, 20),
    # size=(300,300),
    finalize=True,
)


#===== Main() =================================================================
def main():

    global file_name
    global input_data
    
    global plot_ucl_flag
    global plot_lcl_flag
    global plot_mean_flag
    global plot_trend_flag
    global plot_hucl_flag
    global plot_hlcl_flag
    global plot_hmean_flag
    global plot_hbins_auto_flag
    global plot_hbins_number
    
    global plot_ucl_sigma
    global plot_lcl_sigma

    # For the TkInter file open dialog
    root = tk.Tk()
    root.withdraw()

    # Plot blank plots first
    plot_histogram()
    plot_statistics()

    # ===== PySimpleGui Big Loop ==============================================
    while True:

        event, values = window.Read()
        # print(f"events: {event} \nvalues: {values}")

        if event == sg.WIN_CLOSED:
            print("Normal Exit - Window Closed...")
            break

        if event == "-File-":
            path_file = tk.filedialog.askopenfilename(
                filetypes=((("CSV"), "*.csv"), (("All files"), "*.*"))
            )

            if len(path_file) < 1:
                continue

            if is_file_data_ok(path_file) != True:
                sg.popup(
                    "The file selected was not a valid CSV data file.", keep_on_top=True
                )
                # Reset nearly everything on bad import
                input_data.clear()
                file_name = ""
                path_file = ""
                window["-FilePath-"].update(shorter_path(path_file, 80))
                window["-USL-"].update("3.0")
                plot_ucl_sigma = 3.0
                window["-LSL-"].update("3.0")
                plot_lcl_sigma = 3.0
                plot_statistics()
                plot_histogram()
                continue

            # Data file import appears good - so plot
            window["-FilePath-"].update(shorter_path(path_file, 80))
            file_name = str(PurePath(path_file).name)

            # Validate the Sigma Calculation Values
            temp = values["-USL-"]
            if not is_valid_positive_float(temp):
                sg.popup(
                    f"The input Upper Sigma Limit is not a valid, positive floating point number: {temp}",
                    keep_on_top=True,
                )
                window["-USL-"].update("3.0")
                plot_ucl_sigma = 3.0
            else:
                plot_ucl_sigma = float(values["-USL-"])

            temp = values["-LSL-"]
            if not is_valid_positive_float(temp):
                sg.popup(
                    f"The input Lower Sigma Limit is not a valid, positive floating point number: {temp}",
                    keep_on_top=True,
                )
                window["-LSL-"].update("3.0")
                plot_lcl_sigma = 3.0
            else:
                plot_lcl_sigma = float(values["-LSL-"])

            # Now plot....
            plot_statistics()
            plot_histogram()
            continue

        if event == "-RePlot-":
            
            # Validate the Sigma Calculation Values
            temp = values["-USL-"]
            if not is_valid_positive_float(temp):
                sg.popup(
                    f"The input Upper Sigma Limit is not a valid, positive floating point number: {temp}",
                    keep_on_top=True,
                )
                window["-USL-"].update("3.0")
                plot_ucl_sigma = 3.0
            else:
                plot_ucl_sigma = float(values["-USL-"])

            temp = values["-LSL-"]
            if not is_valid_positive_float(temp):
                sg.popup(
                    f"The input Lower Sigma Limit is not a valid, positive floating point number: {temp}",
                    keep_on_top=True,
                )
                window["-LSL-"].update("3.0")
                plot_lcl_sigma = 3.0
            else:
                plot_lcl_sigma = float(values["-LSL-"])

            # Now plot
            plot_statistics()
            continue

        # Statistics Plot Display Options
        if event in ("-UCL-", "-LCL-", "-Mean-", "-Trend-"):
            
            if values["-UCL-"] == False:
                plot_ucl_flag = False
            else:
                plot_ucl_flag = True

            if values["-LCL-"] == False:
                plot_lcl_flag = False
            else:
                plot_lcl_flag = True

            if values["-Mean-"] == False:
                plot_mean_flag = False
            else:
                plot_mean_flag = True

            if values["-Trend-"] == False:
                plot_trend_flag = False
            else:
                plot_trend_flag = True

            # Validate the Sigma Calculation Values
            temp = values["-USL-"]
            if not is_valid_positive_float(temp):
                sg.popup(
                    f"The input Upper Sigma Limit is not a valid, positive floating point number: {temp}",
                    keep_on_top=True,
                )
                window["-USL-"].update("3.0")
                plot_ucl_sigma = 3.0
            else:
                plot_ucl_sigma = float(values["-USL-"])

            temp = values["-LSL-"]
            if not is_valid_positive_float(temp):
                sg.popup(
                    f"The input Lower Sigma Limit is not a valid, positive floating point number: {temp}",
                    keep_on_top=True,
                )
                window["-LSL-"].update("3.0")
                plot_lcl_sigma = 3.0
            else:
                plot_lcl_sigma = float(values["-LSL-"])

            # Update the plot
            plot_statistics()
            continue

        if event in ("-HUCL-", "-HLCL-", "-HMean-", "-HBinsAuto-"):
            
            if values["-HUCL-"] == False:
                plot_hucl_flag = False
            else:
                plot_hucl_flag = True
            
            if values["-HLCL-"] == False:
                plot_hlcl_flag = False
            else:
                plot_hlcl_flag = True

            if values["-HMean-"] == False:
                plot_hmean_flag = False
            else:
                plot_hmean_flag = True

            if values["-HBinsAuto-"] == False:
                plot_hbins_auto_flag = False
                window["-HBins-"].update(disabled=False)
            else:
                plot_hbins_auto_flag = True
                window["-HBins-"].update(disabled=True)
            
            plot_histogram()
            continue

        # Will only happen if HBinsAuto is unchecked
        if event in ("-HBins-"):
            plot_hbins_number = values["-HBins-"]
            plot_histogram()
            continue

    # GUI Exit
    window.Close()


if __name__ == "__main__":
    main()

# ===== Fini ==================================================================
