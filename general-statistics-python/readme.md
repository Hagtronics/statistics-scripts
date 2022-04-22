## Full Classical Statistics Analysis Python 3.9 program with an interactive GUI 
  
When run the program opens a simple to use interactive GUI.   
  
**NOTE: This application requires a minimum of 1920x1080 (FHD) Screen Resolution.**
  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/full_screen.PNG)    
  
  
## How to use:  

You fill out the GUI starting at the upper left corner and work down.  
  
Press the "Import Data File" button and navigate to where your .CSV data file is located.  
  
Once a valid file is read, then the plots will automatically appear, analyzed to the  
default +/- 3.0 Sigma Limits.  

![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/stat_controls.PNG)  
  
To change the default Sigma Limits, enter the desired values in the text boxes,  
then press "Apply New Limits" to regenerate the plot (See figure above).  
  
On the "Statistics Plot" Tab, you can turn on and off all the Analysis Calculations  
that display on the plot.  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/stat_plot_controls.PNG)  
  
  
On the Histogram Plot Tab, you can set the number of histogram bins to use in the generation of the histogram.  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/histo_controls.PNG)  

You can also use the standard MatPlotLib controls to zoom in, pan around and save  
the plot to a file.  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/matplotlib_controls.png)  

## How the script works:  

The script reads a single column of data from the selected CSV file and   
analyzes the mean, standard deviation and then makes two plots of the analysis.
  
A sample data file is included with the files - see above for the sample .CSV file.
  
  
  
Example plots,  

Statistical Analysis Of The Data,  
The first plot shows the: Mean, Trend of the Data and the 3 sigma upper and lower control limits based on the analyzed data.    
  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/statistics.png)  
  
    
    
Histogram Of The Data,  
The second plot is a histogram of the input data.  
   
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/histogram.png)  


