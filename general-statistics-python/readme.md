# Full Classical Statistics Analysis Python 3.9 program with an interactive GUI 
GUI implemented with:   PySimpleGUI    https://github.com/PySimpleGUI  
  
When run, the program opens a simple to use interactive GUI that does statistical analysis on a CSV file.   
  
**NOTE: This application requires a minimum of 1920x1080 (FHD) Screen Resolution.**
  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/full_screen.PNG)    
  
  
## How to use:  

You fill out the GUI starting at the upper left corner and work down.  
  
Press the "Import Data File" button and navigate to where your .CSV data file is located.  
  
Once a valid file is read, then the plots will automatically appear, analyzed to the  
default +/- 3.0 Sigma Limits.  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/stat_controls.PNG)  
  
To change the default 3 Sigma Limits, enter the desired values in the text boxes,  
then press "Apply New Limits" to regenerate the plot (See figure above).  
  
On the "Statistics Plot" Tab, you can turn on and off all the Analysis Calculations  
that display on the plot.  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/stat_plot_controls.PNG)  
  
  
On the "Histogram Plot" Tab, you can turn on and off all the Analysis Calculations  
that display on the plot.   
Set the number of histogram bins to 'Auto' or you can adjust the number of bins used in the generation  
of the histogram manually.   
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/histogram_controls.PNG)  
   
You can also use the standard MatPlotLib controls to zoom in, pan around and save  
the plot to a file.  
*Note: It has been found on Windows 10, that after zooming around, sometimes the 'Home' button fails to reset the graph.  
If this happens, press the "Apply New Limits" button above to regenerate the graph to the default scaling.*
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/matplotlib_controls.png)  
  
## How the script works:  
  
The script reads a single column of data from the selected CSV file and   
analyzes the mean, standard deviation and then makes two plots of the resulting analysis.  
  
A sample data file is included with the files - see above for the sample .CSV file.  
  
  
  
## Example Output Plots  
  
### Statistical Analysis Of The Data,  
The first plot shows the: Mean, Trend of the Data and the 3 Sigma Upper and Lower Control Limits based  
on the analyzed data. The various analysis lines on the chart may be toggled one and off (see above).    
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/statistics.png)  
  
    
    
### Histogram Analysis Of The Data,  
The second plot is a histogram of the input data. Also showing: Mean, and the 3 sigma upper and lower control limits based  
on the analyzed data. The various analysis lines on the chart may be toggled one and off (see above).    
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/histogram.png)  
  
  
