This Python 3.9 program is a full Classical Statistics Analysis program with a interactive GUI.  
  
When run the program opens a simple interactive GUI.   
  
NOTE: This application requires a minimum of 1920x1080 (FHD) Screen Resolution.  
  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/full_screen.PNG)    
  
  
  
How to use:  

You fill out the GUI starting at the upper left corner and work down.  
  
Press the "Import Data File" button and navigate to where your .CSV data file is.  
  
Once a valid file is read, then the plots will automatically appear, analyzed to the  
default +/- 3.0 Sigma Limits.  
  
To change the default Sigma Limits, enter the desired values in the text boxes,  
then press "Apply New Limits" to regenerate the plot.  

On the "Statistics Tab" - You can turn on and off all the Analysis Calculations  
that display on the plot.  

You can also use the standard MatPlotLib controls to zoom in, pan around and save  
the plot to a file.  


How the script works:  

The script reads a single column of data from the selected CSV file and   
analyzes the mean, standard deviation and then makes two plots of the analysis.  
  
(A sample data file is included with the files).  
  
  
  
Example plots,  

Statistical Analysis Of The Data,  
The first plot shows the: Mean, Trend of the Data and the 3 sigma upper and lower control limits based on the analyzed data.    
  
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/statistics.png)  
  
    
    
Histogram Of The Data,  
The second plot is a histogram of the input data.  
   
![image](https://github.com/Hagtronics/statistics-scripts/blob/main/general-statistics-python/histogram.png)  


